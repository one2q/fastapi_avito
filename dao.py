from sqlalchemy.orm import Session
# TODO научится делать запросы через классы
from model import Advert


class AdvertDAO:

	def __init__(self, db):
		self.db = db

	def get_all(self):
		print('-'*15, self.db)
		return self.session.query(Advert).all()