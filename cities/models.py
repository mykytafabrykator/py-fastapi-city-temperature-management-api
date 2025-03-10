from sqlalchemy import String
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)

from temperature.models import Temperature


class Base(DeclarativeBase):
    pass


class City(Base):
    __tablename__ = "city"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    additional_info: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    temperatures: Mapped[list["Temperature"]] = relationship(
        "Temperature",
        back_populates="city",
        cascade="all, delete",
        passive_deletes=True
    )
