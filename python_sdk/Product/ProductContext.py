from pydantic import BaseModel, Field

class ProductContext(BaseModel):
    href: str = Field(alias="href")


class Employee(BaseModel):
    pass
