# coding : utf-8
import os
import psutil      #сторонний модуль
import sys
import shutil

def duplicate_file(filename):
	if os.path.isfile(filename):
				newfile = filename + ".dupl"
				shutil.copy(filename, newfile)
				if os.path.exists(newfile):
					print("Файл ", newfile, " был успешно создан")
					return True
				else:
					print("Возникли проблемы при копировании")
					return False

def sys_info():
	print("Текущая рабочая директория: ", os.getcwd())
	print( "Платформа (ОС): ", sys.platform)
	print( "Кодировка файловой системы: ", sys.getfilesystemencoding())
	print( "Логин пользователя: ", os.getlogin())
	print( "Количество CPU:", psutil.cpu_count())

def del_dubl(direct):
	file_list = os.listdir(direct)
	double_count = 0
	for f in file_list:
		fullname = os.path.join(direct, f)
		if  fullname.endswith(".dupl"):
			os.remove(fullname)
			if not os.path.exists(fullname):
					print("Файл ", fullname, " был успешно создан")
					double_count += 1
				else:
					print("Возникли проблемы при копировании")
	return double_count

print("Мастер Питона :-)")
print("привет, программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать!")

answer = ""

while answer != 'q':
	answer = input("Давайте поработаем?  (Y/N/q) ")

	if answer == "Y":
		print("Отлично, хозяин!")
		print("Я умею:")
		print("[1] - выведу список файлов")
		print("[2] - выведу информацию о системе")
		print("[3] - выведу список процессов")
		print("[4] - продублирую  файлы в текущей директории")
		print("[5] - дублирование указанного файла")
		print("[6] - удаление файлов с окончанием dupl в текущей директории")
		do = int(input("Укажите номер действия: "))

		if do == 1:
			print(os.listdir())
		
		elif do == 2:
			sys_info()

		elif do == 3:
			print(psutil.pids())
		
		elif do == 4:
			print("---Дублирование файлов в текущей директории")
			file_list = os.listdir()
			i = 1
			while i < len(file_list):
				duplicate_file(file_list[i])
				i += 1
		
		elif do == 5:
			file_dupl = input("Какой файл дублировать? ")
			duplicate_file(file_dupl)

		elif do == 6:
			direct = input("Укажите директорию ")
			count = str(del_dubl(direct))
			print("Удалено " + count + " файлов")
		else:
			pass

	elif answer == "N":
		print("До свидания!")
	else:
		print("Неизвестный выбор")