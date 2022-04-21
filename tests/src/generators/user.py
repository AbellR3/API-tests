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


a = {'a': 1, 'b': 2, 'c': {'d': 1}}


def update_inner_value(this_dict: dict, key_elem, value) -> dict:
    if not isinstance(key_elem, list):
        this_dict[key_elem] = value
    else:
        for item in key_elem[:-1]:
            if item not in this_dict.keys():
                this_dict[item] = {}
            this_dict = this_dict[item]
        this_dict[key_elem[-1]] = value


new_dict = update_inner_value(a, ['c', 'd', 'q'], 222)
print(a)


class Tools:
    def __init__(self, result) -> None:
        self.result = result

    def update_inner_value(self, keys, value):
        if not isinstance(keys, list):
            self.result[keys] = value
        else:
            temp = self.result
            for item in keys[:-1]:
                if item not in temp.keys():
                    temp[item] = {}
                temp = temp[item]
            temp[keys[-1]] = value
        return self