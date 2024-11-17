from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite-Datenbank in der Datei 'sqlite:///./test.db' speichern
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Engine erstellen, die mit der SQLite-Datenbank arbeitet
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Basisklasse für unsere Modelle
Base = declarative_base()

# Session Local für den Datenbankzugriff
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
