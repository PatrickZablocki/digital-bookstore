from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    isbn: str
    year_published: int
    genre: str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
