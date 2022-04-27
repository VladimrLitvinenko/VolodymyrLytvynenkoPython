# Task 1
i = int(input("Enter the number: "))
if i > 7:
    print("Привет")

# Task 2
name = input("Enter name: ")
if name == "Вячеслав":
    print(f"Привет {name}")
else:
    print(f"Нет такого имени")

# Task 3
numbers_list = [1, 2, 3, 4, 6, 8, 3]
count = 0
for i in numbers_list:
    if i == 3:
        print(i)
        count += 1
print(f"Итого колличество элементов кратные трем = {count}")

# Task 4
list1 = [[((()), (), (()))]]
# 1.Добавил '[' вначале. Так как у нас была только закрывающая скобка для листа (название массива в питоне)
# 2. И добавил ')' в конце
# 3. Так как это лист с нестед тупалми, то еще добавил запятые как требует синтаксис