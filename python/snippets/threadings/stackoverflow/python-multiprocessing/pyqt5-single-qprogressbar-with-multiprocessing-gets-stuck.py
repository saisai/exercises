import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, pyqtSlot
import multiprocessing as mp
import threading

targets = list(range(0, 100))


def process(i):
    print("target:", i)
    # do something, for example:
    for c in range(1000):
        for r in range(1000):
            c = c * r + 4


class MainWin(QWidget):

    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi()
        self.done = False

    def setupUi(self):
        self.setFixedSize(500, 90)
        self.layout = QGridLayout()
        self.main_widget = QWidget(self)
        self.progressBar = QProgressBar(self.main_widget)
        self.progressBar.setValue(0)

        self.btn = QPushButton('start',self.main_widget)

        self.layout.addWidget(self.progressBar, 0, 0, 1, 1)
        self.layout.addWidget(self.btn, 1, 0, 1, 1)
        self.setLayout(self.layout)

        self.btn.clicked.connect(self.run)
        self.single_done.connect(self.display)
        self.all_done.connect(self.process_results)

    single_done = pyqtSignal()
    @pyqtSlot()
    def display(self):
        self.progressBar.setValue(self.progressBar.value() + 1)
        print("process bar:", self.progressBar.value())
    
    all_done = pyqtSignal()
    @pyqtSlot()
    def process_results(self):
        print("Processing results")
        pass  # do something with the results

    def run(self):
        def func(results):
            pool = mp.Pool()
            for t in targets:
                pool.apply_async(process, (t,), callback=lambda *args: self.single_done.emit())
                results.append(t)
            pool.close()
            pool.join()
            self.all_done.emit()

        results = []
        t = threading.Thread(target=func, args=(results,))
        t.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWin()
    main_win.show()
    sys.exit(app.exec_())