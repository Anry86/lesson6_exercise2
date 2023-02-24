
# ____________________Примечание________________________
# конвертируем кодировку файла в UTF-8, иначе компилятор 
# ругается что кодек не может прочитать русские символы 

print("__________________Урок_6,_задание_2__________________")
print(" Программа считает кол-во натуральных делителей числа ")

# Вводится натуральное число X. Подсчитайте количество 
# натуральных делителей числа X (включая 1 и само число). 
# x ≤ 2e9 (2 миллиарда)

# чтобы программа не закрывалась сразу после вывода результата
# создаём переменную-флаг выхода из программы

exit = 1

# создаём цыкл программы с условием для выхода из программы

while exit == 1:

# вводим количество чисел

    print()
    print("Введите натуральное число")
 
    N = int(input())

# проверяем чтобы число было не больше 2 000 000 000

    if N > 2000000000:
        
        print()
        print("Вы ввели слишком большое число")

    else:

        S = N # создаём счётчик для нахождения методом перебора
        D = 0 # счётчик количества найденных делитилей
        
        # простой алгоритм, но очень ресурсоёмкий на болших числах

        print("Долее будут выведенны все делители")
        print("начиная с наибольшего")
        
        # считаем кол-во делителей

        while S != 0 :
            if N % S == 0: # нет остатка от деления, значит найден делитель
                print(str(S))
                D += 1
            S -= 1

# выводим полученные результаты

    print()
    print("Количество натуральных делитилей числа " + str(N) + " равно " + str(D))

# далее либо выполняем ещё цикл вычисления, либо выходим из программы

    print()
    print("----------------------------------------------")
    print("Чтобы выполнить ещё расчёт, введите число 1.")
    print("Чтобы выйти из программы, введите число 0.")

    exit=int(input())