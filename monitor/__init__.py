# Copyright 2020 Fu Hanxi

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

import logging
import os
import re
import sys
from typing import Dict, List, Pattern, Tuple

from ruamel import yaml

PROJ_DIR = os.path.join(os.path.dirname(__file__), '..')

# logging related
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


# YAML config
def _parse_re_list(keyword_dict: Dict[str, str]) -> List[Tuple[str, Pattern]]:
    res = []
    for keyword, word in keyword_dict.items():
        res.append((keyword, re.compile(word)))
    return res


default_path = os.path.join(PROJ_DIR, '.monitor.yml')
MONITOR_CFG = yaml.safe_load(open(default_path))
KEYWORD_REGEX = _parse_re_list(MONITOR_CFG['keywords'])
