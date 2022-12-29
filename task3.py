print("Преобразовать наборы списков в другой набор и потом вернуть в исходное состояние.")
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]
print(f"Даны списки:\n users = {users}\n ids = {ids}\n salary = {salary}")
new = [list(i) for i in zip(users, ids, salary)]
print(f"Преобразовали их в списки:\n {new[0]}\n {new[1]}\n {new[2]}")
users = [i[0] for i in new]
ids = [i[1] for i in new]
salary = [i[2] for i in new]
print(f"И затем вернули в исходное состояние:\n {users}\n {ids}\n {salary}")
