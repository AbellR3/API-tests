from enum import Enum
from pydantic import BaseModel, Field, validator



class ClassType(Enum):
    Math = 'Math'
    Filosofi = 'Filosofi'





class Validate_student_class(BaseModel):
    type: ClassType = Field(alias='type')
    num_class: int = Field(alias='num-class', ge=1, le=11,)


class Validate_student_schema(BaseModel):
    id: int
    name: str
    surname: str
    birthday: str
    student_class: Validate_student_class = Field(alias='student-class')

schema = {'id': 111,
          'name': 'Vania',
          'surname': 'Vanin',
          'birthday': '30.01.2011',
          'student-class': {
              'type': 'Math',
              'num-class': 4
            }
          }

Validate_student_schema.parse_obj(schema)


# import requests

# resp = requests.request('GET', 'https://google.ru')
# assert resp.status_code == 200, ''
# print(resp.json())


# def run_action(user_make: list) -> None:
#     match user_make:
#         case action, value:
#             print(f'in action {action}, in value {value}')

#         case action, value, third:
#             print(f'in action {action}, in value {value}, third is {third}')

#         case 'this', *action:
#             print(f'This action is {action}')
#         case _:
#             print('Not correct')


# run_action('blabla vakue-blabla tree'.split())
# run_action('this blabla vakue-blabla tree, asdasd, dasdasd,asdasd,asd'.split())


# class UserData:
#     def __init__(self, action: str, value: str) -> None:
#         self.action = action
#         self.value = value


# def run_h(user_input: UserData | dict) -> None:
#     match user_input:
#         case UserData(action="left" | "right", value=value):
#             print('this is our class')
#         case 'left' | 'right', value:
#             print('this is our dict')
#         case _:
#             print('this is not our class or dict')


# in1 = UserData('left', 'vals')

# int4 = ['left', 'vals']
# int22 = 'aa sss'

# run_h(in1)
# run_h(int4)

# run_h(int22)
