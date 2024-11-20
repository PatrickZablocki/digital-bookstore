from fastapi import FastAPI
from app.database import engine
from app import models
from app.routers import books
from app.routers import users

# Tabellen erstellen
# Diese Zeile erstellt die Tabellen in der Datenbank, falls sie noch nicht existieren.
# Es wird geprüft, ob die Tabellen in der Datenbank existieren und falls nicht, werden sie basierend auf den Modellen erstellt.
models.Base.metadata.create_all(bind=engine)
# Erstellen einer FastAPI-Instanz, die die Grundlage für die API darstellt.
app = FastAPI()

# Router einbinden
app.include_router(books.router)

app.include_router(users.router)

# Definiert den Root-Endpunkt der API, der mit einem GET-Request angesprochen wird.
@app.get("/")

def read_root():
    # Gibt eine einfache Nachricht zurück, wenn der Root-Endpunkt aufgerufen wird.
    return {"message":"Welcome to the digitale bookstore API"}