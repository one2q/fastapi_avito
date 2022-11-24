from sqlalchemy.orm import Session

import model
import schema
from constants import ITEMS_PER_PAGE


def get_adverts(db: Session, page: int, price: bool | None, created_at: bool | None):
	offset = (page - 1) * ITEMS_PER_PAGE
	order_by_price = None
	order_by_created = None

	if price is True:
		order_by_price = model.Advert.price
	if price is False:
		order_by_price = model.Advert.price.desc()
	if created_at is True:
		order_by_created = model.Advert.created
	if created_at is False:
		order_by_created = model.Advert.created.desc()

	return db.query(model.Advert).order_by(order_by_price, order_by_created).offset(offset).limit(ITEMS_PER_PAGE).all()


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