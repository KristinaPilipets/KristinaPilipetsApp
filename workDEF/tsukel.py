def arithmetic(a: float,b:float,c:str):
	"""lihtne kalkulaator
	+ - liitmine
	- - lahutamine
	* - korrutamine
	/ - jagamine
	:param float a: esimine arv
	:param float b: Teine arv
	:param str c: aritmeetiline tehing
	:rtype float:
	"""
	if c=="+":
		r=a+b
	elif c=="-":
		r=a-b
	elif c=="*":
		r=a*b
	elif c=="/":
		r=a/b
	else:
		print("Неизвестная операция")
	return 