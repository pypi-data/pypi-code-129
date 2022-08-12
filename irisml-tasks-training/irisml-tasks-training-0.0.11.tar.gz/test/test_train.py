import unittest
import torch
from irisml.tasks.train.build_optimizer import OptimizerFactory


class TestBuildOptimizer(unittest.TestCase):
    def test_create(self):
        self._check_build_optimizer('sgd', 0.001)
        self._check_build_optimizer('adam', 0.001)
        self._check_build_optimizer('amsgrad', 0.001)
        self._check_build_optimizer('adamw', 0.001)
        self._check_build_optimizer('adamw_amsgrad', 0.001)
        self._check_build_optimizer('rmsprop', 0.001)

    def _check_build_optimizer(self, *args):
        module = torch.nn.Conv2d(3, 3, 3)
        factory = OptimizerFactory(*args)
        optimizer = factory(module.parameters())
        self.assertIsInstance(optimizer, torch.optim.Optimizer)
