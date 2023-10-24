from .ControladorMostrar_Mensaje import ControladorMostrar_Mensaje

class ControladorRegistrarUsuario:
    def __init__(self, vista, modelo):
        self.vista = vista
        self.modelo = modelo
        
        self.mensaje = ControladorMostrar_Mensaje()
        
    # funcion para registrar un usuario en la ventana 
    def RegistrarUsuario(self):
        Usuario=self.vista.contra.line_usuario.text()
        Contraseña=self.vista.contra.line_contra.text()
        Contraseña_2=self.vista.contra.line_contra_2.text()
        Contra_ad=self.vista.contra.line_contra_ad.text()
        
        if len(Usuario)==0 or len(Contraseña)==0 or len(Contraseña_2)==0 or len(Contra_ad)==0:
            self.mensaje.mostrar_mensaje("Error", "Por favor Ingrese todos los datos")
            
        elif Contraseña != Contraseña_2:
            self.mensaje.mostrar_mensaje("Error", "Por favor ingrese las contraseñas iguales")
            
        elif Contra_ad != ('UPTBarinas.'):
            self.mensaje.mostrar_mensaje("Error", "Contraseña de administrador es incorrecta")
            
        elif Contraseña == Contraseña_2:
            resultado = self.modelo.ModelLogin.registrar_con(Usuario, Contraseña)
            self.mensaje.mostrar_mensaje("Éxito!", "Se ha registrado exitosamente!")
            self.volver_login()
            self.vista.contra.line_usuario.setText("")
            self.vista.contra.line_contra.setText("")
            self.vista.contra.line_contra_2.setText("")

    #funcion para volver/regresar a la ventrana login, desde la ventana registrar entrada y salida  (contra > login)
    def volver_login(self):
        self.vista.ocultar_contra()
        self.vista.mostrar_login()