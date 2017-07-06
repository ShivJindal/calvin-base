# -*- coding: utf-8 -*-

# Copyright (c) 2017 Ericsson AB
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

from calvin.utilities import calvinlogger

_log = calvinlogger.get_logger(__name__)

class BaseCalvinlibObject(object):

    def __init__(self, calvinlib, name):
        super(BaseCalvinlibObject, self).__init__()
        self.calvinlib = calvinlib
        self.name = name

    def init(self, **kwargs):
        """
        Init object

        Args:
            **kwargs: Key word init arguments
        """
        raise NotImplementedError()

    def dispose(self):
        """
        Dispose of object
        """
        # Usually nothing to do here
        pass
