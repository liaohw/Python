from PyQt5 import QtWidgets
from Ui_test import Ui_MyForm
import sys

class MainWindow(QtWidgets.QWidget, Ui_MyForm):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.setupUi(self)
	def inputText(self):
		text, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
		if ok:
			self.label.setText(str(text))



if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	main = MainWindow()
	main.show()
	sys.exit(app.exec_())

