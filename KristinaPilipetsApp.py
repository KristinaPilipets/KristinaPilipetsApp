from random import*
print("Камень, ножницы, бумага")
print(" Камень >> 1","\n","Ножницы >> 2","\n","Бумага >> 3")
ans=""
while ans not in [1,2,3]:
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

if a==1:
	b="камень"
elif a==2:
	b="ножницы"
elif a==3:
	b="бумага"

if ans==1:
	c="камень"
elif ans==2:
	c="ножницы"
elif ans==3:
	c="бумага"

print(f"компьютер выбрал {b}, вы выбрали {c}")
print(win)
