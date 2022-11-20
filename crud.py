from sqlalchemy.orm import Session

import model
import schema


def get_adverts(db: Session):
	return db.query(model.Advert).all()


def get_adverts_by_id(db: Session, adverts_id: int):
	return db.query(model.Advert).filter(model.Advert.id == adverts_id).first()


def create_adverts(db: Session, item: schema.AdvertCreateSchema):
	db_advert = model.Advert(**item.dict())
	db.add(db_advert)
	db.commit()
	db.refresh(db_advert)
	return db_advert.id