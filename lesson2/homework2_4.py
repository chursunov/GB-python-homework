user_string = input("Введите строку --> ")
number_string = 1  # нумерация строк
temp_word = ""

for letter in user_string + " ":  # пробегаем по всей строке + один пробел
    if letter != " ":  # пока не найдем пробел, перебираем слово
        temp_word += letter
    elif temp_word != "":  # проверка на пустое слово (если пользователь ввел несколько пробелов)
        print(f"{number_string} {temp_word[:10]}")  # отсекаем слово из 10 или менее символов
        number_string += 1
        temp_word = ""
