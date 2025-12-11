from sqlalchemy import Integer, String, TEXT, Date
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from src.comun.utilidades import db


class PokemonModelo(db.Model):
    __tablename__='pokemon'
    codigo_pokemon:Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    nombre:Mapped[str] = mapped_column(String(200),nullable=False)
    descripcion:Mapped[str] = mapped_column(TEXT,nullable=True)
    nivel:Mapped[int] = mapped_column(Integer,nullable=True, default=1)
    #MM-dd-yyyy
    fecha_creacion:Mapped[date] = mapped_column(Date,nullable=False, default=date.today)