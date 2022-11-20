from sqlalchemy import Column, DateTime, func, Integer, String, Float

from db import Base


class Advert(Base):
    __tablename__ = 'advert'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False)
    price = Column(Float, nullable=False)
    main_foto = Column(String, nullable=False)
    describe = Column(String(1000))
    foto = Column(String)
    created = Column(DateTime, nullable=False, default=func.now())
    updated = Column(DateTime, default=func.now(), onupdate=func.now())