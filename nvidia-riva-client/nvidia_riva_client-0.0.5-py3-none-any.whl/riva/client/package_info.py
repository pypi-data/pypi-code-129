# SPDX-FileCopyrightText: Copyright (c) 2022 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: MIT

MAJOR = 0
MINOR = 0
PATCH = 5
PRE_RELEASE = 'rc0'

# Use the following formatting: (major, minor, patch, pre-release)
VERSION = (MAJOR, MINOR, PATCH)

__shortversion__ = '.'.join(map(str, VERSION[:3]))
__version__ = '.'.join(map(str, VERSION[:3])) + ''.join(VERSION[3:])

__package_name__ = 'nvidia-riva-client'
__contact_names__ = 'Anton Peganov'
__contact_emails__ = 'apeganov@nvidia.com'
__homepage__ = 'https://github.com/nvidia-riva/python-clients'
__repository_url__ = 'https://github.com/nvidia-riva/python-clients'
__download_url__ = 'hhttps://github.com/nvidia-riva/python-clients/releases'
__description__ = "Python implementation of the Riva Client API"
__license__ = 'MIT'
__keywords__ = 'deep learning, machine learning, gpu, NLP, ASR, TTS, nvidia, speech, language, Riva, client'
__riva_version__ = "2.3.0"
__riva_release__ = "22.06"
__riva_models_version__ = "2.3.0"
