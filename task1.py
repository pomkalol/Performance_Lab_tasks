# Достанем ВХОДНЫЕ ДАННЫЕ И ПРЕОБРАЗУЕМ ИХ В Числовой Список
f = open('input.txt', 'r')
r = f.read()
t = r.split()
List = [int(item) for item in t]

# ----------------------------------- ОТСОРТИРУЕМ НАШ СПИСОК
List.sort()

# -----------------------------------  90 перцентиль

import math


def percentile(data, percentile):
    size = len(data)
    return sorted(data)[int(math.ceil((size * percentile) / 100)) - 1]


percent = percentile(List, 90)
percent = format(percent, '.2f')
# ---------------------- Медиана задача
from statistics import median

mediana = median(List)
mediana = format(mediana, '.2f')
# ---------------------- Максимальное значение

maximal = max(List)
maximal = format(maximal, '.2f')
# ---------------------- Минимальное значение

minimal = min(List)
minimal = format(minimal, '.2f')
# --------------------- Среднее значение

averege = sum(List) / len(List)
averege = format(averege, '.2f')

# Принтанем результаты всех вычислений
print(percent)
print(mediana)
print(maximal)
print(minimal)
print(averege)