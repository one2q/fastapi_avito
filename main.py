from fastapi import Depends, FastAPI, Request, Response, APIRouter
from sqlalchemy.orm import Session

import crud, model, schema
from db import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


# TODO почитать про это и разобраться
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


@app.get('/adverts/', response_model=list[schema.AdvertSchema])
def get_adverts(db: Session = Depends(get_db), page: int = 1,
                price: bool | None = None, created_at: bool | None = None):
	result = crud.get_adverts(db, page, price, created_at)
	return result


@app.get('/adverts/{adverts_id}', response_model=schema.AdvertSchema)
def get_adverts_by_id(db: Session = Depends(get_db), adverts_id: int = schema.AdvertSchema):
	return crud.get_adverts_by_id(db, adverts_id)


@app.post('/adverts/', status_code=201)
def create_advert(advert: schema.AdvertCreateSchema, db: Session = Depends(get_db)):
	new_advert = crud.create_adverts(db=db, item=advert)
	return {'advert_id': new_advert.id}
