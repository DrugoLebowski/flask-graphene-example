# Vendor
from graphene_sqlalchemy import SQLAlchemyObjectType

# Internal
from src.models.department import Department as DepartmentModel


class Department(SQLAlchemyObjectType):
    """ Department type """

    class Meta:
        model = DepartmentModel
