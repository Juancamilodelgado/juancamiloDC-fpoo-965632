# ------------------

# person

# dni: int
# name: str
# lastname: int
# role: int

# --------------------


class Person:
    def __init__(self,dni: int, name: str, lastname: str, role: int):
        self.dni = dni
        self.name = name 
        self.lastname = lastname
        self.role = role 

    def __repr__(self):
        return f"dni={self.dni} {self.name} {self.lastname} {self.role}"
    # def __repr__(self):
    #     return"dni={}".format(self.dni)

Person1 = Person(dni=123, name="luisito",lastname="velez", role=1)
Person2 = Person(dni=164, name="juan",lastname="caballos", role=2)
Person3 = Person(dni=321, name="ana",lastname="vazques", role=3)
Person3 = Person(dni=423, name="carloz",lastname="yuuy", role=4)

print(Person1,Person2,Person3)

