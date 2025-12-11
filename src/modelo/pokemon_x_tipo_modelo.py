

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.comun.utilidades import db



class PokemonXTipoModelo(db.Model):
    __tablename__='pokemon_x_tipo'
    codigo_pokemon:Mapped[int] = mapped_column(Integer,ForeignKey('pokemon.codigo_pokemon'),primary_key=True)
    codigo_tipo:Mapped[int] = mapped_column(Integer,ForeignKey('tipo.codigo_tipo'),primary_key=True)