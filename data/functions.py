def priskoll(age):
    age = int(age)
    if age in range(18,65):
        return 20
    elif age in range(0,131):
        return 15
    else:
        return "err"