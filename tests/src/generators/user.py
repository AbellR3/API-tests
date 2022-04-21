from faker import Faker



class PlayerLocalization:
    def __init__(self, lang) -> None:
        self.fake =Faker(lang)
        self.result = {
            "nikname":self.fake.first_name()
        }

    def build(self):
        return self.result


class Player:

    def __init__(self) -> None:
        self.result = {
            "local":{
                "eng":PlayerLocalization('en_US').build(),
                "ru":PlayerLocalization('ru_RU').build()
            }
        }

    def set_status(self, status:str = 'Active'):
        self.result ["account:status"] = status
        return self

    
    def set_balance(self, balance:int):
        self.result["balbnce"] = balance
        return self

    def build(self) -> dict:
        return self.result


a = Player()

c = a.set_balance(100).set_status('blabla').set_balance()
print(c)

