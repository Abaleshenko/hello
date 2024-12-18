
def max_price(item):
    return max(item, key=item.get)

products = {
    'apple': 165.7,
    'mango': 62.5,
    'cherry': 89.5
}

print(max_price(products))