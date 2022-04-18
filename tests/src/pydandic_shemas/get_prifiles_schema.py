from pydantic import BaseModel, validator


class Profile(BaseModel):
    id: int
    employeeId: int
    email: bool
    isDefaultPassword: bool
