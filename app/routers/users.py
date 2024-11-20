from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

# Benutzer abrufen
@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()

# Benutzer registrieren
@router.post("/")
def create_user(user: User, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists.")
    
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
