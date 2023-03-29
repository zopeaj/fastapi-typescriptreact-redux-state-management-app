from sqlalchemy import Column, String, Integer, Sequence
from app.app.db.base_class import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, Sequence("user_seq_id"), primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
