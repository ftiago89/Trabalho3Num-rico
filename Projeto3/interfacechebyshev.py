# -*- coding: utf-8 -*-
"""
METODO DE GAUSS CHEBYSHEV PARA INTEGRAÇÃO NUMÉRICA
"""
import sys
import numpy as np
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from ChebyshevQuadrature import ChebyshevQuadrature
import scipy.integrate as integrate



Ui_MainWindow, QtBaseClass = uic.loadUiType("gausschebyshevinterface.ui")

#classe principal da interface
class MyApp(QMainWindow):
    #load na ui e eventos de botoes
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.pushButtonCalcular.clicked.connect(self.calcularChebyshev)
    
    #coleta a funcao da interface e parametros de entrada e usa o metodo de hermite
    #para calcular as raizes da funcao.    
    def calcularChebyshev(self):
        cheby = ChebyshevQuadrature()
        f = lambda x: eval(self.ui.textFunc1.toPlainText())
        fPython = lambda x: (eval(self.ui.textFunc1.toPlainText()))/((np.sqrt(1.0-x**2)))
        n = (int)(self.ui.textEditN1.toPlainText())
        resultado = cheby.chebyQuad(f, n)
        self.ui.textResult1.setText((str)(resultado))
        valorIntegral, erro = integrate.quad(fPython, -1, 1)
        self.ui.textResult2.setText((str)(valorIntegral))
        self.ui.textEditDiferenca.setText((str)(abs(resultado-valorIntegral)))
        self.desenhaGraficos(fPython)
        print(fPython(0.5))
    
    #funcao para desenhar o grafico na interface    
    def desenhaGraficos(self, f1):
        
        x = np.arange(-0.9, 0.9, 0.1)
        
        self.ui.MplWidgetGaussChebyshev.canvas.axes.clear()
        self.ui.MplWidgetGaussChebyshev.canvas.draw()
        self.ui.MplWidgetGaussChebyshev.canvas.axes.axhline(y=0, color='r')
        self.ui.MplWidgetGaussChebyshev.canvas.axes.plot(x, f1(x), label='f(x)/(1-x**2)^1/2')
        self.ui.MplWidgetGaussChebyshev.canvas.axes.legend()
        self.ui.MplWidgetGaussChebyshev.canvas.axes.grid()
        self.ui.MplWidgetGaussChebyshev.canvas.draw()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())