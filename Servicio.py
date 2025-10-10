from Conexcion import *
from Empleado import *
from Consultas import *

class Servicio:
    def conectar():
        miConexion = Conexion.ConexionBaseDeDatos()
        miCursor = miConexion.cursor()
        return miConexion, miCursor

    def conexionBBDD():
        miConexion,miCursor = Servicio.conectar()
        miCursor.execute(Consulta.CREATE_TABLE)

    def eliminarBBDD():
        miConexion,miCursor = Servicio.conectar()
        miCursor.execute(Consulta.DELETE_TABLE)

    def consultar():
        miConexion,miCursor = Servicio.conectar()
        miCursor.execute(Consulta.SELECT)
        return miCursor.fetchall()
    
    def crear(nombre, cargo, salario):
        miConexion,miCursor = Servicio.conectar()
        empleado = Empleado(nombre, cargo, salario)
        miCursor.execute(Consulta.INSERT, (empleado.info()))
        miConexion.commit()

    def actualizar(nombre, cargo, salario, id):
        miConexion,miCursor = Servicio.conectar()
        empleado = Empleado(nombre, cargo, salario)
        miCursor.execute(Consulta.UPDATE+id, (empleado.info()))
        miConexion.commit()

    def eliminar(id):
        miConexion,miCursor = Servicio.conectar()
        miCursor.execute(Consulta.DELETE+id)
        miConexion.commit()

    def buscar(nombre):
        miConexion,miCursor = Servicio.conectar()
        miCursor.execute(Consulta.BUSCAR, (nombre,))
        return miCursor.fetchall()