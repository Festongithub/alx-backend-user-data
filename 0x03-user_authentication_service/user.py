#!/usr/bin/env python3

""" user model """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Intger, String

Base = declarative_base

class User(Base):
    """sqlalchemy model"""
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    hashed_password = Column(String)
    session_id = Column(String)
    reset_token = Column(String)


