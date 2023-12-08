from pydantic import BaseModel, Field

class Meta():
    href: str = Field(alias="href")

    type: str = Field(alias="type")

    mediaType: str = Field(alias="mediaType")

    size: int = Field(alias="size")

    limit: int = Field(alias="limit")

    offset: int = Field(alias="offset")

    nextHref: str = Field(alias="nextHref")

    previousHref: str = Field(alias="previousHref")

    metadataHref: str = Field(alias="metadataHref")

    uuidHref: str = Field(alias="uuidHref")

    downloadHref: str = Field(alias="downloadHref")