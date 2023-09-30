""" My camera Application
  Author: Md Naeem
  jkkniu
  Upcoming SE in Google
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QTimer

import cv2

class window(QTabWidget):
    """Main app window"""
    
    def __init__(self):
        super().__init__()
        
        #variable for app window
        self.window_width=640
        self.window_height=400
        
        #variable for image
        self.image_width=640
        self.image_height=400
        
        
        #set up the window
        self.setWindowTitle("My camera")
        self.setGeometry(700,350,self.window_width,self.window_height)
        self.setFixedSize(self.window_width,self.window_height)
        
        
        #Set up timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.ui()
        
        
    def ui(self):
        """All buttons
        contains all ui things"""
        
        #image label
        self.image_label = QLabel(self)
        self.image_label.setGeometry(0, 0, self.image_width, self.image_height)
        self.show()
        
        #timer
        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)
            
    
    def update(self):
        """update frame"""
        _, self.frame = self.cap.read()
        frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        height, width, channel = frame.shape
        step = channel * width
        
        q_frame = QImage(frame.data, width, height, step, QImage.Format_RGB888)
        self.image_label.setPixmap(QPixmap.fromImage(q_frame))
    
    def save_img(self):
        """update image"""
        pass
    
    def record(self):
        """video capture"""
        pass
    


#run
app = QApplication(sys.argv)
win = window()
sys.exit(app.exec_())
