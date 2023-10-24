import sqlite3 as sql
import datetime

class ModelRegistro:
    
    def __init__(self):
       pass

    def set_entrada(self, cedula, hora_fecha):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        cursor.execute('''INSERT INTO registro (cedula, entrada) VALUES (?, ?)''', (cedula, hora_fecha))
        con.commit()
        con.close()
        
    def actualizar_registro(self, hora_fecha, cedula):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        cursor.execute('''UPDATE registro SET salida = ? WHERE cedula = ? AND salida IS NULL''', (hora_fecha, cedula))
        con.commit()
        con.close()
    
    def verificar_entrada(self, cedula):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d')
        cursor.execute('SELECT * FROM registro WHERE cedula = ? AND DATE(entrada) = ?', (cedula, fecha_actual))
        return cursor.fetchone()
    
    def verificar_salida(self, cedula):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        fecha_actual = datetime.datetime.now().strftime('%Y-%m-%d')
        cursor.execute('SELECT * FROM registro WHERE cedula = ? AND DATE(salida) = ?', (cedula, fecha_actual))
        return cursor.fetchone()
    

    def cargar_registros(self):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion = "SELECT * from Registro"
        cursor.execute(instruccion)
        resultados = cursor.fetchall()
        return resultados

