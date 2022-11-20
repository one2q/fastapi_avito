from fastapi import Depends, FastAPI, Request, Response, APIRouter
from sqlalchemy.orm import Session

import crud, model, schema
from db import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
	response = Response("Internal server error", status_code=500)
	try:
		request.state.db = SessionLocal()
		response = await call_next(request)
	finally:
		request.state.db.close()
	return response


# Dependency
# TODO попробовать сделать чз with
def get_db(request: Request):
	return request.state.db

# def get_db():
# 	db = SessionLocal()
# 	try:
# 		yield db
# 	finally:
# 		db.close()


@app.get('/adverts/', response_model=list[schema.AdvertListSchema])
def get_adverts(db: Session = Depends(get_db)):
	result = crud.get_adverts(db)
	return result


@app.get('/adverts/{adverts_id}', response_model=schema.AdvertListSchema)
def get_adverts_by_id(db: Session = Depends(get_db), adverts_id: int = schema.AdvertListSchema):
	return crud.get_adverts_by_id(db, adverts_id)


@app.post('/adverts/', response_model=schema.AdvertListSchema)
def create_advert(advert: schema.AdvertCreateSchema, db: Session = Depends(get_db)):
	return crud.create_adverts(db=db, item=advert)
