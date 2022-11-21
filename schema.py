from datetime import datetime

from pydantic import BaseModel, datetime_parse


class AdvertBaseSchema(BaseModel):
	name: str
	price: float
	main_foto: str
	describe: str | None
	foto: str | None
	updated: datetime
	created: datetime

	class Config:
		orm_mode = True


class AdvertCreateSchema(AdvertBaseSchema):
	pass


class AdvertSchema(AdvertBaseSchema):
	id: int


class AdvertListSchema(AdvertSchema):
	pass

