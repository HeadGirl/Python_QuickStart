# coding : utf-8

print("Мастер Питона :-)")
print("привет, программист!")
name = input("Ваше имя: ")

print(name, ", добро пожаловать!")

answer = input("Давайте поработаем?  (Y/N)")

if answer == "Y":
	doing = print("Вы хотите кодировать или писать требования? (C/R)")		#pass #print("Вам премия!")
	if doing == "C":
		print("Откройте свой файл в блокноте")
	elif doing = "R":
		print("Откройте вордовский файл")
	else:
		print("Неизвестный ответ")
elif answer == "N":
	print("До свидания!")
else:
	print("Неизвестный выбор")