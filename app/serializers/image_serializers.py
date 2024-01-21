from pydantic import BaseModel


class ImageCreate(BaseModel):
    name: str


class ImageResponse(BaseModel):
    id: int
    name: str
