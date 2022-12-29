print("Отфильтровать двузначные числа в указанном списке.")
inp = input("Введите список целых чисел в одну строку через пробел\n>>> ")
try:
    nums = [int(num) for num in inp.split()]
    fnums = filter(lambda n: 9 < abs(n) < 100, nums)
    print(f"Двузначные числа в списке: {' '.join([str(n) for n in fnums])}")
except:
    print("Неверный формат ввода.")
