from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Category(Base):
    __tablename__ = 'categorys'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    notes = relationship('Note', back_populates='category')

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('categorys.id', ondelete='CASCADE'), nullable=False)

    category = relationship('Category', back_populates='notes')
