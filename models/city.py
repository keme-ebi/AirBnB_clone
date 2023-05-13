#!/usr/bin/python3
"""module with a class City"""

from models.base_model import BaseModel


class City(BaseModel):
    """Inherits from BaseModel class"""
    state_id = ""
    name = ""
