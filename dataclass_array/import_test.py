# Copyright 2022 The dataclass_array Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for import.

Import should work even if the lazy deps are not present.

"""

from __future__ import annotations

import sys

import dataclass_array as dca
from etils import enp


class A(dca.DataclassArray):
  x: dca.typing.f32['*s']


def test_lazy():

  x = A(x=[1.0, 2.0])
  assert x.xnp is enp.lazy.np
