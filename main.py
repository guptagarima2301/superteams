from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from recommendation import recommend_products

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/search/")
def search_products(query: str, db: Session = Depends(get_db)):
    # Add search and recommendation logic
    recommendations = recommend_products(query, db)
    return {"search_results": recommendations}
