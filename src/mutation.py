# Vendor
from graphene import ObjectType

# Internal
from src.mutations.department import CreateDepartment, UpdateDepartment, DeleteDepartment
from src.mutations.employee import CreateEmployee, UpdateEmployee, DeleteEmployee


class Mutations(ObjectType):
    # Department
    create_department = CreateDepartment.Field()
    update_department = UpdateDepartment.Field()
    delete_department = DeleteDepartment.Field()

    # Employee
    create_employee = CreateEmployee.Field()
    update_employee = UpdateEmployee.Field()
    delete_employee = DeleteEmployee.Field()
