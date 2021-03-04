for i in range(1, 101):
    if i % 15 == 0:
        print('피즈버즈')
    elif i % 3 == 0:
        print('피즈')
    elif i % 5 == 0:
        print('버즈')
    else:
        print(i)

