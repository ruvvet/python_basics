def add(a, b):

    return a+b


def subtract(a, b):

    return a-b


def random(arr):

    return [x for x in arr if x > 5]


print(add(5, 10))
print(subtract(5, 3))
print(random([5, 4, 3, 6, 8, 9, 4, 1, 2, 4, 6]))
