from typing import Optional

from pydantic import BaseModel, validator


class ISBN10FormatError(Exception):
    """Custom error that is raised when ISBN10 does not have the right format"""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)


class Book(BaseModel):
    title: str
    author: str
    publisher: str
    isbn_10: Optional[str]
    isbn_13: Optional[str]

    @classmethod
    @validator
    def isbn_10_valid(cls, value):
        chars = [c for c in value if c in "0123456789Xx"]
        if len(chars) != 10:
            raise ISBN10FormatError(value=value, message="ISBN10 should be 10 digits.")

    @staticmethod
    def char_to_int(char: str) -> int:
        if char in "Xx":
            return 10
        return int(char)





