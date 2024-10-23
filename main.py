# Напишите программу, которая создает список из 5 строк
# и меняет первый и последний элементы в нём.

def get_5_lines():
    list_of_5_lines = []
    for number in range(1, 6):
        line = input(f"Введите {number} строку: ")
        list_of_5_lines.append(line)
    print(f"\nСписок из 5 введенных строк:\n{list_of_5_lines}")
    return list_of_5_lines


list_of_words = get_5_lines()
list_of_words[0], list_of_words[-1] = list_of_words[-1], list_of_words[0]
print(f"\nНовый список, после перестановки элементов:\n{list_of_words}")
