import mysql.connector


class Conexion:
    def ConexionBaseDeDatos():
        try:

            conexion = mysql.connector.connect(user='root',
                                           password='Tecnica2019',
                                           host='localhost',
                                           database='base',
                                           port='3306')
        
            
            return conexion
    
        except mysql.connector.Error as error:  
            print("Error al conectar a la base de datos {}".format(error))
            return conexion
    
    def Desconectar (self): 
         if self.conexion.is_connected():
             self.conexion.close()
             print ("Bd desconectada")
 #   ConexionBaseDeDatos()