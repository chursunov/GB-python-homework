rating = [7, 5, 3, 3, 2]
print("Начальный рейтинг ", rating)

while True:
    try:
        number = int(input("Введите элемент рейтинга (для выхода введите любую букву)--> "))
    except ValueError:
        print("Праграмма закончена!")
        exit()
    if number in rating:  # проверяем, есть ли элемент в рейтинге
        shift_count = rating.count(number)  # получаем количество элементов
        position = rating.index(number)  # получаем позицию первого одинакового элемента
        rating.insert(position + shift_count, number)  # размещаем новый элемент следом за имеющимися
    else:
        position = 0
        for element in rating:  # ищем, куда надо вставить новый элемент рейтинга
            if number > element:  # если новый элемент максимальный, то вставляем его в начало
                break
            else:
                position += 1  # выбираем на какую позицию будем вставлять, если новый элемент не максимальный
        rating.insert(position, number)
    print("Новый рейтинг ", rating)
