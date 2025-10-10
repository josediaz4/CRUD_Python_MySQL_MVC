class Empleado:
    #Constructor
    def __init__(self, nombre, cargo, salario):
        self.__nombre = nombre
        self.__cargo = cargo
        self.__salario = salario

    #Retornar el empleado
    def info(self):
        return self.__nombre, self.__cargo, self.__salario
    
empleado = Empleado("Manu", "Development Senior", "$2.000.000")
print(empleado.info())