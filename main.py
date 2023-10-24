import sys
from controllers.Controller import Controlador
from models.Model import Model
from views.view import Vista
from PyQt5 import QtWidgets, uic

class Sistema():
    
    def __init__(self):
        self.modelo = Model()
        self.vista = Vista()
        self.controlador = Controlador(self.vista, self.modelo)

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    main = Sistema()
    main.vista.mostrar_login()
    sys.exit(app.exec())