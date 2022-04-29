# from faker import Faker


# class PlayerLocalization:
#     def __init__(self, lang) -> None:
#         self.fake =Faker(lang)
#         self.result = {
#             "nikname":self.fake.first_name()
#         }

#     def build(self):
#         return self.result

# """{'local': {'eng': {'nikname': 'Nancy'},
#             'ru': {'nikname': 'Милица'}},
#             'balbnce': 300,
#             'account_status': 'blabla'}"""
# class Player:

#     def __init__(self) -> None:
#         self.result = {
#             "local":{
#                 "eng":PlayerLocalization('en_US').build(),
#                 "ru":PlayerLocalization('ru_RU').build()
#             }
#         }

#     def set_status(self, status:str = 'Active'):
#         self.result ["account_status"] = status
#         return self


#     def set_balance(self, balance:int):
#         self.result["balbnce"] = balance
#         return self

#     def build(self) -> dict:
#         return self.result


# a = Player()

# c = a.set_balance(100).set_status('blabla').set_balance(300).build()
# print(c)


# a = {'a': 1, 'b': 2, 'c': {'d': 1}}


# def update_inner_value(this_dict: dict, key_elem, value) -> dict:
#     if not isinstance(key_elem, list):
#         this_dict[key_elem] = value
#     else:
#         for item in key_elem[:-1]:
#             if item not in this_dict.keys():
#                 this_dict[item] = {}
#             else:
#                 this_dict = this_dict[item]
#         this_dict[key_elem[-1]] = value


# new_dict = update_inner_value(a, ['c', 'd',], 1111)
# print(a.keys())
# print(a)

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
