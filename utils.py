import os

from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
import sys,time
class Music:
    def __init__(self):
        self.path=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'assets/sample.mp3')
        self.url=QUrl.fromLocalFile(self.path)
        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(self.url))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.player=QMediaPlayer()
        self.player.setPlaylist(self.playlist)
    def play(self):
        print("audio started")
        self.player.play()
    def stop(self):
        print("audio stopped")
        self.player.stop()
    def change_music(self,path):
        self.path=path
        self.url=QUrl.fromLocalFile(self.path)
        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(self.url))
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.player=QMediaPlayer()
        self.player.setPlaylist(self.playlist)
    def mute(self):
        print("muted")
        self.player.setVolume(0)
    def unmute(self):
        print("unmuted")
        self.player.setVolume(100)

class Timerthread(QThread):
    signal = pyqtSignal(int)
    def __init__(self,limit):
        super(Timerthread,self).__init__()
        self.limit_seconds = limit
    def run(self):
        i=self.limit_seconds
        self.flag=False
        while i>0:
            if self.flag:
                break
            self.signal.emit(i)
            time.sleep(1)

            i-=1
        self.signal.emit(-1)