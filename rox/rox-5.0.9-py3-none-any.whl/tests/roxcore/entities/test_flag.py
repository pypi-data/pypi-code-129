import unittest

from rox.core.entities.flag import Flag
from rox.core.roxx.evaluation_result import EvaluationResult
from rox.core.configuration.models.experiment_model import ExperimentModel

try:
    from unittest.mock import Mock
except ImportError:
    from mock import Mock

class FlagTests(unittest.TestCase):
    def test_flag_without_default_value(self):
        flag = Flag()
        self.assertFalse(flag.is_enabled(None))

    def test_flag_with_default_value(self):
        flag = Flag(True)
        self.assertTrue(flag.is_enabled(None))

    def test_will_return_value_when_on_evaluation_boolean(self):
        parser = Mock()
        parser.evaluate_expression.return_value = EvaluationResult(True) # Returning a boolean here.

        flag = Flag(False)
        flag.set_for_evaluation(parser, None, ExperimentModel('id', 'name', '123', False, [1.0], set(), 'stam'))

        self.assertTrue(flag.is_enabled(None))

    def test_will_return_value_when_on_evaluation_string(self):
        parser = Mock()
        parser.evaluate_expression.return_value = EvaluationResult('true') # As above, but returning boolean-as-string.

        flag = Flag(False)
        flag.set_for_evaluation(parser, None, ExperimentModel('id', 'name', '123', False, [1.0], set(), 'stam'))

        self.assertTrue(flag.is_enabled(None))

    def test_will_invoke_enabled_action(self):
        flag = Flag(True)
        is_called = {'called': False}

        def action():
            is_called['called'] = True

        flag.enabled(None, action)

        self.assertTrue(is_called['called'])

    def test_will_invoke_disabled_action(self):
        flag = Flag()
        is_called = {'called': False}

        def action():
            is_called['called'] = True

        flag.disabled(None, action)

        self.assertTrue(is_called['called'])

    def test_should_return_flag_default_when_flag_dependency_does_not_exist(self):
        flag = Flag(True)
        flag.condition = 'flagValue("fff")'
        flag.parser = Mock()
        self.assertTrue(flag.is_enabled())
