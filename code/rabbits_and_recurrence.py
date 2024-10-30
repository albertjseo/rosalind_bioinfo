# sample data set provided 5 & 3
# start the Fibonacci sequence at 1

def rabbit_recurrence(n, k):
    parent, child = 1, 1
    for months in range(1, n - 1):
        child, parent = parent, parent + (child * k)
    return parent


# test print
print(rabbit_recurrence(5, 3))
