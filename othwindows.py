from PyQt5 import QtWidgets,QtCore,uic

class Settings(QtWidgets.QMainWindow):
    signal = QtCore.pyqtSignal(int)
    music_sig=QtCore.pyqtSignal(str)
    def __init__(self,limit):
        super(Settings,self).__init__()
        uic.loadUi('ui/settings.ui',self)
        self.file_name=""
        self.limit.setValue(limit/60)
        
        self.setWindowTitle("Settings")
        self.update.clicked.connect(self.change)
        self.open.clicked.connect(self.change_song)
        self.loc.setText(self.file_name)
        self.limit.setMinimum(0)
        self.limit.setMaximum(600)
        self.limit.valueChanged.connect(self.limit_stat)
    def limit_stat(self,val):
        self.stat.setText(str(round(float(val/60),1)))
    def change(self):
        time_in_secs=float(self.limit.value())*60

        self.signal.emit(int(time_in_secs))
    def change_song(self):
        self.file_name,_=QtWidgets.QFileDialog.getOpenFileName(self,"Open file",r"<Default dir>" , "Musicfiles (*.mp3 *.wav )")
        self.loc.setText(self.file_name)
        self.music_sig.emit(self.file_name)

class End(QtWidgets.QMainWindow):
    sig_to_stop=QtCore.pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/end.ui',self)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowOpacity(0.8)
        self.showFullScreen()
        self.ok.clicked.connect(self.close)
    def close(self):
        self.destroy()