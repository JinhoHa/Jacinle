#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# File   : __init__.py
# Author : Jiayuan Mao
# Email  : maojiayuan@gmail.com
# Date   : 03/09/2020
#
# This file is part of NSCL-PyTorch.
# Distributed under terms of the MIT license.


from .collate_v1 import VarLengthCollateV1
from .collate_v2 import VarLengthCollateV2
from .collate_v3 import VarLengthCollateV3
from .utils import user_scattered_collate, VarLengthCollateMode

VarLengthCollate = VarLengthCollateV1
