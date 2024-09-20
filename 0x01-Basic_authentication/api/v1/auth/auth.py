#!/usr/bin/python3

"""implement auth class"""

from flask import request
from typing import List, TypeVar


class Auth:
    """class implement authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        auth __summary__
        """

        if path is None:
            return True

        if not excluded_paths is None or excluded_paths == []:
            return True

        if path in excluded_paths:
            return False

        for excluded_path in excluded_paths:
            if excluded_path.startswith(path):
                return False

        return False

    def authorization_header(self, request=None) -> str:
        """
        Returns none
        """
        if request is None:
            return None

        header = request.headers.get('Authorization')

        if header is None:
            return None

        return header


    def current_user(self, request=None) -> TypeVar('User'):
        """
        return __summary__ of current user
        """
        return None
