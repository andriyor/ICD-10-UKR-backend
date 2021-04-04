from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, backref

from .database import Base


class Code(Base):
    __tablename__ = "code"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String)
    descriptionUA = Column(String)
    hasChild = Column(Boolean, nullable=True)
    descriptionENG = Column(String, nullable=True)
    parent_id = Column(Integer, ForeignKey('code.id'), nullable=True)
    child = relationship("Code",
                         backref=backref('parent', remote_side=[id])
                         )
