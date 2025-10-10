class Consulta:

    #SENTENCIAS SQL EN FORMATO STRING    
    CREATE_TABLE = "CREATE TABLE empleado (ID int auto_increment PRIMARY KEY, NOMBRE VARCHAR(50) NOT NULL, CARGO VARCHAR(50) NOT NULL, SALARIO INT NOT NULL);"
    
    DELETE_TABLE = "DROP TABLE empleado;"

    INSERT = "INSERT INTO empleado VALUES(null, %s, %s, %s);"

    SELECT = "SELECT * FROM empleado;"

    UPDATE = "UPDATE empleado SET NOMBRE=%s, CARGO=%s, SALARIO=%s WHERE ID="

    DELETE = "DELETE FROM empleado WHERE ID="

    BUSCAR = "SELECT * FROM empleado WHERE NOMBRE LIKE '%' %s '%'"

