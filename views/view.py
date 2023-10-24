from PyQt5 import QtWidgets, uic

class Vista:

    def __init__(self):
        # Cargar archivos .ui (ventanas)
        self.login = uic.loadUi("views/ventana_p.ui") 
        self.entrar = uic.loadUi("views/ventana_ad.ui")
        self.forma = uic.loadUi("views/ventana_re.ui")
        self.contra = uic.loadUi("views/ventana_re_contra.ui")
        self.verreg = uic.loadUi("views/ventana_ver.ui")
        self.usuario = uic.loadUi("views/ventana_us.ui")

    def mostrar_login(self):
        self.login.show()

    def ocultar_login(self):
        self.login.hide()

    def mostrar_entrar(self):
        self.entrar.show()

    def ocultar_entrar(self):
        self.entrar.hide()

    def mostrar_forma(self):
        self.forma.show()

    def ocultar_forma(self):
        self.forma.hide()

    def mostrar_contra(self):
        self.contra.show()

    def ocultar_contra(self):
        self.contra.hide()

    def mostrar_verreg(self):
        self.verreg.show()

    def ocultar_verreg(self):
        self.verreg.hide()

    def mostrar_usuario(self):
        self.usuario.show()

    def ocultar_usuario(self):
        self.usuario.hide()
