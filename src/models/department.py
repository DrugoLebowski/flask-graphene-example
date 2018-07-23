# Vendor
from sqlalchemy import Column, String

# Internal
from src.app import db
from src.models.base import BaseModelMixin


class Department(BaseModelMixin, db.Model):
    __tablename__ = "department"

    # Name of the Department
    name = Column(
        String(128),
        nullable=False
    )

    # Physical location of the Department
    location = Column(
        String(256),
        nullable=False
    )

    employees = db.relationship(
        "Employee",
        backref="department",
        lazy=True,
        cascade="all, delete, delete-orphan",
    )

    def __repr__(self) -> str:
        return "<Department %s from %s>" % (self.name, self.location)
