import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    ID = Column(Integer, primary_key=True)
    userID = Column(String(250))
    userName = Column(String(250))
    firstName = Column(String(250))
    lastName = Column(String(250))
    email = Column(String(250))

class Follower(Base):
    __tablename__ = 'Follower'
    ID = Column(Integer, primary_key=True)
    userID = Column(Integer, ForeignKey('User.ID'))
    userToId = Column(Integer, ForeignKey('User.ID'))
    user = relationship('User', foreign_keys=[userID])
    user_to = relationship('User', foreign_keys=[userToId])

class Post(Base):
    __tablename__ = 'Post'
    ID = Column(Integer, primary_key=True)
    userID = Column(Integer, ForeignKey('User.ID'))
    user = relationship('User')

class Comment(Base):
    __tablename__ = 'Comment'
    ID = Column(Integer, primary_key=True)
    commentText = Column(String(250))
    authorID = Column(Integer, ForeignKey('User.ID'))
    postID = Column(Integer, ForeignKey('Post.ID'))
    author = relationship('User')
    post = relationship('Post')

class Media(Base):
    __tablename__ = 'Media'
    ID = Column(Integer, primary_key=True)
    type = Column(String(250))
    url = Column(String(250))
    postID = Column(Integer, ForeignKey('Post.ID'))
    post = relationship('Post')


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
