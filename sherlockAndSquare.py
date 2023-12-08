def betterPow(base,power):
    if(power == 0):
        return 1
    half_power = betterPow(base,power//2)
    if(power % 2 == 0):
        return half_power * half_power
    else:
        return half_power * half_power * base
def solve(n):
    result = 4
    if(n == 0):
        return result
    else:
        for i in range(1,n+1):
            result += betterPow(2,i)
    return result % (betterPow(10,9) + 7)
print(solve(10571))