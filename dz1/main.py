# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import random
import time
import calendar


def dz2_1():
    print("Поиск минимального элемента из рандомно-генерирующегося "
          "\nмассива в 10000000 значений в диапазоне от 0 до 100000")
    mas = [random.randint(0, 1000000) for i in range(10000000)]

    start = time.time()
    mins = 1000000

    for i in mas:
        if mins > i:
            mins = i

    end = time.time()
    print("Время выполнения", end - start, "Минимальный элемент", mins)


def dz2_2():
    year = 1970
    per = 2
    monthc = 1
    monthdays = 31
    current_gmt = time.gmtime()

    time_stamp = calendar.timegm(current_gmt)

    secs = time_stamp % 60
    m_time_stamp = time_stamp // 60
    mints = m_time_stamp % 60
    h_time_stamp = m_time_stamp // 60
    hours = h_time_stamp % 24
    d_time_stamp = h_time_stamp // 24

    while d_time_stamp > 365 + (per // 4):
        if per != 4:
            d_time_stamp -= 365
            per += 1
        else:
            d_time_stamp -= 366
            per = 1
        year += 1

    while d_time_stamp >= monthdays:
        if monthc % 2 == 1 | monthc == 8:
            monthdays = 31
            d_time_stamp -= 31
        elif monthc == 2:
            if per != 4:
                monthdays = 28
                d_time_stamp -= 28
            else:
                monthdays = 29
                d_time_stamp -= 29
        else:
            monthdays = 30
            d_time_stamp -= 30
        monthc += 1

    print("Current time:", year, monthc, d_time_stamp, hours, mints, secs)


print('0 - поиск минимального элемента массива в кратчайшее время,'
      ' \n1 и более - вывод времени и даты с помощью timestamp')
z = int(input())
if z == 0:
    """Используя стандартные функции"""
    dz2_1()
else:
    """Используя свои функции"""
    dz2_2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
