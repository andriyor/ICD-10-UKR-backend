from typing import Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    code: str
    descriptionUA: str
    descriptionENG: Optional[str] = None
    parent_id: Optional[str] = None
    hasChild: Optional[bool] = None


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True