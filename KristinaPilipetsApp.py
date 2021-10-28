from random import*
print("Камень, ножницы, бумага")
print(" Камень >> 1","\n","Ножницы >> 2","\n","Бумага >> 3")
ans=""
while type(ans) != int:
	try:
		ans=int(input("Выберите камень, ножницы или бумага"))
	except:
		TypeError
a=randint(1,3)
if a==1 and ans==1:
	win="ничья"
elif a==2 and ans==2:
	win="ничья"
elif a==3 and ans==3:
	win="ничья"
elif a==1 and ans==2:
	win="Вы проиграли"
elif a==1 and ans==3:
	win="Вы победили"
elif a==2 and ans==1:
	win="Вы победили"
elif a==2 and ans==3:
	win="Вы проиграли"
elif a==3 and ans==1:
	win="Вы проиграли"
elif a==3 and ans==2:
	win="Вы победили"
else:
	win="Нет такого варианта"
print(f"компьютер выбрал {a}, вы выбрали {ans}")
print(win)
