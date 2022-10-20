# числа фибаначи 0 1 1 2 3 5 8 13 21 34 (каждое последующее число  является суммой 2х предыдущих)

def fibonacci(index):
    first = 0
    second = 1

    if index < 2:
        return index   # тк индекс и первые значения равны


    for i in range(2, index + 1):
        third = first + second
        first = second
        second = third
    return third


def main():
    index = int(input("Input index in Fibonacci row: "))
    element = fibonacci(index)

    msg = f"Fibonacci[{index}] is {element}"

    print(msg)

main()