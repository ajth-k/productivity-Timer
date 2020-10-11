import sys,time
from PyQt5 import QtWidgets,uic,QtCore
from othwindows import End,Settings
from util import Music,Timerthread 
class MainWindow(QtWidgets.QMainWindow):
    signal_to_sett=QtCore.pyqtSignal()
    def __init__(self,*args,**kwargs):

        super(MainWindow,self).__init__()

        uic.loadUi('ui/main.ui',self)
        self.setWindowTitle("Productivity Timer")
        self.mute.setCheckState(2)
        self.time_in_secs=1800
        self.stop.hide()
        self.thread =Timerthread(self.time_in_secs)
        self.settings.clicked.connect(self.to_settings)
        self.stop.clicked.connect(self.stop_thread)

        self.mute.stateChanged.connect(self.state_changed)


        self.start.clicked.connect(self.timer)
        self.bgm=Music()
    def state_changed(self,val):
        if val==0:
            self.bgm.mute()
        else:
            self.bgm.unmute()
    def to_settings(self):
        self.signal_to_sett.emit()
    def timer(self):
        self.start.hide()
        self.stop.show()
        self.thread.signal.connect(self.change_label)
        self.thread.start()
        self.bgm.play()
    def stop_thread(self):
        self.thread.flag=True
        self.count.setText("0:0")
        self.stop.hide()
        self.bgm.stop()


    def change_label(self,val):
        if val==-1:
            self.end=End()
            self.end.show()
            self.start.show()
            self.count.setText("Ok!")
            self.bgm.stop()

        else:
            if val<3600:
                self.count.setText("{:.2f}".format(round(float(val/60),2)))
                self.time.setText("Minutes")
            else:
                self.count.setText("{:.2f}".format(round(float(val/3600),2)))
                self.time.setText("Hours")

class Controller:
    def show_main(self):
        self.main=MainWindow()
        self.main.show()
        self.main.signal_to_sett.connect(self.settings)
    def settings(self):
        self.settings=Settings(self.main.thread.limit_seconds)
        self.settings.signal.connect(self.change_limit)
        self.settings.music_sig.connect(self.change_music)
        self.settings.show()
    def change_limit(self,val):
        self.main.thread.limit_seconds=val
        print(self.main.thread.limit_seconds)
    def change_music(self,path):
        self.main.bgm.change_music(path)


app=QtWidgets.QApplication(sys.argv)
ctr=Controller()
ctr.show_main()
sys.exit(app.exec_())