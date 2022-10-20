#факториал 5 = 5* 4 * 3* 2 *1

#recursion case
# f(5!) = 5 * f(4!)
# f(4!) = 4 * f(3!)
# f(3!) = 3 * f(2!)
# f(2!) = 2 * f(1!)
#
# #base case
# f(1!) = 1
# f(0!) = 1

def factorial(number):
    if number <= 1:
        return 1

    return number * factorial(number - 1)

