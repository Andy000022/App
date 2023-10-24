from .ModelLogin import ModelLogin
from .ModelTrabajadores import ModelTrabajadores
from .ModelRegistro import ModelRegistro
import sqlite3 as sql

class Model:

    def __init__(self):
        
        self.ModelLogin = ModelLogin()
        self.ModelTrabajadores = ModelTrabajadores()
        self.ModelRegistro = ModelRegistro()


        self.crear_tablas()

    def ejecutar_consulta(self, instruccion):
        # Conectar a la base de datos
        con = sql.connect('base_de_datos.db', isolation_level=None)
        cursor = con.cursor()
        # Ejecutar la consulta
        cursor.execute(instruccion)
        # Guardar los cambios y cerrar la conexión
        con.commit()
        con.close()


    def crear_tabla_login(self):
        instruccion = '''CREATE TABLE IF NOT EXISTS "Login" (
                            "Usuario" TEXT,
                            "Contraseña" BLOB NOT NULL,
                            PRIMARY KEY("Usuario")
                        );'''
        self.ejecutar_consulta(instruccion)


    def crear_tabla_registro(self):
        instruccion = '''CREATE TABLE IF NOT EXISTS "Registro" (
                            "Cedula" INTEGER,
                            "Entrada" DATETIME,
                            "Salida" DATETIME,
                            FOREIGN KEY("Cedula") REFERENCES "Trabajadores"("Cedula")
                        );'''
        self.ejecutar_consulta(instruccion)

    def crear_tabla_trabajadores(self):
        instruccion = '''CREATE TABLE IF NOT EXISTS "Trabajadores" (
                            "Nombres" TEXT,
                            "Apellidos" TEXT,
                            "Edad" INTEGER,
                            "Sexo" TEXT,
                            "Telefono" INTEGER,
                            "Area" TEXT,
                            "Cedula" INTEGER,
                            "Correo" TEXT
                        );'''
        self.ejecutar_consulta(instruccion)

    def crear_tablas(self):
        self.crear_tabla_login()
        self.crear_tabla_registro()
        self.crear_tabla_trabajadores()