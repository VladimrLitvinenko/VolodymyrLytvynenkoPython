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

# Task 3
list1 = [[((()), (), (()))]]
