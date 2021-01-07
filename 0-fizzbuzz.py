def fizzbuzz():
    n = int(input('Enter a number..  '))
    print(n)
    new_set = list(range(n + 1))
    for i in new_set:
        new_num = new_set[i] + 1
        if new_num % 3 == 0:
            print('fizz')
        elif new_num % 5 == 0:
            print('buzz')
        else:
            print(str(new_num))
fizzbuzz()

