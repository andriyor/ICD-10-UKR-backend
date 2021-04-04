from typing import Optional

from sqlalchemy.orm import Session

from . import models


def get_code(db: Session, code_id: int):
    return db.query(models.Code).filter(models.Code.id == code_id).first()


def get_codes(db: Session, skip: int = 0, limit: int = 100, parent: Optional[int] = None, search: Optional[str] = None):
    codes = db.query(models.Code)
    if search:
        codes = codes.filter(models.Code.descriptionUA.like('%{0}%'.format(search)))
    return codes.filter(models.Code.parent_id == parent).offset(skip).limit(limit).all()
