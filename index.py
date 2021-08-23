
#Importar as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser


#Criar nossa janela
jan = Tk()
jan.title("DP Systems - Acess Painel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha",0.9) #propriedade para deixar transparente
#jan.iconbitmap(default="icons/LogoIcon.ico")

#Carregando Imagens
logo = PhotoImage(file="Original.png")

#Widgets
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
UserLabel.place(x=10, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=155, y=110)

PassLabel = Label(RightFrame, text="Password:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=10, y=150)

PassEntry = ttk.Entry(RightFrame, width=30, show="•")
PassEntry.place(x=150, y=160)


def Login():
	User = UserEntry.get()
	Pass = PassEntry.get()

	DataBaser.cursor.execute("""
	SELECT * FROM Users
	WHERE (User=? AND Password=?)
	""", (User, Pass))
	#print("Selecionou")
	VerifyLogin = DataBaser.cursor.fetchone()
	try:
		if (User in VerifyLogin and Pass in VerifyLogin):
			messagebox.showinfo(title="Login Info", message="Acesso Confirmado. BEM VINDO!")
	except:
		messagebox.showinfo(title="Login Info", message="Acesso Negado. Usuario ou Senha incorretos!")

#Botoes
LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=120, y=210)

def Register():
	#Removendo widgets de login
	LoginButton.place(x=5000)
	RegisterButton.place(x=5000)
	#inserindo widgets de cadastro
	NomeLabel = Label(RightFrame, text="Name:", font = ("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
	NomeLabel.place(x=7, y=5)

	NomeEntry = ttk.Entry(RightFrame, width=40)
	NomeEntry.place(x=105, y=16)

	EmailLabel = Label(RightFrame, text = "Email:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="white")
	EmailLabel.place(x=7, y=55)

	EmailEntry = ttk.Entry(RightFrame, width=40)
	EmailEntry.place(x=105, y=66)

	def RegisterToDataBase():
		Nome = NomeEntry.get()
		Email = EmailEntry.get()
		Usuario = UserEntry.get()
		Senha = PassEntry.get()

		if (Nome=="" or Email =="" or Usuario=="" or Senha==""):
			messagebox.showerror(title="Register Error", message="Preencha Todos os Campos")
		else:
			DataBaser.cursor.execute("""
			INSERT INTO Users(Name, Email, User, Password)	VALUES(?, ?, ?, ?)
			""", (Nome, Email, Usuario, Senha))
			DataBaser.conn.commit()
			messagebox.showinfo(title="Register Info", message="Register Sucessfull")

	Register = ttk.Button(RightFrame, text = "Register", width=30, command=RegisterToDataBase)
	Register.place(x=120, y=220)


	def BackToLogin():
		#Removendo Widgets de cadastro
		NomeLabel.place(x=5000)
		NomeEntry.place(x=5000)
		EmailLabel.place(x=5000)
		EmailEntry.place(x=5000)
		Register.place(x=5000)
		Back.place(x=5000)
		LoginButton.place(x=120, y=210)
		RegisterButton.place(x=150, y=250)


	Back = ttk.Button(RightFrame, text="Back", width=20, command=BackToLogin)
	Back.place(x=150, y=260)


RegisterButton = ttk.Button(RightFrame, text="Register", width=20, command=Register)
RegisterButton.place(x=150, y=250)


jan.mainloop()
