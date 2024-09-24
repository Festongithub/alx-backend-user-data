#!/usr/bin/env python3
""" Hash password """

import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from typing import Union
from user import User
from uuid import uuid4


def _hash_password(password: str) -> str:
    new_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return new_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        __summary__
        Return: User creds
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(email, hashed_password)

            return user
        else:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """
        Tries to locate the user by email
        """
        try:
            user = self._db.find_user(email=email)
        except NoResultFound:
            return False
        user_pass = user.hashed_password
        encoded_pass = password.encode()

        if bcrypt.checkpw(encoded_pass, user_pass):
            return True
        return False
