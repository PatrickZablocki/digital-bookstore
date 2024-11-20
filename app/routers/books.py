from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Book
from app.schemas import BookCreate, Book

router = APIRouter(
    prefix="/books",  # Basis-URL für alle Buch-Endpunkte
    tags=["books"],   # Gruppierung der Endpunkte in der Dokumentation
)

# Bücher abrufen
@router.get("/")
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

# Ein Buch hinzufügen
@router.post("/")
def create_book(book: Book, db: Session = Depends(get_db)):
    # Überprüfen, ob ein Buch mit derselben ISBN existiert
    db_book = db.query(Book).filter(Book.isbn == book.isbn).first()
    if db_book:
        raise HTTPException(status_code=400, detail="Book with this ISBN already exists.")
    
    # Neues Buch speichern
    db.add(book)
    db.commit()
    db.refresh(book)
    return book
