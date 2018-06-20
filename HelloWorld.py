# coding : utf-8
import os
import psutil      #сторонний модуль

print("Мастер Питона :-)")
print("привет, программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать!")

answer = input("Давайте поработаем?  (Y/N)")

if answer == "Y":
	print("Отлично, хозяин!")
	print("Я умею:")
	print("[1] - выведу список файлов")
	print("[2] - выведу информацию о системе")
	print("[3] - выведу список процессов")
	do = int(input("Укажите номер действия: "))

	if do == 1:
		print(os.listdir())
	elif do == 2:
		pass
	elif do == 3:
		print(psutil.pids())
	else:
		pass

elif answer == "N":
	print("До свидания!")
else:
	print("Неизвестный выбор")