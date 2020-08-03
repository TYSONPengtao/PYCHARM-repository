def fact_sum(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    return fact_sum(n-1) + n * (fact_sum(n-1)-fact_sum(n-2))
print(fact_sum(30))