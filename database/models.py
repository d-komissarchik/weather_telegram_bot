from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(30), nullable=False)
    author = Column(String(30), nullable=False)
    reviews = relationship('Reviews', backref='book', lazy=True)

    def __repr__(self):
        return self.title


class Reviews(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    text = Column(String(2000), nullable=False)
    book_id = Column(Integer, ForeignKey('book.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'Вiд {self.reviewer}'


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    reviews = relationship('Reviews', backref='reviewer', lazy=True)

    def __repr__(self):
        return self.name


engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres', echo=True)

Base.metadata.create_all(engine)
