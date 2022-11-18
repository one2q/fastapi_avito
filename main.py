from fastapi import Depends, FastAPI, HTTPException, Request, Response
from sqlalchemy.orm import Session

import crud, model, schema
from db import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
# TODO попробовать сделать чз with
def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()


@app.get('/adverts/', response_model=schema.Advert)
def get_adverts(db: Session = Depends(get_db)):
	return crud.get_adverts(db)


@app.post('/adverts/', response_model=schema.Advert)
def create_advert(advert: schema.AdvertCreate, db: Session = Depends(get_db)):
	return crud.create_adverts(db=db, advert=advert)
