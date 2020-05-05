from tkinter import *
from tkinter import messagebox as MessageBox

root = Tk()
root.resizable(0,0)

# Funciones

def validar():
	cadena = str(texto.get())
	c = 0
	e = 0
	s = 0
	for i in cadena:
		if i.isnumeric():
			c += 1
		elif i == " ":
			e += 1
		elif not i.isalpha():
			s += 1
	if cadena == "":
		MessageBox.showerror("Error","El campo de texto está vacio, ingresa un texto")
	elif c > 0:
		MessageBox.showerror("Error","Ingresa una cadena de texto sin números")
	elif e > 0:
		MessageBox.showerror("Error","Ingresa una cadena de texto sin espacios")
	elif s > 0:
		MessageBox.showerror("Error","Ingresa una cadena de texto sin caracteres especiales")
	elif (len(cadena) <= 5 or len(cadena) >= 10) and c == 0:
		MessageBox.showerror("Error","Ingresa una cadena de texto entre 6 y 10 caracteres")
	elif len(cadena) > 5 and len(cadena) < 10:
		MessageBox.showinfo("Valido","La cadena de texto es válida :)")


# Stringvar

texto = StringVar()

# Configuración de Root

root.title("Prueba de caja negra")
root.config(background="#1E2425")

# Procedimiento

label1 = Label(root,bg="#1E2425",text="Ingresar cadena de texto",pady=5,font=("Sitka",10), fg="white").pack(side="top")
entry1 = Entry(root,textvariable=texto,bg="#263844",fg="white",relief="groove").pack()
frame_separador = Frame(root,bg="#1E2425",height=15).pack()
btn = Button(root,text="Validar",command=validar,bg="#263844",font=("Sitka",10),fg="white").pack(side="top")

# Frames

frame_principal = Frame(root,bg="#1E2425",width=400,height=100).pack()

# Label piso

label2 = Label(root,justify="left",text="Prueba de caja negra - Facundo Kimbo", bg="#263844",font=("Sitka",10),fg="white").pack(anchor="sw",side="bottom",fill="both",expand=1)

# Ejecución

root.mainloop()
