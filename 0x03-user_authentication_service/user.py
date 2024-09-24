#!/usr/bin/env python3

""" user model """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Intger, String

Base = declarative_base


class User(Base):
    """sqlalchemy model"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)

    def __repr__(self):
        """
        string
        """
        return f"<User(id={self.id}, email={self.email})>"
