from random import*
from keyboard import*
print("Камень, ножницы, бумага")
print(" Камень >> r","\n","Ножницы >> s","\n","Бумага >> p")
fair=0
wina=0
winans=0
f=0
b=""
c=""
print("Вы хотите играть с компьютером или с другим человеком?","\n","компьютер - 1","\n","человек - 2")
choice=""
while True:
	try:
		print("Выберите вариант игры нажав клавишу 1 или 2 ")
		if read_key()=="1":
			choice=1
			break
		elif read_key()=="2":
			choice=2
			break
	except:
		ValueError

print("Если вы хотите закончить игру нажмите q <и если хотите продолжить нажмите любую клавишу>")

while True:
	print("продолжить играть - enter; прекратить играть - esc")
	if read_key()=="esc":
		break
	else:
		while True:
			try:
				print("Игрок 1. Выберите камень, ножницы или бумага")
				if read_key()=="r":
					ans=1
					break
				elif read_key()=="s":
					ans=2
					break
				elif read_key()=="p":
					ans=3
					break
			except:
				ValueError
		if choice==1:
			a=randint(1,3)
		elif choice==2:
			print()
			while True:
				try:
					print("Игрок 2. Выберите камень, ножницы или бумага")
					if read_key()=="r":
						a=1
						break
					elif read_key()=="s":
						a=2
						break
					elif read_key()=="p":
						a=3
						break
				except:
					ValueError
	
		if int(a)==1 and int(ans)==1:
			win="ничья"
			fair+=1
			f=0+fair
		elif int(a)==2 and int(ans)==2:
			win="ничья"
			fair+=1
			f=0+fair
		elif int(a)==3 and int(ans)==3:
			win="ничья"
			fair+=1
			f=0+fair
		elif int(a)==1 and int(ans)==2:
			win="Вы проиграли"
			wina+=1
			wa=0+wina
		elif int(a)==1 and int(ans)==3:
			win="Вы победили"
			winans+=1
			wans=0+winans
		elif int(a)==2 and int(ans)==1:
			win="Вы победили"
			winans+=1
			wans=0+winans
		elif int(a)==2 and int(ans)==3:
			win="Вы проиграли"
			wina+=1
			wa=0+wina
		elif int(a)==3 and int(ans)==1:
			win="Вы проиграли"
			wina+=1
			wa=0+wina
		elif int(a)==3 and int(ans)==2:
			win="Вы победили"
			winans+=1
			wans=0+winans
		else:
			print("нет такого варианта")
	
		if int(a)==1:
			b="камень"
		elif int(a)==2:
			b="ножницы"
		elif int(a)==3:
			b="бумага"

		if int(ans)==1:
			c="камень"
		elif int(ans)==2:
			c="ножницы"
		elif int(ans)==3:
			c="бумага"
		print()
		if choice==1:
			print(f"компьютер выбрал {b}, вы выбрали {c}")
		elif choice==2:
			print(f"игрок 1 выбрал {b}, игрок 2 выбрал {c}")
		print()

print("игра окончена")
if choice==1:
	print(f"компьютер выиграл {wina} раза, вы выиграли {winans} раза, ничья {f}")
elif choice==2:
	print(f"игрок 1 выиграл {wina} раза, игрок 2 выиграл {winans} раза")
