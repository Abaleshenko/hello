# def area(a, b):
#     return a * b
#
#
# print(f"Area: {area(12, 8)}")
# print(f"Area: {area(5, 10)}")
from cgitb import reset


# def cinema(language: str = 'ua') -> str:
#     return f"Мова: {language}"
#
#
# print(cinema())
#
#
#
# def to_cart(product, quantity=1):
#     return f"{product} у кількості: {quantity}"
#
# print(to_cart('lemon'))


def type_of_args(*args, **kwargs):
    global result
    result = {
        'position': args,
        'keyword': kwargs
    }
    return result



print(type_of_args(2, 5, -8, 12, film='Harry Potter', ocean='Atlantic'))
print(result)