#!/usr/bin/env python3

"""Filter data and obfuscation"""

import logging
from typing import List, Union
import re


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """filter data"""
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}',
                         f'{f}={redaction}{separator}', message)
        return message
