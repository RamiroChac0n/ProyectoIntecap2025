from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from src.comun.utilidades import db


class TipoModelo(db.Model):
    __tablename__='tipo'
    codigo_tipo:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    nombre:Mapped[str] = mapped_column(String(100),nullable=False)