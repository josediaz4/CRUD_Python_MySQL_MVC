from tkinter import messagebox
from Servicio import *
import Mensaje

class Gestor:

    #Gestionar servicios de conexion
    def conexionBBDD():
        try:
            Servicio.conexionBBDD()
            messagebox.showinfo("Conexión", Mensaje.EXITO_DB)

        except:
            messagebox.showwarning("Conexión", Mensaje.ERROR_DB)
    
    def eliminarBBDD():
        if messagebox.askyesno(message=Mensaje.CONFIRMAR_DB, title="Advertencia"):
            Servicio.eliminarBBDD()
        else:
            messagebox.showwarning("Conexión", Mensaje.ERROR_ELIMINAR_DB)

    #Gestionar servicios CRUD de empleados
    def mostrar(tree):
        registros = tree.get_children()
        for elemento in registros:
            tree.delete(elemento)

        try:
            empleados = Servicio.consultar()
            for row in empleados:
                tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3]))
        except:
            messagebox.showwarning("ADVERTENCIA", Mensaje.ERROR_MOSTRAR)

    def buscar(tree, criterio):
        registros = tree.get_children()
        #aqui escribo la forma corta de escribir el bucle for
        for elemento in registros:
            tree.delete(elemento)

        try:
            if (criterio != ""):
                empleados = Servicio.buscar(criterio)
                #aqui escribo la forma corta de escribir el bucle for
                for row in empleados:
                    tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3]))
            else:
                messagebox.showwarning("ADVERTENCIA", Mensaje.NOMBRE_FALTANTE)
        except:
            messagebox.showwarning("ADVERTENCIA", Mensaje.ERROR_BUSCAR)

    def crear(nombre, cargo, salario):
        try:
            if(nombre != "" and cargo != "" and salario != ""):
                Servicio.crear(nombre, cargo, salario)
            else:
                messagebox.showwarning("ADVERTENCIA", Mensaje.CAMPOS_FALTANTES)
        except:
            messagebox.showwarning("ADVERTENCIA", Mensaje.ERROR_CREAR)

    def actualizar(nombre, cargo, salario, id):
        try:
            if(nombre != "" and cargo != "" and salario != ""):
                Servicio.actualizar(nombre, cargo, salario, id)
            else:
                messagebox.showwarning("ADVERTENCIA", Mensaje.CAMPOS_FALTANTES)
        except:
            messagebox.showwarning("ADVERTENCIA", Mensaje.ERROR_ACTUALIZAR)

    def borrar(id):
        try:

            if messagebox.askyesno(message=Mensaje.CONFIRMAR, title="ADVERTENCIA"):
                Servicio.eliminar(id)
            else:
                pass
        except:
            messagebox.showwarning("ADVERTENCA", Mensaje.ERROR_ELIMINAR)

    #Gestionar version APP
    def mensaje():
        messagebox.showinfo(title="INFORMACION", message=Mensaje.ACERCA)