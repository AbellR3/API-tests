from pydantic import BaseModel, EmailStr, Field, validator



class Profile(BaseModel):
    id: int
    employeeId: int
    email: EmailStr
    isDefaultPassword: bool
