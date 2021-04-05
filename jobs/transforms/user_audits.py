# coding: utf-8
#
# Copyright 2021 The Oppia Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Beam DoFns and PTransforms to provide validation of user models."""

from __future__ import absolute_import  # pylint: disable=import-only-modules
from __future__ import unicode_literals  # pylint: disable=import-only-modules

import re

from core.platform import models
import feconf
from jobs.decorators import audit_decorators
from jobs.transforms import base_model_audits

(user_models,) = models.Registry.import_models([models.NAMES.user])


@audit_decorators.AuditsExisting(user_models.UserSettingsModel)
class ValidateUserModelId(base_model_audits.ValidateBaseModelId):
    """Overload for models keyed by a user ID, which have a special format."""

    MODEL_ID_REGEX = re.compile(feconf.USER_ID_REGEX)
