import sqlite3 as sql
import bcrypt

class ModelLogin:
    
    def __init__(self):
        pass

    def usuario_login(self, usuario, password):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        instruccion = 'SELECT Usuario, Contraseña FROM Login WHERE Usuario = ?'
        cursor.execute(instruccion, (usuario,))
        resultado = cursor.fetchone()
    
        if resultado:
            hashed_password = resultado[1]
            
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                return True
        
        return False

    def registrar_con(self, Usuario, Contraseña):
        con = sql.connect("base_de_datos.db")
        cursor = con.cursor()
        # Encriptar la contraseña
        Contraseña_encriptada = bcrypt.hashpw(Contraseña.encode(), bcrypt.gensalt())
        instruccion = f"INSERT INTO Login VALUES(?, ?)"
        cursor.execute(instruccion, (Usuario, Contraseña_encriptada))
        con.commit()
        con.close()
