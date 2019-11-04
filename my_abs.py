def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

y=float(input('求绝对值: '))
x=my_abs(y)
print(x)       