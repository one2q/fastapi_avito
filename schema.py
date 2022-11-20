from datetime import datetime

from pydantic import BaseModel


class AdvertBaseSchema(BaseModel):
	name: str
	price: float
	main_foto: str
	describe: str | None
	foto: str | None
	updated: datetime | None
	created: datetime | None

	class Config:
		orm_mode = True


class AdvertCreateSchema(AdvertBaseSchema):
	pass


class AdvertListSchema(AdvertBaseSchema):
	id: int

