import re
from itertools import filterfalse

print("Вывести отдельно буквы и цифры в заданном списке.")
a=['a','b','2','3','c']
print(f"Задан список: {a}")
reg=re.compile(r'^\d+$')
predicate=lambda x: reg.match(x) is not None
b=list(filterfalse(predicate,a))
c=list(filter(predicate,a))
print(f"Буквы: {b}")
print(f"Цифры: {c}")