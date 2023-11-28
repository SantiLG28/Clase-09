from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QLabel, QDesktopWidget, QHBoxLayout, QApplication
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
        self.imagenFondo = QPixmap('imagenes/imagen2.jpg')

        self.fondo.setPixmap(self.imagenFondo)

        self.fondo.setScaledContents(True)

        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        self.setCentralWidget(self.fondo)

        self.horizontal = QHBoxLayout()

        self.horizontal.setContentsMargins(30, 30, 30, 30)

        #PONER AL FINAL
        self.fondo.setLayout(self.horizontal)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana1 =  Ventana1 ()
    ventana1.show()
    sys.exit(app.exec_())