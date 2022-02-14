from tkinter import Frame,Label,Button,Tk
import functionFile as f

class Calculator:
	def __init__(self):
		self.window=Tk()
		self.window.title("Calulator")
		self.window.geometry("600x600+520+60")
		self.window.wm_minsize(width=350,height=600)

		self.topFrame=Frame(self.window,bg="black")
		self.topFrameConstuct()
		self.topFrame.place(relheight=0.2,relwidth=1,rely=0)

		self.bottomFrame=Frame(self.window,bg="black")
		self.bottomFrameConstruct()
		self.bottomFrame.place(relheight=0.8,relwidth=1,rely=0.2)
		self.window.mainloop()


	def topFrameConstuct(self):
		self.label =Label(self.topFrame,text=str(),font="arial 30 bold",bg="#313131",fg="#FFF")
		self.label.place(relheight=0.8,relwidth=0.9,rely=0.1,relx=0.05)

	def bottomFrameConstruct(self):
		self.label2=Label(self.bottomFrame,text=str(),font="arial 20 ",bg="black",fg="#FFF",justify="right")
		self.label2.place(relheight=0.16,relwidth=0.9,rely=0.0,relx=0.05)

		self.EqButton=Button(self.bottomFrame,text="=",fg="#fff",font="arial 20 bold",bg="#252525",activebackground="grey",activeforeground="#fff",borderwidth=0,command=self.EqPress)
		self.EqButton.place(rely=0.2,relx=0.025,relheight=0.15,relwidth=0.47)

		self.CButton=Button(self.bottomFrame,text="C",fg="#fff",font="arial 20 bold",bg="#252525",activebackground="grey",activeforeground="#fff",borderwidth=0,command=self.CPress)
		self.CButton.place(rely=0.2,relx=0.505,relheight=0.15,relwidth=0.23)

		self.CancelButtons=Button(self.bottomFrame,text="X",fg="#fff",font="arial 20 bold",bg="#252525",activebackground="grey",activeforeground="#fff",borderwidth=0,command=self.xPress)
		self.CancelButtons.place(rely=0.2,relx=0.745,relheight=0.15,relwidth=0.23)

		self.num7=Button(self.bottomFrame,text="7",fg="#fff",font="arial 20 bold",bg="#090909",activebackground="grey",activeforeground="#fff",borderwidth=0,command=self.num7Press)
		self.num7.place(rely=0.36,relx=0.025,relheight=0.15,relwidth=0.23)

		self.num8=Button(self.bottomFrame,text="8",fg="#fff",font="arial 20 bold",bg="#090909",activebackground="grey",activeforeground="#fff",borderwidth=0,command=self.num8Press)
		self.num8.place(rely=0.36,relx=0.265,relheight=0.15,relwidth=0.23)

		self.num9=Button(self.bottomFrame,text="9",fg="#fff",font="arial 20 bold",bg="#090909",activebackground="grey",activeforeground="#fff",borderwidth=0,command=self.num9Press)
		self.num9.place(rely=0.36,relx=0.505,relheight=0.15,relwidth=0.23)

		self.devideButton=Button(self.bottomFrame,text="/",fg="#fff",font="arial 20 bold",bg="#252525",activebackground="grey",activeforeground="#fff",borderwidth=0,command=self.divPress)
		self.devideButton.place(rely=0.36,relx=0.745,relheight=0.15,relwidth=0.23)

		self.num4=Button(self.bottomFrame,text="4",fg="#fff",font="arial 20 bold",bg="#090909",activebackground="grey",activeforeground="#fff",borderwidth=0,command=self.num4Press)
		self.num4.place(rely=0.52,relx=0.025,relheight=0.15,relwidth=0.23)

		self.num5=Button(self.bottomFrame,text="5",fg="#fff",font="arial 20 bold",bg="#090909",activebackground="grey",activeforeground="#fff",borderwidth=0,command=self.num5Press)
		self.num5.place(rely=0.52,relx=0.265,relheight=0.15,relwidth=0.23)

		self.num6=Button(self.bottomFrame,text="6",fg="#fff",font="arial 20 bold",bg="#090909",activebackground="grey",activeforeground="#fff",borderwidth=0,command=self.num6Press)
		self.num6.place(rely=0.52,relx=0.505,relheight=0.15,relwidth=0.23)

		self.multiplyButton=Button(self.bottomFrame,text="x",fg="#fff",font="arial 20 bold",bg="#252525",activebackground="grey",activeforeground="#fff",borderwidth=0,command=self.mulPress)
		self.multiplyButton.place(rely=0.52,relx=0.745,relheight=0.15,relwidth=0.23)

		self.num1=Button(self.bottomFrame,text="1",fg="#fff",font="arial 20 bold",bg="#090909",activebackground="grey",activeforeground="#fff",borderwidth=0,command=self.num1Press)
		self.num1.place(rely=0.68,relx=0.025,relheight=0.15,relwidth=0.23)

		self.num2=Button(self.bottomFrame,text="2",fg="#fff",font="arial 20 bold",bg="#090909",activebackground="grey",activeforeground="#fff",borderwidth=0,command=self.num2Press)
		self.num2.place(rely=0.68,relx=0.265,relheight=0.15,relwidth=0.23)

		self.num3=Button(self.bottomFrame,text="3",fg="#fff",font="arial 20 bold",bg="#090909",activebackground="grey",activeforeground="#fff",borderwidth=0,command=self.num3Press)
		self.num3.place(rely=0.68,relx=0.505,relheight=0.15,relwidth=0.23)

		self.signAdd=Button(self.bottomFrame,text="+",fg="#fff",font="arial 20 bold",bg="#252525",activebackground="grey",activeforeground="#fff",borderwidth=0,command=self.addPress)
		self.signAdd.place(rely=0.68,relx=0.745,relheight=0.15,relwidth=0.23)

		self.num0=Button(self.bottomFrame,text="0",fg="#fff",font="arial 20 bold",bg="#090909",activeforeground="#fff",borderwidth=0,command=self.num0Press)
		self.num0.place(rely=0.84,relx=0.265,relheight=0.15,relwidth=0.47)

		self.dot=Button(self.bottomFrame,text=".",fg="#fff",font="arial 20 bold",bg="#090909",activebackground="grey",activeforeground="#fff",borderwidth=0,command=self.dotPress)
		self.dot.place(rely=0.84,relx=0.025,relheight=0.15,relwidth=0.23)

		self.signSub=Button(self.bottomFrame,text="-",fg="#fff",font="arial 20 bold",bg="#252525",activebackground="grey",activeforeground="#fff",borderwidth=0,command=self.subPress)
		self.signSub.place(rely=0.84,relx=0.745,relheight=0.15,relwidth=0.23)

	def num1Press(self):
		self.update(1)

	def num2Press(self):
		self.update(2)

	def num3Press(self):
		self.update(3)

	def num4Press(self):
		self.update(4)

	def num5Press(self):
		self.update(5)

	def num6Press(self):
		self.update(6)

	def num7Press(self):
		self.update(7)

	def num8Press(self):
		self.update(8)

	def num9Press(self):
		self.update(9)

	def num0Press(self):
		self.update(0)

	def dotPress(self):
		self.update(".")

	def EqPress(self):
		self.update("=")

	def CPress(self):
		self.update("C")
	def addPress(self):
		self.update("+")

	def divPress(self):
		self.update("/")

	def subPress(self):
		self.update("-")

	def mulPress(self):
		self.update("*")

	def xPress(self):
		self.update("X")

	def update(self,obj):
		obj=f.objProsses(obj)
		self.label.config(text=str(obj[0]))
		self.label2.config(text=str(obj[1]))


if __name__ == "__main__":
	Calculator()
