"""
Numerous benchmarks of specific functionality.
"""
import json
import os
import platform
from datetime import date, datetime, timedelta, timezone
from typing import Dict, FrozenSet, List, Optional, Set, Union

import pytest

from pydantic_core import PydanticValueError, SchemaValidator, ValidationError, ValidationError as CoreValidationError

if os.getenv('BENCHMARK_VS_PYDANTIC'):
    try:
        from pydantic import BaseModel, StrictBool, StrictInt, StrictStr, ValidationError as PydanticValidationError
    except ImportError:
        BaseModel = None
else:
    BaseModel = None

skip_pydantic = pytest.mark.skipif(BaseModel is None, reason='skipping benchmarks vs. pydantic')


class TestBenchmarkSimpleModel:
    @pytest.fixture(scope='class')
    def pydantic_model(self):
        class PydanticModel(BaseModel):
            name: str
            age: int
            friends: List[int]
            settings: Dict[str, float]

        return PydanticModel

    @pytest.fixture(scope='class')
    def core_validator_fs(self):
        class CoreModel:
            __slots__ = '__dict__', '__fields_set__'

        return SchemaValidator(
            {
                'type': 'new-class',
                'class_type': CoreModel,
                'schema': {
                    'type': 'typed-dict',
                    'return_fields_set': True,
                    'fields': {
                        'name': {'schema': {'type': 'str'}},
                        'age': {'schema': {'type': 'int'}},
                        'friends': {'schema': {'type': 'list', 'items_schema': 'int'}},
                        'settings': {'schema': {'type': 'dict', 'keys_schema': 'str', 'values_schema': 'float'}},
                    },
                },
            }
        )

    @pytest.fixture(scope='class')
    def core_validator_not_fs(self):
        class CoreModel:
            __slots__ = '__dict__', '__fields_set__'

        return SchemaValidator(
            {
                'type': 'new-class',
                'class_type': CoreModel,
                'schema': {
                    'type': 'typed-dict',
                    'fields': {
                        'name': {'schema': {'type': 'str'}},
                        'age': {'schema': {'type': 'int'}},
                        'friends': {'schema': {'type': 'list', 'items_schema': 'int'}},
                        'settings': {'schema': {'type': 'dict', 'keys_schema': 'str', 'values_schema': 'float'}},
                    },
                },
            }
        )

    data = {'name': 'John', 'age': 42, 'friends': list(range(200)), 'settings': {f'v_{i}': i / 2.0 for i in range(50)}}

    @skip_pydantic
    @pytest.mark.benchmark(group='simple model - python')
    def test_pyd_python(self, pydantic_model, benchmark):
        benchmark(pydantic_model.parse_obj, self.data)

    @pytest.mark.benchmark(group='simple model - python')
    def test_core_python_fs(self, core_validator_fs, benchmark):
        m = core_validator_fs.validate_python(self.data)
        assert m.name == 'John'
        assert m.__dict__.keys() == {'name', 'age', 'friends', 'settings'}
        assert m.__fields_set__ == {'name', 'age', 'friends', 'settings'}
        benchmark(core_validator_fs.validate_python, self.data)

    @pytest.mark.benchmark(group='simple model - python')
    def test_core_python_not_fs(self, core_validator_not_fs, benchmark):
        m = core_validator_not_fs.validate_python(self.data)
        assert m.name == 'John'
        assert m.__dict__.keys() == {'name', 'age', 'friends', 'settings'}
        assert not hasattr(m, '__fields_set__')
        benchmark(core_validator_not_fs.validate_python, self.data)

    @skip_pydantic
    @pytest.mark.benchmark(group='simple model - JSON')
    def test_pyd_json(self, pydantic_model, benchmark):
        json_data = json.dumps(self.data)

        @benchmark
        def pydantic_json():
            obj = json.loads(json_data)
            return pydantic_model.parse_obj(obj)

    @pytest.mark.benchmark(group='simple model - JSON')
    def test_core_json_fs(self, core_validator_fs, benchmark):
        json_data = json.dumps(self.data)
        benchmark(core_validator_fs.validate_json, json_data)

    @pytest.mark.benchmark(group='simple model - JSON')
    def test_core_json_not_fs(self, core_validator_not_fs, benchmark):
        json_data = json.dumps(self.data)
        benchmark(core_validator_not_fs.validate_json, json_data)


bool_cases = [True, False, 0, 1, '0', '1', 'true', 'false', 'True', 'False']


@skip_pydantic
@pytest.mark.benchmark(group='bool')
def test_bool_pyd(benchmark):
    class PydanticModel(BaseModel):
        value: bool

    @benchmark
    def t():
        for case in bool_cases:
            PydanticModel(value=case)


@pytest.mark.benchmark(group='bool')
def test_bool_core(benchmark):
    schema_validator = SchemaValidator({'type': 'bool'})

    @benchmark
    def t():
        for case in bool_cases:
            schema_validator.validate_python(case)


small_class_data = {'name': 'John', 'age': 42}


@skip_pydantic
@pytest.mark.benchmark(group='create small model')
def test_small_class_pyd(benchmark):
    class PydanticModel(BaseModel):
        name: str
        age: int

    benchmark(PydanticModel.parse_obj, small_class_data)


@pytest.mark.benchmark(group='create small model')
def test_small_class_core_dict(benchmark):
    model_schema = {
        'type': 'typed-dict',
        'fields': {'name': {'schema': {'type': 'str'}}, 'age': {'schema': {'type': 'int'}}},
    }
    dict_schema_validator = SchemaValidator(model_schema)
    benchmark(dict_schema_validator.validate_python, small_class_data)


@pytest.mark.benchmark(group='create small model')
def test_small_class_core_model(benchmark):
    class MyCoreModel:
        # this is not required, but it avoids `__fields_set__` being included in `__dict__`
        __slots__ = '__dict__', '__fields_set__'
        # these are here just as decoration
        name: str
        age: int

    model_schema_validator = SchemaValidator(
        {
            'type': 'new-class',
            'class_type': MyCoreModel,
            'schema': {
                'type': 'typed-dict',
                'return_fields_set': True,
                'fields': {'name': {'schema': {'type': 'str'}}, 'age': {'schema': {'type': 'int'}}},
            },
        }
    )
    benchmark(model_schema_validator.validate_python, small_class_data)


@pytest.mark.benchmark(group='string')
def test_core_string_lax(benchmark):
    validator = SchemaValidator({'type': 'str'})
    input_str = 'Hello ' * 20

    benchmark(validator.validate_python, input_str)


@pytest.fixture
def recursive_model_data():
    data = {'width': -1}

    _data = data
    for i in range(100):
        _data['branch'] = {'width': i}
        _data = _data['branch']
    return data


@pytest.mark.skipif(platform.python_implementation() == 'PyPy', reason='crashes on pypy due to recursion depth')
@skip_pydantic
@pytest.mark.benchmark(group='recursive model')
def test_recursive_model_pyd(recursive_model_data, benchmark):
    class PydanticBranch(BaseModel):
        width: int
        branch: Optional['PydanticBranch'] = None  # noqa: F821

    benchmark(PydanticBranch.parse_obj, recursive_model_data)


@pytest.mark.skipif(platform.python_implementation() == 'PyPy', reason='crashes on pypy due to recursion depth')
@pytest.mark.benchmark(group='recursive model')
def test_recursive_model_core(recursive_model_data, benchmark):
    class CoreBranch:
        # this is not required, but it avoids `__fields_set__` being included in `__dict__`
        __slots__ = '__dict__', '__fields_set__'

    v = SchemaValidator(
        {
            'ref': 'Branch',
            'type': 'new-class',
            'class_type': CoreBranch,
            'schema': {
                'type': 'typed-dict',
                'return_fields_set': True,
                'fields': {
                    'width': {'schema': {'type': 'int'}},
                    'branch': {
                        'schema': {'type': 'nullable', 'schema': {'type': 'recursive-ref', 'schema_ref': 'Branch'}},
                        'default': None,
                    },
                },
            },
        }
    )
    benchmark(v.validate_python, recursive_model_data)


@skip_pydantic
@pytest.mark.benchmark(group='List[TypedDict]')
def test_list_of_dict_models_pyd(benchmark):
    class PydanticBranch(BaseModel):
        width: int

    class PydanticRoot(BaseModel):
        __root__: List[PydanticBranch]

    data = [{'width': i} for i in range(100)]
    benchmark(PydanticRoot.parse_obj, data)


@pytest.mark.benchmark(group='List[TypedDict]')
def test_list_of_dict_models_core(benchmark):
    v = SchemaValidator(
        {'type': 'list', 'items_schema': {'type': 'typed-dict', 'fields': {'width': {'schema': {'type': 'int'}}}}}
    )

    data = [{'width': i} for i in range(100)]
    benchmark(v.validate_python, data)


list_of_ints_data = ([i for i in range(1000)], [str(i) for i in range(1000)])


@skip_pydantic
@pytest.mark.benchmark(group='List[int]')
def test_list_of_ints_pyd_py(benchmark):
    class PydanticModel(BaseModel):
        __root__: List[int]

    @benchmark
    def t():
        PydanticModel.parse_obj(list_of_ints_data[0])
        PydanticModel.parse_obj(list_of_ints_data[1])


@pytest.mark.benchmark(group='List[int]')
def test_list_of_ints_core_py(benchmark):
    v = SchemaValidator({'type': 'list', 'items_schema': {'type': 'int'}})

    @benchmark
    def t():
        v.validate_python(list_of_ints_data[0])
        v.validate_python(list_of_ints_data[1])


@skip_pydantic
@pytest.mark.benchmark(group='List[int] JSON')
def test_list_of_ints_pyd_json(benchmark):
    class PydanticModel(BaseModel):
        __root__: List[int]

    json_data = [json.dumps(d) for d in list_of_ints_data]

    @benchmark
    def t():
        PydanticModel.parse_obj(json.loads(json_data[0]))
        PydanticModel.parse_obj(json.loads(json_data[1]))


@pytest.mark.benchmark(group='List[int] JSON')
def test_list_of_ints_core_json(benchmark):
    v = SchemaValidator({'type': 'list', 'items_schema': {'type': 'int'}})

    json_data = [json.dumps(d) for d in list_of_ints_data]

    @benchmark
    def t():
        v.validate_json(json_data[0])
        v.validate_json(json_data[1])


@skip_pydantic
@pytest.mark.benchmark(group='List[Any]')
def test_list_of_any_pyd_py(benchmark):
    class PydanticModel(BaseModel):
        __root__: list

    @benchmark
    def t():
        PydanticModel.parse_obj(list_of_ints_data[0])
        PydanticModel.parse_obj(list_of_ints_data[1])


@pytest.mark.benchmark(group='List[Any]')
def test_list_of_any_core_py(benchmark):
    v = SchemaValidator({'type': 'list'})

    @benchmark
    def t():
        v.validate_python(list_of_ints_data[0])
        v.validate_python(list_of_ints_data[1])


set_of_ints_data = ({i for i in range(1000)}, {str(i) for i in range(1000)})


@skip_pydantic
@pytest.mark.benchmark(group='Set[int]')
def test_set_of_ints_pyd(benchmark):
    class PydanticModel(BaseModel):
        __root__: Set[int]

    @benchmark
    def t():
        PydanticModel.parse_obj(set_of_ints_data[0])
        PydanticModel.parse_obj(set_of_ints_data[1])


@pytest.mark.benchmark(group='Set[int]')
def test_set_of_ints_core(benchmark):
    v = SchemaValidator({'type': 'set', 'items_schema': {'type': 'int'}})

    @benchmark
    def t():
        v.validate_python(set_of_ints_data[0])
        v.validate_python(set_of_ints_data[1])


@skip_pydantic
@pytest.mark.benchmark(group='Set[int] JSON')
def test_set_of_ints_pyd_json(benchmark):
    class PydanticModel(BaseModel):
        __root__: Set[int]

    json_data = [json.dumps(list(d)) for d in set_of_ints_data]

    @benchmark
    def t():
        PydanticModel.parse_obj(json.loads(json_data[0]))
        PydanticModel.parse_obj(json.loads(json_data[1]))


@pytest.mark.benchmark(group='Set[int] JSON')
def test_set_of_ints_core_json(benchmark):
    v = SchemaValidator({'type': 'set', 'items_schema': {'type': 'int'}})

    json_data = [json.dumps(list(d)) for d in set_of_ints_data]

    @benchmark
    def t():
        v.validate_json(json_data[0])
        v.validate_json(json_data[1])


frozenset_of_ints = frozenset({i for i in range(1000)})


@skip_pydantic
@pytest.mark.benchmark(group='FrozenSet[int]')
def test_frozenset_of_ints_pyd(benchmark):
    class PydanticModel(BaseModel):
        __root__: FrozenSet[int]

    benchmark(PydanticModel.parse_obj, frozenset_of_ints)


@pytest.mark.benchmark(group='FrozenSet[int]')
def test_frozenset_of_ints_core(benchmark):
    v = SchemaValidator({'type': 'frozenset', 'items_schema': {'type': 'int'}})

    benchmark(v.validate_python, frozenset_of_ints)


dict_of_ints_data = ({str(i): i for i in range(1000)}, {str(i): str(i) for i in range(1000)})


@skip_pydantic
@pytest.mark.benchmark(group='Dict[str, int]')
def test_dict_of_ints_pyd(benchmark):
    class PydanticModel(BaseModel):
        __root__: Dict[str, int]

    @benchmark
    def t():
        PydanticModel.parse_obj(dict_of_ints_data[0])
        PydanticModel.parse_obj(dict_of_ints_data[1])


@pytest.mark.benchmark(group='Dict[str, int]')
def test_dict_of_ints_core(benchmark):
    v = SchemaValidator({'type': 'dict', 'keys_schema': 'str', 'values_schema': 'int'})

    @benchmark
    def t():
        v.validate_python(dict_of_ints_data[0])
        v.validate_python(dict_of_ints_data[1])


@pytest.mark.benchmark(group='Dict[any, any]')
def test_dict_of_any_core(benchmark):
    v = SchemaValidator({'type': 'dict'})

    @benchmark
    def t():
        v.validate_python(dict_of_ints_data[0])
        v.validate_python(dict_of_ints_data[1])


@skip_pydantic
@pytest.mark.benchmark(group='Dict[str, int] JSON')
def test_dict_of_ints_pyd_json(benchmark):
    class PydanticModel(BaseModel):
        __root__: Dict[str, int]

    json_data = [json.dumps(d) for d in dict_of_ints_data]

    @benchmark
    def t():
        PydanticModel.parse_obj(json.loads(json_data[0]))
        PydanticModel.parse_obj(json.loads(json_data[1]))


@pytest.mark.benchmark(group='Dict[str, int] JSON')
def test_dict_of_ints_core_json(benchmark):
    v = SchemaValidator({'type': 'dict', 'keys_schema': 'str', 'values_schema': 'int'})

    json_data = [json.dumps(d) for d in dict_of_ints_data]

    @benchmark
    def t():
        v.validate_json(json_data[0])
        v.validate_json(json_data[1])


many_models_data = [{'age': i} for i in range(1000)]


@skip_pydantic
@pytest.mark.benchmark(group='List[SimpleMode]')
def test_many_models_pyd(benchmark):
    class SimpleMode(BaseModel):
        age: int

    class PydanticModel(BaseModel):
        __root__: List[SimpleMode]

    benchmark(PydanticModel.parse_obj, many_models_data)


@pytest.mark.benchmark(group='List[DictSimpleMode]')
def test_many_models_core_dict(benchmark):
    model_schema = {'type': 'list', 'items_schema': {'type': 'typed-dict', 'fields': {'age': {'schema': 'int'}}}}
    v = SchemaValidator(model_schema)
    benchmark(v.validate_python, many_models_data)


@pytest.mark.benchmark(group='List[SimpleMode]')
def test_many_models_core_model(benchmark):
    class MyCoreModel:
        __slots__ = '__dict__', '__fields_set__'

    v = SchemaValidator(
        {
            'type': 'list',
            'items_schema': {
                'type': 'new-class',
                'class_type': MyCoreModel,
                'schema': {'type': 'typed-dict', 'return_fields_set': True, 'fields': {'age': {'schema': 'int'}}},
            },
        }
    )
    benchmark(v.validate_python, many_models_data)


list_of_nullable_data = [None if i % 2 else i for i in range(1000)]


@skip_pydantic
@pytest.mark.benchmark(group='List[Nullable[int]]')
def test_list_of_nullable_pyd(benchmark):
    class PydanticModel(BaseModel):
        __root__: List[Optional[int]]

    benchmark(PydanticModel.parse_obj, list_of_nullable_data)


@pytest.mark.benchmark(group='List[Nullable[int]]')
def test_list_of_nullable_core(benchmark):
    v = SchemaValidator({'type': 'list', 'items_schema': {'type': 'nullable', 'schema': 'int'}})

    benchmark(v.validate_python, list_of_nullable_data)


some_bytes = b'0' * 1000


@pytest.mark.benchmark(group='bytes')
def test_bytes_core(benchmark):
    v = SchemaValidator({'type': 'bytes'})

    benchmark(v.validate_python, some_bytes)


@skip_pydantic
@pytest.mark.benchmark(group='bytes')
def test_bytes_pyd(benchmark):
    class PydanticModel(BaseModel):
        __root__: bytes

    benchmark(PydanticModel.parse_obj, some_bytes)


class TestBenchmarkDateTime:
    @pytest.fixture(scope='class')
    def pydantic_model(self):
        class PydanticModel(BaseModel):
            dt: datetime

        return PydanticModel

    @pytest.fixture(scope='class')
    def core_validator(self):
        class CoreModel:
            __slots__ = '__dict__', '__fields_set__'

        return SchemaValidator(
            {
                'type': 'new-class',
                'class_type': CoreModel,
                'schema': {'type': 'typed-dict', 'return_fields_set': True, 'fields': {'dt': {'schema': 'datetime'}}},
            }
        )

    @pytest.fixture(scope='class')
    def datetime_raw(self):
        return datetime.utcnow().replace(tzinfo=timezone.utc) + timedelta(days=1)

    @pytest.fixture(scope='class')
    def datetime_str(self, datetime_raw):
        return str(datetime_raw)

    @pytest.fixture(scope='class')
    def python_data_dict(self, datetime_raw):
        return {'dt': datetime_raw}

    @pytest.fixture(scope='class')
    def json_dict_data(self, datetime_str):
        return json.dumps({'dt': datetime_str})

    @skip_pydantic
    @pytest.mark.benchmark(group='datetime model - python')
    def test_pyd_python(self, pydantic_model, benchmark, python_data_dict):
        benchmark(pydantic_model.parse_obj, python_data_dict)

    @pytest.mark.benchmark(group='datetime model - python')
    def test_core_python(self, core_validator, benchmark, python_data_dict):
        benchmark(core_validator.validate_python, python_data_dict)

    @skip_pydantic
    @pytest.mark.benchmark(group='datetime model - JSON')
    def test_model_pyd_json(self, pydantic_model, benchmark, json_dict_data):
        @benchmark
        def pydantic_json():
            obj = json.loads(json_dict_data)
            return pydantic_model.parse_obj(obj)

    @pytest.mark.benchmark(group='datetime model - JSON')
    def test_model_core_json(self, core_validator, benchmark, json_dict_data):
        benchmark(core_validator.validate_json, json_dict_data)

    @pytest.mark.benchmark(group='datetime datetime')
    def test_core_raw(self, benchmark, datetime_raw):
        v = SchemaValidator({'type': 'datetime'})

        benchmark(v.validate_python, datetime_raw)

    @pytest.mark.benchmark(group='datetime str')
    def test_core_str(self, benchmark, datetime_str):
        v = SchemaValidator({'type': 'datetime'})

        benchmark(v.validate_python, datetime_str)

    @pytest.mark.benchmark(group='datetime future')
    def test_core_future(self, benchmark, datetime_raw):
        v = SchemaValidator({'type': 'datetime', 'gt': datetime.now()})

        benchmark(v.validate_python, datetime_raw)

    @pytest.mark.benchmark(group='datetime future')
    def test_core_future_str(self, benchmark, datetime_str):
        v = SchemaValidator({'type': 'datetime', 'gt': datetime.now()})

        benchmark(v.validate_python, datetime_str)


class TestBenchmarkDateX:
    @pytest.fixture(scope='class')
    def validator(self):
        return SchemaValidator({'type': 'date'})

    @pytest.mark.benchmark(group='date from date')
    def test_date_from_date(self, benchmark, validator):
        benchmark(validator.validate_python, date.today())

    @pytest.mark.benchmark(group='date from str')
    def test_date_from_str(self, benchmark, validator):
        benchmark(validator.validate_python, str(date.today()))

    @pytest.mark.benchmark(group='date from datetime')
    def test_date_from_datetime(self, benchmark, validator):
        benchmark(validator.validate_python, datetime(2000, 1, 1))

    @pytest.mark.benchmark(group='date from datetime str')
    def test_date_from_datetime_str(self, benchmark, validator):
        benchmark(validator.validate_python, str(datetime(2000, 1, 1)))

    @pytest.mark.benchmark(group='date future')
    def test_core_future(self, benchmark):
        v = SchemaValidator({'type': 'date', 'gt': date.today()})

        benchmark(v.validate_python, date(2032, 1, 1))

    @pytest.mark.benchmark(group='date future')
    def test_core_future_str(self, benchmark):
        v = SchemaValidator({'type': 'date', 'gt': date.today()})

        benchmark(v.validate_python, str(date(2032, 1, 1)))


class TestBenchmarkUnion:
    @pytest.mark.benchmark(group='smart-union')
    def test_smart_union_core(self, benchmark):
        v = SchemaValidator({'type': 'union', 'choices': [{'type': 'bool'}, {'type': 'int'}, {'type': 'str'}]})

        benchmark(v.validate_python, 1)

    @skip_pydantic
    @pytest.mark.benchmark(group='smart-union')
    def test_smart_union_pyd(self, benchmark):
        # default pydantic-core behavior matches pydantic one with `Config.smart_union`
        class PydanticModel(BaseModel, smart_union=True):
            __root__: Union[bool, int, str]

        benchmark(PydanticModel.parse_obj, 1)

    @pytest.mark.benchmark(group='smart-union-coerce')
    def test_smart_union_coerce_core(self, benchmark):
        v = SchemaValidator({'type': 'union', 'choices': [{'type': 'bool'}, {'type': 'str'}]})

        benchmark(v.validate_python, 1)  # will be True

    @skip_pydantic
    @pytest.mark.benchmark(group='smart-union-coerce')
    def test_smart_union_coerce_pyd(self, benchmark):
        class PydanticModel(BaseModel, smart_union=True):
            __root__: Union[bool, str]

        benchmark(PydanticModel.parse_obj, 1)  # will be True

    @pytest.mark.benchmark(group='strict-union')
    def test_strict_union_core(self, benchmark):
        v = SchemaValidator(
            {'type': 'union', 'strict': True, 'choices': [{'type': 'bool'}, {'type': 'int'}, {'type': 'str'}]}
        )

        benchmark(v.validate_python, 1)

    @skip_pydantic
    @pytest.mark.benchmark(group='strict-union')
    def test_strict_union_pyd(self, benchmark):
        class PydanticModel(BaseModel):
            __root__: Union[StrictBool, StrictInt, StrictStr]

        benchmark(PydanticModel.parse_obj, 1)  # will be True

    @pytest.mark.benchmark(group='strict-union-error')
    def test_strict_union_error_core(self, benchmark):
        v = SchemaValidator({'type': 'union', 'strict': True, 'choices': [{'type': 'bool'}, {'type': 'str'}]})

        def validate_with_expected_error():
            try:
                v.validate_python(2)
                assert False
            except CoreValidationError:
                assert True

        benchmark(validate_with_expected_error)

    @skip_pydantic
    @pytest.mark.benchmark(group='strict-union-error')
    def test_strict_union_error_pyd(self, benchmark):
        class PydanticModel(BaseModel):
            __root__: Union[StrictBool, StrictStr]

        def validate_with_expected_error():
            try:
                PydanticModel.parse_obj(2)
                assert False
            except PydanticValidationError:
                assert True

        benchmark(validate_with_expected_error)


@pytest.mark.benchmark(group='raise-error')
def test_dont_raise_error(benchmark):
    def f(input_value, **kwargs):
        return input_value

    v = SchemaValidator({'type': 'function', 'mode': 'plain', 'function': f})

    @benchmark
    def t():
        v.validate_python(42)


@pytest.mark.benchmark(group='raise-error')
def test_raise_error_value_error(benchmark):
    def f(input_value, **kwargs):
        raise ValueError('this is a custom error')

    v = SchemaValidator({'type': 'function', 'mode': 'plain', 'function': f})

    @benchmark
    def t():
        try:
            v.validate_python(42)
        except ValidationError:
            pass
        else:
            raise RuntimeError('expected ValidationError')


@pytest.mark.benchmark(group='raise-error')
def test_raise_error_custom(benchmark):
    def f(input_value, **kwargs):
        raise PydanticValueError('my_error', 'this is a custom error {foo}', {'foo': 'FOOBAR'})

    v = SchemaValidator({'type': 'function', 'mode': 'plain', 'function': f})

    @benchmark
    def t():
        try:
            v.validate_python(42)
        except ValidationError:
            pass
        else:
            raise RuntimeError('expected ValidationError')


@pytest.mark.benchmark(group='tuple')
def test_positional_tuple(benchmark):
    v = SchemaValidator({'type': 'tuple', 'mode': 'positional', 'items_schema': ['int', 'int', 'int', 'int', 'int']})
    assert v.validate_python((1, 2, 3, '4', 5)) == (1, 2, 3, 4, 5)

    benchmark(v.validate_python, (1, 2, 3, '4', 5))


@pytest.mark.benchmark(group='tuple')
def test_variable_tuple(benchmark):
    v = SchemaValidator({'type': 'tuple', 'items_schema': 'int'})
    assert v.validate_python((1, 2, 3, '4', 5)) == (1, 2, 3, 4, 5)

    benchmark(v.validate_python, (1, 2, 3, '4', 5))


@pytest.mark.benchmark(group='tuple-many')
def test_tuple_many_variable(benchmark):
    v = SchemaValidator({'type': 'tuple', 'items_schema': 'int'})
    assert v.validate_python(list(range(10))) == tuple(range(10))

    benchmark(v.validate_python, list(range(10)))


@pytest.mark.benchmark(group='tuple-many')
def test_tuple_many_positional(benchmark):
    v = SchemaValidator({'type': 'tuple', 'mode': 'positional', 'items_schema': [], 'extra_schema': 'int'})
    assert v.validate_python(list(range(10))) == tuple(range(10))

    benchmark(v.validate_python, list(range(10)))


@pytest.mark.benchmark(group='arguments')
def test_arguments(benchmark):
    v = SchemaValidator(
        {
            'type': 'arguments',
            'arguments_schema': [
                {'name': 'args1', 'mode': 'positional_only', 'schema': 'int'},
                {'name': 'args2', 'mode': 'positional_only', 'schema': 'str'},
                {'name': 'a', 'mode': 'positional_or_keyword', 'schema': 'bool'},
                {'name': 'b', 'mode': 'keyword_only', 'schema': 'str'},
                {'name': 'c', 'mode': 'keyword_only', 'schema': 'int'},
            ],
        }
    )
    assert v.validate_python(((1, 'a', 'true'), {'b': 'bb', 'c': 3})) == ((1, 'a', True), {'b': 'bb', 'c': 3})

    benchmark(v.validate_python, ((1, 'a', 'true'), {'b': 'bb', 'c': 3}))
