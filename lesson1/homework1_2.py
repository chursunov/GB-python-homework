time_in_seconds = int(input("Введите количество секунд: "))
hours = time_in_seconds // 3600
minutes = (time_in_seconds - 3600 * hours) // 60
seconds = round((time_in_seconds - 3600 * hours) % 60, 2)
print("Время в формате чч:мм:сс >>> %02d:%02d:%02d" % (hours, minutes, seconds))
