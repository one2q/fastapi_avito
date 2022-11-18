from pydantic import BaseModel
from pydantic.dataclasses import dataclass


class AdvertBase(BaseModel):
	name: str
	price: float
	main_foto: str
	created: str


class AdvertCreate(AdvertBase):
	pass


class Config:
	orm_mode = True


@dataclass(config=Config)
class Advert(AdvertBase):
	id: int
	foto: str
	updated: str   # TODO (from pydantic.schema import datetime) возможно так правильнее datetime.datetime