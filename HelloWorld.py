# coding : utf-8
import os
import psutil      #сторонний модуль
import sys

print("Мастер Питона :-)")
print("привет, программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать!")

answer = input("Давайте поработаем?  (Y/N) ")

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
		print("[1] - текущая рабочая директория")
		print("[2] - платформа (ОС)")
		print("[3] - кодировка файловой системы")
		print("[4] - логин пользователя")
		print("[5] - количество CPU")
		do_two = int(input("Укажите номер действия: "))

		if do_two == 1:
			print(os.getcwd())
		elif do_two == 2:
			print(sys.platform)
		elif do_two == 3:
			print(sys.getfilesystemencoding())
		elif do_two == 4:
			print(os.getlogin())
		elif do_two == 5:
			print(psutil.cpu_count())
		else:
			pass 

	elif do == 3:
		print(psutil.pids())
	else:
		pass

elif answer == "N":
	print("До свидания!")
else:
	print("Неизвестный выбор")