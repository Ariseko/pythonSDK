from pydantic import BaseModel, Field
from python_sdk.entities.Meta import Meta

class Product():
    meta: Meta = Field(alias="meta")

    id: str = Field(alias="id")

    accountId: str = Field(alias="accountId")

    #owner: Owner = Field(alias="owner") #создать объект Owner

    shared: bool = Field(alias="shared")

    #group: Group = Field(alias="group") #создать объект Group (там только мета)

    updated: datetime = Field(alias="updated")

    name: str = Field(alias="name")

    code: str = Field(alias="code")

    externalCode: str = Field(alias="externalCode")

    archieved: bool = Field(alias="archieved")

    pathName: str = Field(alias="pathName")

    #productFolder: ProductFolder = Field(alias="productFolder") #создать объект ProductFolder (там только мета)

    useParentVat: bool = Field(alias="useParentVat")

    #images: ImageMetaArray = Field(alias="images") #создать объект ImageMetaArray (массив мет)

    minPrice: str = Field(alias="minPrice")
