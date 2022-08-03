# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator 2.3.33.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class LimitSettings(Model):
    """LimitSettings.

    :param max_trials:
    :type max_trials: int
    :param trial_timeout:
    :type trial_timeout: str
    :param job_timeout:
    :type job_timeout: str
    :param max_concurrent_trials:
    :type max_concurrent_trials: int
    :param max_cores_per_trial:
    :type max_cores_per_trial: int
    :param job_exit_score:
    :type job_exit_score: float
    :param enable_early_termination:
    :type enable_early_termination: bool
    """

    _attribute_map = {
        'max_trials': {'key': 'maxTrials', 'type': 'int'},
        'trial_timeout': {'key': 'trialTimeout', 'type': 'str'},
        'job_timeout': {'key': 'jobTimeout', 'type': 'str'},
        'max_concurrent_trials': {'key': 'maxConcurrentTrials', 'type': 'int'},
        'max_cores_per_trial': {'key': 'maxCoresPerTrial', 'type': 'int'},
        'job_exit_score': {'key': 'jobExitScore', 'type': 'float'},
        'enable_early_termination': {'key': 'enableEarlyTermination', 'type': 'bool'},
    }

    def __init__(self, max_trials=None, trial_timeout=None, job_timeout=None, max_concurrent_trials=None, max_cores_per_trial=None, job_exit_score=None, enable_early_termination=None):
        super(LimitSettings, self).__init__()
        self.max_trials = max_trials
        self.trial_timeout = trial_timeout
        self.job_timeout = job_timeout
        self.max_concurrent_trials = max_concurrent_trials
        self.max_cores_per_trial = max_cores_per_trial
        self.job_exit_score = job_exit_score
        self.enable_early_termination = enable_early_termination
