#!/usr/bin/python3
# -*- coding: utf-8 -*-


def print_words():
    import string
    f = open('text.txt', 'r')       # чтение из текст файла
    f.seek(0)
    str = f.read().decode('utf-8').split()     # decode string

    my_d = dict()                           # new dict
    my_set = set()                          # new set

    for i in str:                   # пропускаю через множества
        my_set.add(i)

    for word in str:
        new_word = word.lower()
        new_word1 = new_word.strip(string.punctuation)  # удаление знаков припенания

        for ky in new_word1:
            if ky not in my_d:
                my_d[ky] = 1
            else:
                my_d[ky] += 1

    for y in my_d:
        print '{1} - {0}'.format(y.encode('utf-8'), my_d[y])
        # print '%s - %d' % (y, my_d[y])    # Вывод на экран
        # print 'test'
    f.close()
    return


print_words()

