try:
    result = []
    def divider(a, b):
        if a < b:
            return a*b
        if b > 100:
            raise IndexError
        return a/b
    data = {10: 2, 2: 5, 123: 4, 18: 1, 1: 15, 8 : 4}

    for key in data:
        res = divider(key, data[key])
        result.append(res)
    print(result)
except NameError:
    print("We have a deal with a name error")
except SyntaxError:
    print("We have a deal with a syntax error")
except TypeError:
    print("We have a deal with a type error")




