from sqlalchemy.orm import Session

import model
import schema


def get_adverts(db: Session):
	return db.query(model.Advert).all()


def create_adverts(db: Session, advert: schema.AdvertCreate):
	db_advert = model.Advert(name=advert.name, price=advert.price, main_foto=advert.main_foto)
	db.add(db_advert)
	db.commit()
	return db_advert.id