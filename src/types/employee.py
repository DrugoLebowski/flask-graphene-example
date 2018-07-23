# Vendor
from graphene import Int
from graphene_sqlalchemy import SQLAlchemyObjectType

# Internal
from src.models.employee import Employee as EmployeeModel


class Employee(SQLAlchemyObjectType):
    """ Employee type. """

    class Meta:
        model = EmployeeModel

    id = Int()
