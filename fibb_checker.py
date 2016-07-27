def fib_checker(num):
    a,b = 0,1
    while a < num:
        a,b= b,a+b
    if a == num:
        return True
    else:
        return False
