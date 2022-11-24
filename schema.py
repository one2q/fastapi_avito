from pydantic import BaseModel, HttpUrl


class AdvertBaseSchema(BaseModel):
	name: str
	price: float
	main_foto: str

	class Config:
		orm_mode = True


class AdvertCreateSchema(AdvertBaseSchema):
	describe: str | None
	foto: str | None


class AdvertSchema(AdvertBaseSchema):
	id: int


class AdvertFullSchema(AdvertBaseSchema):
	id: int
	describe: str | None
	foto: str | None


# updated: datetime
# created: datetime