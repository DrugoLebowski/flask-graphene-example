# Vendor
from graphene import Field, Int,List, ObjectType

# Internal
from src.types.employee import Employee as EmployeeType
from src.types.department import Department as DepartmentType
from src.models.department import Department as DepartmentModel
from src.models.employee import Employee as EmployeeModel


class Query(ObjectType):
    department = Field(DepartmentType, id=Int(required=True))
    employee = Field(EmployeeType, id=Int(required=True))
    all_departments = Field(List(DepartmentType), lower=Int(), upper=Int())
    all_employees = Field(List(EmployeeType), lower=Int(), upper=Int())

    def resolve_department(self, info, id):
        if id is None:
            raise Exception("The id is required")

        return DepartmentModel.query.get(id)

    def resolve_employee(self, info, id):
        if id is None:
            raise Exception("The id is required")

        return EmployeeModel.query.get(id)

    def resolve_all_departments(self, info, **kwargs):
        l = kwargs.get('lower')
        u = kwargs.get('uppper')
        return DepartmentModel.query.all()[l:u]

    def resolve_all_employees(self, info, **kwargs):
        l = kwargs.get('lower')
        u = kwargs.get('uppper')
        return EmployeeModel.query.all()[l:u]
