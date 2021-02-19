import timeit

start = timeit.default_timer()

for i in range(100000):
    print('1')

end = timeit.default_timer()

print(f'{(end - start)}')