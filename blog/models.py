from db import Base
from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = 'blog_posts'

    id = Column(Integer, primary_key=True, unique=True, index=True)
    user = Column(Integer, ForeignKey('users.id'))
    users_id = relationship('User')
    title = Column(String)
    text = Column(Text)
    date = Column(DateTime)
