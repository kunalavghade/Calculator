base= 0
strval =""
def objProsses(obj):
	try:
		if obj >=0 and obj <=9:
			global strval
			global base
			strval="".join((strval,str(obj)))
			base=eval(strval)
	except:
		if obj == "X":
			try:
				strval=strval[:-1]
			except:
				pass
		elif obj ==".":
			strval=dot(strval)			
		elif obj =="=":
			strval=str(base)
		elif obj =="-":
			strval=Sub(strval)
		elif obj =="+":
			strval=add(strval)
		elif obj =="*":
			strval=mul(strval)
		elif obj == "C":
			strval=""
		elif obj == "/":
			strval=div(strval)

	return strval,base



def Sub(arg):
	arg=str(arg)
	if "+" in arg[-1] or "-" in arg[-1] or "/" in arg[-1] or "*" in arg[-1]:
		return arg
	else:
		arg +="-"
		return arg

def add(arg):
	arg=str(arg)
	if "+" in arg[-1] or "-" in arg[-1] or "/" in arg[-1] or "*" in arg[-1]:
		return arg
	else:
		arg +="+"
		return arg

def div(arg):
	arg=str(arg)
	if "+" in arg[-1] or "-" in arg[-1] or "/" in arg[-1] or "*" in arg[-1]:
		return arg
	else:
		arg +="/"
		return arg

def mul(arg):
	arg=str(arg)
	if "+" in arg[-1] or "-" in arg[-1] or "/" in arg[-1] or "*" in arg[-1]:
		return arg
	else:
		arg +="*"
		return arg

def dot(arg):
	arg=str(arg)
	if "+" in arg[-1] or "-" in arg[-1] or "/" in arg[-1] or "*" in arg[-1]:
		return arg
	else:
		arg +="."
		return arg
	