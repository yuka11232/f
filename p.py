result = []

def divider(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("arg must be int or float")
    if a < b:
        raise ValueError("first arg must be greater than second")
    if b > 100:
        raise IndexError("second arg must be less than 100")
    if b == 0:
        raise ZeroDivisionError("error, division by zero")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}

for key, value in data.items():
    try:
        res = divider(key, value)
    except (ZeroDivisionError, TypeError, ValueError, IndexError) as e:
        print(f"error: {e}")
    else:
        result.append(res)
    finally:
        print(f"pair processing  ({key}, {value}) has finished")

print("Result:", result)
