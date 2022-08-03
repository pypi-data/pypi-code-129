import pytest

from shapely.geometry import shape, Polygon, MultiLineString
from shapely.geometry.geo import _is_coordinates_empty


@pytest.mark.parametrize(
    "geom",
    [{"type": "Polygon", "coordinates": None}, {"type": "Polygon", "coordinates": []}],
)
def test_polygon_no_coords(geom):
    assert shape(geom) == Polygon()


def test_polygon_empty_np_array():
    np = pytest.importorskip("numpy")
    geom = {"type": "Polygon", "coordinates": np.array([])}
    assert shape(geom) == Polygon()


def test_polygon_with_coords_list():
    geom = {"type": "Polygon", "coordinates": [[[5, 10], [10, 10], [10, 5]]]}
    obj = shape(geom)
    assert obj == Polygon([(5, 10), (10, 10), (10, 5)])


def test_polygon_not_empty_np_array():
    np = pytest.importorskip("numpy")
    geom = {"type": "Polygon", "coordinates": np.array([[[5, 10], [10, 10], [10, 5]]])}
    obj = shape(geom)
    assert obj == Polygon([(5, 10), (10, 10), (10, 5)])


@pytest.mark.parametrize("geom", [
    {'type': "MultiLineString", "coordinates": []},
    {'type': 'MultiLineString', 'coordinates': [[]]},
    {'type': 'MultiLineString', 'coordinates': None}
])
def test_multilinestring_empty(geom):
    assert shape(geom) == MultiLineString()


@pytest.mark.parametrize("coords", [
    [],
    [[]],
    [[], []],
    None,
    [[[]]]
])
def test_is_coordinates_empty(coords):
    assert _is_coordinates_empty(coords)
