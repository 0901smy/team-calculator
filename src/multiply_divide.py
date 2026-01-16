def multiply(a, b):
    """乘法运算"""
    return a * b

def divide(a, b):
    """除法运算"""
    if b == 0:
        return "错误：除数不能为0"
    return a / b

if __name__ == "__main__":
    print(f"5 * 3 = {multiply(5, 3)}")
    print(f"6 / 2 = {divide(6, 2)}")

