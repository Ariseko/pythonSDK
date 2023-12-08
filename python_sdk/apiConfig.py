import os

from typing import Optional, Union
from pydantic import BaseModel

class APIConfig():
    base_path: str = "https://api.moysklad.ru/api/remap/1.2"
    verify: Union[bool, str] = True

    def get_access_token(self) -> Optional[str]:
        return 'TOKEN'

    def set_access_token(self, value: str):
        raise Exception(
            "This client was generated with an environment variable for the access token. Please set the environment variable 'access_token' to the access token."
        )

class HTTPException(Exception):
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"{status_code} {message}")

    def __str__(self):
        return f"{self.status_code} {self.message}"


