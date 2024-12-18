# def subtrack(a, b):
#     return a - b
#
#
# print(subtrack(12, 8))
# print(type(subtrack))

MILE = 1.852

def compass(distance, mode):
    modify = {
        'km': distance * MILE
    }
    return modify[mode]


print(compass(256, 'km'))