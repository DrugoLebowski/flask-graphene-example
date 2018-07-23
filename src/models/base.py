# Standard
from datetime import datetime

# Vendor
from sqlalchemy import Column, Integer, DateTime

# Internal
from src.app import db


class BaseModelMixin(object):
    """ Base model. Must be extended. """

    id = Column(
        Integer,
        nullable=False,
        primary_key=True,
        autoincrement=True,
    )

    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow(),
    )

    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow(),
        onupdate=datetime.utcnow(),
    )
