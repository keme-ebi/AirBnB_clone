#!/usr/bin/python3
"""module with Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Inherits from BaseModel class"""
    place_id = ""
    user_id = ""
    text = ""
