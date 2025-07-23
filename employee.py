from pydantic import BaseModel


class Employee(BaseModel):
  name:str
  role:str
  years_of_experience:int

employee=Employee(name="Patrick",role="Senior Technical lead",years_of_experience="5")
print(employee)