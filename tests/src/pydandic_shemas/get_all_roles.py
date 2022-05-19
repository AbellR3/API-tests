from pydantic import BaseModel, EmailStr, Field, validator


class AllRoles(BaseModel):
    salaryService:str
    permissions:list[str]



{
  "salaryService": "Сервис полезных контактов",
  "permissions": [
    "CREATE_DELETE_CONTACT",
    "GET_CATEGORY"
  ]
}