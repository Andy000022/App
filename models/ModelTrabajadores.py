import sqlite3 as sql

class ModelTrabajadores:
    
    def __init__(self):
        pass

    def verificar_cedula(self, cedula):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        cursor.execute('SELECT * FROM trabajadores WHERE cedula = ?', (cedula,))
        return cursor.fetchone()

    def registrar_trabajador(self, nombre, ap, edad, sex, cel, area, cedula, mail):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion = f"INSERT INTO Trabajadores VALUES ('{nombre}', '{ap}'," \
                    f"'{edad}', '{sex}', '{cel}', '{area}','{cedula}', '{mail}')"
        cursor.execute(instruccion)
        con.commit()
        con.close()