from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

import model
import schema
from constants import ITEMS_PER_PAGE


def get_adverts(db: Session, page: int, price: bool | None, created_at: bool | None):
	offset = (page - 1) * ITEMS_PER_PAGE
	query = db.query(model.Advert)
	if price is None and created_at is None:
		return query.offset(offset).limit(ITEMS_PER_PAGE).all()
	if price is True and created_at is False:
		return query.order_by(model.Advert.price, model.Advert.created.desc()).offset(offset).limit(ITEMS_PER_PAGE).all()
	if price is True:
		return query.order_by(model.Advert.price).offset(offset).limit(ITEMS_PER_PAGE).all()
	if price is False:
		return query.order_by(model.Advert.price.desc()).offset(offset).limit(ITEMS_PER_PAGE).all()
	if created_at is True:
		return query.order_by(model.Advert.created).offset(offset).limit(ITEMS_PER_PAGE).all()
	if created_at is False:
		return query.order_by(model.Advert.created.desc()).offset(offset).limit(ITEMS_PER_PAGE).all()


def get_adverts_by_id(db: Session, adverts_id: int):
	return db.query(model.Advert).filter(model.Advert.id == adverts_id).first()


def create_adverts(db: Session, item: schema.AdvertCreateSchema):
	db_advert = model.Advert(**item.dict())
	db.add(db_advert)
	db.commit()
	db.refresh(db_advert)
	return db_advert


# def get_paginate(db: Session, page: int):
# 	offset = (page - 1) * ITEMS_PER_PAGE
# 	return db.query(model.Advert).offset(offset).limit(ITEMS_PER_PAGE).all()