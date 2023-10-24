from .ControladorLogin import ControladorLogin
from .ControladorRegistrarUsuario import ControladorRegistrarUsuario
from .ControladorEntradaSalida import ControladorEntradaSalida
from .ControladorHomeAdmin import ControladorHomeAdmin


class Controlador:

    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
        
        self.login = ControladorLogin(vista, modelo)
        self.NuevoUsuario = ControladorRegistrarUsuario(vista, modelo)
        self.EntradaSalida = ControladorEntradaSalida(vista, modelo)
        self.HomeAdmin = ControladorHomeAdmin(vista, modelo)
        
        
            # Botones de ventana de inicio de sesion (login)
        self.vista.login.pushButton.clicked.connect(self.login.validar_login)
        self.vista.login.pushButton_re_contra.clicked.connect(self.registrar_contra)
        self.vista.login.pushButton_2.clicked.connect(self.usua_re)

            # Botones de la ventana registrar un nuevo usurio (contra)
        self.vista.contra.boton_registrar.clicked.connect(self.NuevoUsuario.RegistrarUsuario)
        self.vista.contra.boton_regresar.clicked.connect(self.NuevoUsuario.volver_login)
        
            # Botones de la ventana marcar entrada y salidad (usuario)
        self.vista.usuario.pushButton.clicked.connect(self.EntradaSalida.regi_entra)
        self.vista.usuario.pushButton_2.clicked.connect(self.EntradaSalida.regi_sali)
        self.vista.usuario.boton_regresar.clicked.connect(self.volver_login)
        
            # Botones de la ventana despues de iniciar sesion (entrar)
        self.vista.entrar.pushButton.clicked.connect(self.HomeAdmin.cerrar_sesion)
        self.vista.entrar.pushButton_3.clicked.connect(self.HomeAdmin.regis_empleado)
        self.vista.entrar.ver_reg.clicked.connect(self.HomeAdmin.ver_registro)


    #funcion para ventrar/mostrar la ventrana registrar nuevo usuario, desde la ventana login (login > contra)
    def registrar_contra(self):
        self.vista.ocultar_login()
        self.vista.mostrar_contra()

    #funcion para entrar/mostrar la ventrana registro entrada y salida, desde la ventana login  (login > usuario)
    def usua_re(self):
        self.vista.ocultar_login()
        self.vista.mostrar_usuario()

    #funcion para volver/regresar a la ventrana login, desde la ventana registrar nuevo usuario  (usuario > login)
    def volver_login(self):
        self.vista.ocultar_usuario()
        self.vista.mostrar_login()
