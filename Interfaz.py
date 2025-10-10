#Importar Bibliotecas
from tkinter import *
from tkinter import ttk, messagebox
from Mensaje import *
from Gestor import *

############ INVOCAR LOS METODOS para la BD ##################
def conexionBBDD():
    Gestor.conexionBBDD()

def eliminarBBDD():
    Gestor.eliminarBBDD()
    limpiarMostrar()

def limpiarMostrar():
    limpiarCampos()
    mostrar()

def limpiarCampos():
    miId.set("")
    miNombre.set("")
    miCargo.set("")
    miSalario.set("")

def mostrar():
    Gestor.mostrar(tree)

def salirAplicacion():
    valor = messagebox.askquestion("Salir", Mensaje.SALIR)
    if valor == "yes":
        formPrincipal.destroy()

############ INVOCAR LOS METODOS CRUD ##################

def crear():
    Gestor.crear(miNombre.get(), miCargo.get(), miSalario.get())
    limpiarMostrar()

def editar():
    Gestor.actualizar(miNombre.get(), miCargo.get(), miSalario.get(), miId.get())
    limpiarMostrar()

def eliminar():
    Gestor.borrar(miId.get())
    limpiarMostrar()

def buscar():
    Gestor.buscar(tree, miNombre.get())

def seleccionarUsandoClick(event):
    item = tree.identify('item', event.x, event.y)
    miId.set(tree.item(item, "text"))
    miNombre.set(tree.item(item, "values")[0])
    miCargo.set(tree.item(item, "values")[1])
    miSalario.set(tree.item(item, "values")[2])

########### DESARROLLO DE LA INTERFAZ GRAFICA ##########
formPrincipal = Tk()
formPrincipal.title("APLICACIÓN CRUD CON BASE DE DATOS")
formPrincipal.configure(background='lightblue')
formPrincipal.geometry("600x350")

#ICONOS
imagen_crear = PhotoImage(file='imagen/crear.png')
imagen_editar = PhotoImage(file='imagen/editar.png')
imagen_borrar = PhotoImage(file='imagen/eliminar.png')
imagen_buscar = PhotoImage(file='imagen/buscar.png')
imagen_mostrar = PhotoImage(file='imagen/mostrar.png')

#VARIABLES PARA LAS CAJAS DE TEXTOS
miId = StringVar()
miNombre = StringVar()
miCargo = StringVar()
miSalario = StringVar()


########### GRILLA / TABLA ##########
cabecera = ["ID", "Nombre del empleado", "Cargo", "Salario"]
tree = ttk.Treeview(height=10, columns=('#0','#1','#2'))
tree.place(x=0, y=130)
tree.column('#0', width=100)
tree.heading('#0', text = cabecera[0], anchor=CENTER)
tree.heading('#1', text = cabecera[1], anchor=CENTER)
tree.heading('#2', text = cabecera[2], anchor=CENTER)
tree.column('#3', width=100)
tree.heading('#3', text = cabecera[3], anchor=CENTER)
tree.bind("<Button-1>", seleccionarUsandoClick)
mostrar()

########### COLOCAR LOS WIDGETS EN LA VISTA ##########

##Creando los menus##
menubar = Menu(formPrincipal)
menuBaseSet = Menu(menubar, tearoff=0)
menuBaseSet.add_command(label="Crear/Conectar Base de Datos", command=conexionBBDD)
menuBaseSet.add_command(label="Eliminar Base de Datos", command=eliminarBBDD)
menuBaseSet.add_command(label="Salir", command=salirAplicacion)
menubar.add_cascade(label="Inicio", menu=menuBaseSet)

ayudaMenu = Menu(menubar, tearoff=0)
ayudaMenu.add_command(label="Resetear Campos", command=limpiarCampos)
ayudaMenu.add_command(label="Acerca de", command=Gestor.mensaje)
menubar.add_cascade(label="Ayuda", menu=ayudaMenu)

 ##Creando etiquetas y cajas de textos##
e1 = Entry(formPrincipal, textvariable=miId)

l2 = Label(formPrincipal, text="Nombre: ", background='lightblue').place(x=40, y=10)
e2 = Entry(formPrincipal, textvariable=miNombre, width=50).place(x=100, y=10)

l3 = Label(formPrincipal, text="Cargo: ", background='lightblue').place(x=50, y=40)
e3 = Entry(formPrincipal, textvariable=miCargo).place(x=100, y=40)

l4 = Label(formPrincipal, text="Salario:  ", background='lightblue').place(x=270, y=40)
e4 = Entry(formPrincipal, textvariable=miSalario, width=15).place(x=320, y=40)

l5 = Label(formPrincipal, text="ARS", background='lightblue').place(x=400, y=40)

 ##Creando los botones##
b0 = Button(formPrincipal, text="Buscar Registro", image=imagen_buscar, command=buscar).place(x=450, y=10)
b1 = Button(formPrincipal, text="Crear Registro", image=imagen_crear, command=crear).place(x=50, y=85)
b2 = Button(formPrincipal, text="Editar Registro", image=imagen_editar, command=editar).place(x=180, y=85)
b3 = Button(formPrincipal, text="Mostrar Lista", image=imagen_mostrar, command=mostrar).place(x=320, y=85)
b4 = Button(formPrincipal, text="Eliminar Registro", image=imagen_borrar, command=eliminar, bg="red").place(x=450, y=85)


formPrincipal.config(menu=menubar)

formPrincipal.mainloop()


