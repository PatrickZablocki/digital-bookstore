from sqlalchemy import Column, Integer, String
from app.database import Base

# Das 'Book'-Modell definiert die Struktur einer Tabelle in der Datenbank, die Bücher speichert.
class Book(Base):

    __tablename__ = "books" # Der Name der Tabelle in der Datenbank, die mit diesem Modell verbunden ist
    # Die einzelnen Spalten der 'books'-Tabelle werden hier definiert
    id = Column(Integer, primary_key=True,index=True)
    title = Column(String, index=True)
    author = Column(String)
    isbn = Column(String, unique=True)
    year_published = Column(Integer)
    genre = Column(String)

# Definiert das 'User'-Modell, das Informationen über Benutzer speichert
class User(Base):
    __tablename__ = "users"  # Der Name der Tabelle in der Datenbank

    id = Column(Integer, primary_key=True, index=True) # 'id' ist der Primärschlüssel
    username = Column (String, unique=True, index=True) # Der Benutzername des Benutzers (muss einzigartig sein)
    password = Column(String) # Das Passwort des Benutzers (muss in einer echten Anwendung gehasht werden)