def print_blank(number):
    for n in range(number):
        print(' ', end='')


start = 0
end = 65
while start <= end:
    for num in range(end-start):
        print('*', end='')
    print()
    print_blank(start+1)
    start = start+1
    end = end-1