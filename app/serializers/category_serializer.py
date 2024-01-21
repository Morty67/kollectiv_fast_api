from typing import List, Optional

from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class CategoryResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class CategoryList(BaseModel):
    categories: List[CategoryResponse]

    class Config:
        orm_mode = True


class CategoryDelete(BaseModel):
    deleted: bool
    message: Optional[str] = None
