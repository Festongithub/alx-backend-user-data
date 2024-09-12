#!/usr/bin/env python3

"""Filter data and obfuscation"""

import logging
from typing import List, Union
import re


def filter_datum(fields: List[str], redaction: str, message: str, separator: str):
