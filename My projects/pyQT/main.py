import sys
import typing 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget
from gui import Ui_MainWindow
from currency_converter import CurrencyConverter

class CurrencyConvert(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(CurrencyConvert, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    
    def init_UI(self):
        self.setWindowTitle('Currency Converter')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(0, 0)

        self.ui.input_currency.setPlaceholderText('Currency (USD): ')
        self.ui.input_amount.setPlaceholderText('Amount: ')
        self.ui.output_currency.setPlaceholderText('Currency (EURO): ')
        self.ui.output_amount.setPlaceholderText('Amount: ')
        self.ui.pushButton.clicked.connect(self.converter)

    def converter(self):
        converter = CurrencyConverter()
        input_currency = self.ui.input_currency.text()    #USD
        output_currency = self.ui.output_currency.text()  #EURO

        input_amount = int(self.ui.input_amount.text()) # 150
        output_amount = round(converter.convert(input_amount, '%s' % (input_currency), '%s' % (output_currency)), 2)
        self.ui.output_amount.setText(str(output_amount))

app = QtWidgets.QApplication([])
application = CurrencyConvert()
application.show()

sys.exit(app.exec_())