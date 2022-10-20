# index   0 1 2 3 4 5 6 7  8  9 10 11 12
# element 0 1 1 2 3 5 8 13 21 34 55 89 144

def fibonacci(index):
    # базовый случай base case ( два числа, которые не заданы и определяют результат)
    if index < 2:
        return index

    # recursion case не посредственно рекурсия
    return fibonacci(index - 1) + fibonacci(index - 2)

def main():
    index = int(input("Input index in Fibonacci row: "))
    element = fibonacci(index)

    msg = f"Fibonacci[{index}] is {element}"

    print(msg)

main()