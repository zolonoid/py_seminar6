from itertools import accumulate, takewhile, count

# # Найти список множителей для числа n
# def Divisions(n):
#     a = []
#     f = 2
#     while n > 1:
#         if n % f == 0:
#             a.append(f)
#             n //= f
#         else:
#             f += 1
#     return a


# Найти список множителей для числа n
def Divisions(n):
    return [t[1] for t in takewhile(lambda t: t[0]>1 or t[2]>0,accumulate(count(),lambda t,i: (t[0]//t[1],t[1],1) if t[0]%t[1]==0 else (t[0],t[1]+1,0),initial=(n,2,0))) if t[2]>0]


print("Составить список простых множителей для числа N")
inp=input("Введите натуральное число N...\n")
try:
    n=int(inp)
    print(f"Список простых множителей для числа {n}: {Divisions(n)}")
except:
    print("Это неправильное число")