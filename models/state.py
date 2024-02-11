#!/usr/bin/python3
"""State Module"""
form models.base_model import BaseModel


class State(BaseModel):
    """A class to indicate the state name
    Attributes:
    name (str): the state name
    """
    name = ""
