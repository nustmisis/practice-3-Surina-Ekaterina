# -*- coding: utf-8 -*-
"""
Напишите функцию которая на вход получает строку с госномером автомибиля и
выводит к какому типу относится данный госномер, или возвращает Fail! если это
не госномер.

Типы гос.номеров:

Тип |    Пример
----+----------
 1А | с227на 69
 1Б |  ао365 78
  2 | ан7331 47
  3 | 3733мм 55

Для корректной работы автоматических тестов не переименовывайте функцию
get_plate_type!
"""

import re


def get_plate_type(plate):
    # ваше решение:
    num_letters = set('авекмнорстухabekmhopctyx')
    if len(plate) == 9 and plate[0] in num_letters and plate[1:4].isdigit() and num_letters.intersection(set(plate[4:6])) == set(plate[4:6]) and plate[-2:].isdigit():
        return "1А"
    elif len(plate) == 8 and num_letters.intersection(set(plate[0:2])) == set(plate[0:2]) and plate[2:5].isdigit() and plate[-2:].isdigit():
        return "1Б"
    elif len(plate) == 9 and num_letters.intersection(set(plate[0:2])) == set(plate[0:2]) and plate[2:6].isdigit() and plate[-2:].isdigit():
        return "2"
    elif len(plate) == 9 and plate[0:4].isdigit() and num_letters.intersection(set(plate[4:6])) == set(plate[4:6]) and plate[-2:].isdigit():
        return "3"
    else:
        return "Fail!"
