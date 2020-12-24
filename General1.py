# Решите следующую задачу: напишите программу, которая запрашивает ввод двух значений.
# Если хотя бы одно из них не является числом, то должна выполняться конкатенация, т. е.
# соединение, строк. В остальных случаях введенные числа суммируются.


def getNumber01():

    getNumber1 = input('Введите 1 число: ')
    getNumber2 = input('Введите 2 число: ')
    try:
        if int(getNumber1) and int(getNumber1):
            c = int(getNumber1) + int(getNumber2)
            print(c)
    except ValueError:
        print(getNumber1 + getNumber2)


print(getNumber01())
