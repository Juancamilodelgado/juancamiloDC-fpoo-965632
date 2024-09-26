
# producto

# id: int 
# name: str
# price: float
# section: int

id = int(input("ingrese el id de su producto"))
name = input("por favor ingrese el nombre de su producto")
price = float(input("por favor ingrese el precio de su producto"))
section = input("por favor ingrese la setcion de su producto")

product1 = {
    "id": id,
    "name": name,
    "price": price,
    "section": section,
}

store.append(product1)

# mostrar los productos del almacen
for product1 in store:
    price(product1)