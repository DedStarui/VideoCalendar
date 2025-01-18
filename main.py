import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from random import randint


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #Створи обєкт медія плеєра
        self.media = QMediaPlayer(self)
        #налаштуй вивід зображення в Qwidget
        self.media.setVideoOutput(self.ui.widget)
        #Завантаж відео що треба програвати
        vid=QMediaContent(QUrl.fromLocalFile('Video\\6.avi'))
        self.media.setMedia(vid)
        #запусти відео
        self.media.play()
        #self.media.stop()

    #def configure(self):
        #...

    #def get_date(self):
        #...

    #def media_play(self):
        #...

    #def media_stop(self):
        #...


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())
