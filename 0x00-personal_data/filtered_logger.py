#!/usr/bin/env python3

"""Filter data and obfuscation"""

import logging
from typing import List, Union
import re


def filter_datum(fields, redaction, message, separator):
    """filtering data"""
    return re.sub(f'({"|".join(fields)})=[^{separator}]+',
                  lambda m: f'{m.group(1)}={redaction}', message)
