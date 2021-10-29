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
			cho=1
			break
		elif read_key()=="2":
			cho=2
			break
	except:
		ValueError

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
		if cho==1:
			a=randint(1,3)
		elif cho==2:
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
		if cho==1:
			print(f"компьютер выбрал {b}, вы выбрали {c}")
		elif cho==2:
			print(f"игрок 1 выбрал {b}, игрок 2 выбрал {c}")
		print()

print("игра окончена")
if cho==1:
	print(f"компьютер выиграл {wina} раза, вы выиграли {winans} раза, ничья {f}")
elif cho==2:
	print(f"игрок 1 выиграл {wina} раза, игрок 2 выиграл {winans} раза")
print()
print("--------------------------")
while True:
	print("продолжить играть - 1; закончить играть - 2")
	if read_key()=="2":
		break
	else:
		print("компьютеры играют в камень, ножницы, бумага")
		rob1=0
		rob2=0
		rob3=0
		a=randint(1,3)
		b=randint(1,3)
		if a==1 and b==1:
			win="ничья"
			rob3+=1
		elif a==2 and b==2:
			win="ничья"
			rob3+=1
		elif a==3 and b==3:
			win="ничья"
			rob3+=1
		elif a==1 and b==2:
			win="Бот 1 победил"
			rob1+=1
		elif a==1 and b==3:
			win="Бот 2 победил"
			rob2+=1
		elif a==2 and b==1:
			win="Бот 2 победил"
			rob2+=1
		elif a==2 and b==3:
			win="Бот 1 победил"
			rob1+=1
		elif a==3 and b==1:
			win="Бот 1 победил"
			rob1+=1
		elif a==3 and b==2:
			win="Бот 1 победил"
			rob1+=1

		if a==1:
			d="камень"
		elif a==2:
			d="ножницы"
		elif a==3:
			d="бумага"

		if b==1:
			c="камень"
		elif b==2:
			c="ножницы"
		elif b==3:
			c="бумага"

		print(f"компьютер 1 выбрал {d}, комптютер 2 выбрал {c}")
		print(win)
print (f"компьютер 1 выиграл {rob1} раз, комптютер 2 выиграл {rob2} раз")
print("--------------------------")
################
#пример с ботами
m=0
while m not in [1,2]:
	try:
		m=int(input("Kellega mängimine?\n1-botid \n2-robotiga"))
	except:
		ValueError
v1=["Kivi","Käärid","Paber"]
v2=["Kivi","Käärid","Paber"]
if m==1:
	while True:
		print("kas mängime? q - välja, enter - mängimine")
		if read_key()=="q":
			break
		elif read_key()=="enter":
			p1=choice(v1)
			print("Esimine bot: ",p1)
			p2=choice(v2)
			print("Teine bot: ",p2)
			if p1==p2:
				print("Viik")
			elif p1==v1[0] and p2==v2[1] or p1==v2[0] or p1==v1[1] and p2==v2[2]:
				print("Võitis 1")
			else:
				print("Võitis 2")
if m==2:
	while 1:
		pass