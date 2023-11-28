from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QDesktopWidget, QHBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton
from PyQt5 import QtGui
import sys


class Ventana1(QMainWindow):

    #Hacer el metodo de construccion de la ventana
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

        # Poner el título:
        self.setWindowTitle("Formulario de registro")

        # poner icono
        self.setWindowIcon(QtGui.QIcon('imagenes/imagen1.jpg'))

        # Propirdades de ancho y alto
        self.ancho = 800
        self.alto = 600

        #establecer tamaño de la ventana
        self.resize(self.ancho, self.alto)

        # hacer que la ventana quede en el centro
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # para que la pantalla no se pueda cambiar de tamaño
        self.setFixedHeight(self.alto)
        self.setFixedWidth(self.ancho)

        #establecemos el fondo principal:
        self.fondo = QLabel(self)
        self.imagenFondo = QPixmap('imagenes/imagen3.png')

        self.fondo.setPixmap(self.imagenFondo)

        self.fondo.setScaledContents(True)

        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        self.setCentralWidget(self.fondo)

        self.horizontal = QHBoxLayout()

        self.horizontal.setContentsMargins(30, 30, 30, 30)

        #layout izquierdo :
        self.ladoIzquierdo = QFormLayout()

        # Hacemos un letrero
        self.letrero1 = QLabel()

        # Le escribimos un texto
        self.letrero1.setText("Información del cliente")

        #tipo de letra
        self.letrero1.setFont(QFont("arial", 20))
        #color de letra
        self.letrero1.setStyleSheet("color: #FFFFFF")

        self.ladoIzquierdo.addRow(self.letrero1)

        self.letrero2 = QLabel()

        self.letrero2.setFixedWidth(340)

        self.letrero2.setText("por favor ingrese la información del cliente"
                              "\nen el formulario de abajo los campos marcados"
                              "\ncon asterico son obligarios.")

        self.letrero2.setFont(QFont("arial", 10))

        self.letrero2.setStyleSheet("color: #001F7A; margin: 40px "
                                    "margin-top:20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #FFFFFF"
                                    "border-left: none;"
                                    "border-right:none;"
                                    "border-top: none;")

        self.ladoIzquierdo.addRow(self.letrero2)

        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)
        self.ladoIzquierdo.addRow("Nombre completo*", self.nombreCompleto)

        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("password*", self.password)

        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("password*", self.password2)

        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)
        self.ladoIzquierdo.addRow("Correo*", self.correo)

        self.botonRegistrar = QPushButton("Registrar")

        self.botonRegistrar.setFixedWidth(90)

        self.botonRegistrar.setStyleSheet("background-color: #000845;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        self.botonLimpiar = QPushButton("limpiar")

        self.botonLimpiar.setFixedWidth(90)

        self.botonLimpiar.setStyleSheet("background-color: #000342;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)

        self.horizontal.addLayout(self.ladoIzquierdo)

        #PONER AL FINAL
        self.fondo.setLayout(self.horizontal)

    def accion_botonLimpiar(self):
        pass

    def accion_botonRegistrar(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana1 =  Ventana1 ()
    ventana1.show()
    sys.exit(app.exec_())