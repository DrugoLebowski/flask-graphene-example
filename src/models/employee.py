# Vendor
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# Internal
from src.app import db
from src.models.base import BaseModelMixin


class Employee(BaseModelMixin, db.Model):
    __tablename__ = "employee"

    # Legal employee name
    name = Column(
        String(128),
        nullable=False,
    )

    # Legal employee surname
    surname = Column(
        String(128),
        nullable=False,
    )

    department_id = Column(
        Integer(),
        ForeignKey("department.id"),
        nullable=False,
    )

    def __repr__(self) -> str:
        return "<Employee %s %s of Department: %s>" % (self.name, self.surname, self.department.name)
