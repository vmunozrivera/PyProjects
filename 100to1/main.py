# 100to1
# Shows all the numbers between 1 and 100, but inverse


if __name__ == '__main__':
    n = range(1, 101)
    n_inv = sorted(n, reverse=True)
    print(n_inv)
