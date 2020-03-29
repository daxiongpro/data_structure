def n_jc(n):
    sum = 1
    for i in range(1, n+1):
        sum *= i
    return sum

def jixian(n):
    return n_jc(n) / 2**n

x = jixian(20)
print(x)