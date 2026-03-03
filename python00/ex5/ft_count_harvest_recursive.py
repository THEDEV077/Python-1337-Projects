def helper(n):
    if (n == 0):
        return
    helper(n - 1)
    print(f"Day {n}")


def ft_count_harvest_recursive():
    x = int(input("Days until harvest: "))
    helper(x)
    print("Harvest time!")
