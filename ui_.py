import time
import os
import sys
import shutil

import cv2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qt_material import apply_stylesheet

from detect import main,my_lodelmodel,parse_opt
from play_main import play_midi
from utils.mido_yin import Musical_Instruments

CurFolder=os.getcwd()
DefaultImFolder=CurFolder

class picture(QWidget):
    def __init__(self):
        super(picture, self).__init__()
        self.str_name = '0'
        # self.my_model = my_lodelmodel()
        self.resize(1400, 1200)
        self.setWindowTitle("光学乐谱识别软件V1.0")
        camera_or_video_save_path = 'data\\test'
        if not os.path.exists(camera_or_video_save_path):
            os.makedirs(camera_or_video_save_path)

        self.label1 = QLabel(self)
        self.label1.setText("                                           待检测乐谱")
        self.label1.setFixedSize(500, 700)
        self.label1.move(200, 20)
        self.label1.setStyleSheet("QLabel{background:#7A6969;}"
                                  "QLabel{color:rgb(300,300,300,120);font-size:20px;font-weight:bold;font-family:宋体;}")

        self.label2 = QLabel(self)
        self.label2.setText("                                          检测结果")
        self.label2.setFixedSize(500, 700)
        self.label2.move(750, 20)
        self.label2.setStyleSheet("QLabel{background:#7A6969;}"
                                  "QLabel{color:rgb(300,300,300,120);font-size:20px;font-weight:bold;font-family:宋体;}")

        self.textEdit = QTextEdit(self)
        self.textEdit.setFixedSize(1050,170)
        self.textEdit.move(200,750)

        self.cb = QComboBox(self)
        musical_instruments = list(Musical_Instruments.keys())
        self.cb.addItems(musical_instruments)
        self.cb.move(0,200)

        OpenImgBtn = QPushButton(self)
        OpenImgBtn.setText("打开乐谱")
        OpenImgBtn.setStyleSheet(''' 
                                                     QPushButton
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     QPushButton:pressed
                                                     {text-align : center;
                                                     background-color : light gray;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     ''')
        OpenImgBtn.move(30, 50)
        OpenImgBtn.clicked.connect(self.openimage)

        DeteImgBtn = QPushButton(self)
        DeteImgBtn.setText("检测乐谱")
        DeteImgBtn.setStyleSheet(''' 
                                                     QPushButton
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     QPushButton:pressed
                                                     {text-align : center;
                                                     background-color : light gray;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     ''')
        DeteImgBtn.move(30, 100)
        DeteImgBtn.clicked.connect(self.Test_score)

        PlayImgBtn = QPushButton(self)
        PlayImgBtn.setText("播放乐谱")
        PlayImgBtn.setStyleSheet('''
                                                     QPushButton
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     QPushButton:pressed
                                                     {text-align : center;
                                                     background-color : light gray;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     ''')
        PlayImgBtn.move(30, 150)
        PlayImgBtn.clicked.connect(self.play_music)

        ExitBtn = QPushButton(self)
        ExitBtn.setText('退出应用')
        ExitBtn.setStyleSheet(''' 
                                                     QPushButton
                                                     {text-align : center;
                                                     background-color : #006EFF;
                                                     color : #D4EBFF;
                                                     font: bold;
                                                     border-color: #006EFF;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     QPushButton:pressed
                                                     {text-align : center;
                                                     background-color : light gray;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     ''')
        ExitBtn.move(30, 850)
        ExitBtn.clicked.connect(self.close_app)

        OpenDirBtn = QPushButton(self)
        OpenDirBtn.setText('打开文件')
        OpenDirBtn.setStyleSheet('''
                                                     QPushButton
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     QPushButton:pressed
                                                     {text-align : center;
                                                     background-color : light gray;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     ''')
        OpenDirBtn.move(30, 250)
        OpenDirBtn.clicked.connect(self.OpenDirBntClicked)

        PerimgBtn = QPushButton(self)
        PerimgBtn.setText('上一张')
        PerimgBtn.setStyleSheet('''
                                                     QPushButton
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     QPushButton:pressed
                                                     {text-align : center;
                                                     background-color : light gray;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     ''')
        PerimgBtn.move(15, 300)
        PerimgBtn.clicked.connect(self.PreImBntClicked)

        NextimgBtn = QPushButton(self)
        NextimgBtn.setText('下一张')
        NextimgBtn.setStyleSheet('''
                                                     QPushButton
                                                     {text-align : center;
                                                     background-color : white;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     QPushButton:pressed
                                                     {text-align : center;
                                                     background-color : light gray;
                                                     font: bold;
                                                     border-color: gray;
                                                     border-width: 2px;
                                                     border-radius: 10px;
                                                     padding: 6px;
                                                     height : 14px;
                                                     border-style: outset;
                                                     font : 14px;}
                                                     ''')
        NextimgBtn.move(80, 300)
        NextimgBtn.clicked.connect(self.NextImBntClicked)

        self.imgname1 = '0'
        self.img_name1 = '0'
        self.save_dir1 = '0'
        self.ImFolder = ''  # 图片文件夹路径
        self.ImNameSet = []  # 图片集合
        self.CurImId = 0  # 当前显示图在集合中的编号

    def openimage(self):
        self.textEdit.clear()
        self.label2.clear()
        imgName, imgType = QFileDialog.getOpenFileName(self, "打开图片", "", "*.jpg;;*.png;;All Files(*)")
        img_name = imgName.split("/")[-1]
        self.img_name1 = img_name
        if imgName != '':
            self.imgname1 = imgName
            im0 = cv2.imread(imgName)
            width = im0.shape[1]
            height = im0.shape[0]
            # 设置新的图片分辨率框架
            width_new = 500
            height_new = 700
            # 判断图片的长宽比率
            if width / height >= width_new / height_new:
                show = cv2.resize(im0, (width_new, int(height * width_new / width)))
            else:
                show = cv2.resize(im0, (int(width * height_new / height), height_new))
            im0 = cv2.cvtColor(show, cv2.COLOR_RGB2BGR)
            showImage = QtGui.QImage(im0, im0.shape[1], im0.shape[0], 3 * im0.shape[1], QtGui.QImage.Format_RGB888)
            self.label1.setPixmap(QtGui.QPixmap.fromImage(showImage))

    def Test_score(self):
        self.textEdit.clear()
        if self.imgname1 != '0':
            QApplication.processEvents()
            opt = parse_opt(self.imgname1)
            im0, label,imgs_infor,save_dir = main(opt)
            self.save_dir1 = save_dir
            QApplication.processEvents()
            width = im0.shape[1]
            height = im0.shape[0]
            # 设置新的图片分辨率框架
            width_new = 500
            height_new = 700
            # 判断图片的长宽比率
            if width / height >= width_new / height_new:
                show = cv2.resize(im0, (width_new, int(height * width_new / width)))
            else:
                show = cv2.resize(im0, (int(width * height_new / height), height_new))
            im0 = cv2.cvtColor(show, cv2.COLOR_RGB2BGR)
            image_name = QtGui.QImage(im0, im0.shape[1], im0.shape[0], 3 * im0.shape[1], QtGui.QImage.Format_RGB888)
            self.label2.setPixmap(QtGui.QPixmap.fromImage(image_name))
            for i in range(len(imgs_infor)):
                for j in range(len(imgs_infor[i])):
                    self.textEdit.insertPlainText(str(imgs_infor[i][j] + ' '))
                self.textEdit.append('')
        else:
            QMessageBox.information(self, '错误', '请先选择一个图片文件', QMessageBox.Yes, QMessageBox.Yes)

    def play_music(self):
        if self.imgname1 != '0':
            QApplication.processEvents()
            meta_time = 60 * 60 * 10 / 75
            save_dir = self.save_dir1
            txt_name = self.img_name1.replace('jpg','txt')
            mung_path = os.path.join(save_dir, "mung/{}".format(txt_name))
            musical = self.cb.currentText()
            play_midi(mung_path,meta_time,musical=musical)
            QApplication.processEvents()
        else:
            QMessageBox.information(self, '错误', '请先选择一个图片文件', QMessageBox.Yes, QMessageBox.Yes)

    def OpenDirBntClicked(self):
        ImFolder = QtWidgets.QFileDialog.getExistingDirectory(None,"select folder", DefaultImFolder)
        if ImFolder!='':
            ImNameSet = os.listdir(ImFolder)
            if '.DS_Store' in ImNameSet:
                ImNameSet.remove('.DS_Store')
            ImNameSet.sort()
            ImPath = os.path.join(ImFolder, ImNameSet[0])
            self.imgname1 = ImPath
            img_name = ImPath.split('/')[-1]
            self.img_name1 = img_name
            im0 = cv2.imread(ImPath)
            width = im0.shape[1]
            height = im0.shape[0]
            width_new = 500
            height_new = 700
            if width / height >= width_new / height_new:
                show = cv2.resize(im0, (width_new, int(height * width_new / width)))
            else:
                show = cv2.resize(im0, (int(width * height_new / height), height_new))
            im0 = cv2.cvtColor(show, cv2.COLOR_RGB2BGR)
            showImage = QtGui.QImage(im0, im0.shape[1], im0.shape[0], 3 * im0.shape[1], QtGui.QImage.Format_RGB888)
            self.label1.setPixmap(QtGui.QPixmap.fromImage(showImage))
            self.Test_score()

            self.ImFolder=ImFolder
            self.ImNameSet=ImNameSet
            self.CurImId=0

        else:
            print('请重新选择文件夹')

    def NextImBntClicked(self):
        ImFolder = self.ImFolder
        ImNameSet = self.ImNameSet
        CurImId = self.CurImId
        ImNum = len(ImNameSet)
        if CurImId < ImNum - 1:  # 不可循环看图
            ImPath = os.path.join(ImFolder, ImNameSet[CurImId + 1])
            self.imgname1 = ImPath
            img_name = ImPath.split('/')[-1]
            self.img_name1 = img_name
            im0 = cv2.imread(ImPath)
            width = im0.shape[1]
            height = im0.shape[0]
            width_new = 500
            height_new = 700
            if width / height >= width_new / height_new:
                show = cv2.resize(im0, (width_new, int(height * width_new / width)))
            else:
                show = cv2.resize(im0, (int(width * height_new / height), height_new))
            im0 = cv2.cvtColor(show, cv2.COLOR_RGB2BGR)
            showImage = QtGui.QImage(im0, im0.shape[1], im0.shape[0], 3 * im0.shape[1], QtGui.QImage.Format_RGB888)
            self.label1.setPixmap(QtGui.QPixmap.fromImage(showImage))
            self.Test_score()
            self.CurImId = CurImId + 1

    def PreImBntClicked(self):
        ImFolder = self.ImFolder
        ImNameSet = self.ImNameSet
        CurImId = self.CurImId
        ImNum = len(ImNameSet)
        if CurImId > 0:  # 第一张图片没有前一张
            ImPath = os.path.join(ImFolder, ImNameSet[CurImId - 1])
            self.imgname1 = ImPath
            img_name = ImPath.split('/')[-1]
            self.img_name1 = img_name
            im0 = cv2.imread(ImPath)
            width = im0.shape[1]
            height = im0.shape[0]
            width_new = 500
            height_new = 700
            if width / height >= width_new / height_new:
                show = cv2.resize(im0, (width_new, int(height * width_new / width)))
            else:
                show = cv2.resize(im0, (int(width * height_new / height), height_new))
            im0 = cv2.cvtColor(show, cv2.COLOR_RGB2BGR)
            showImage = QtGui.QImage(im0, im0.shape[1], im0.shape[0], 3 * im0.shape[1], QtGui.QImage.Format_RGB888)
            self.label1.setPixmap(QtGui.QPixmap.fromImage(showImage))
            self.Test_score()
            self.CurImId = CurImId - 1

        if self.CurImId < 0:
            self.CurImId = 0

    def close_app(self):
        app = QApplication.instance()
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # apply_stylesheet(app,theme='light_teal.xml',invert_secondary=True)
    splash = QSplashScreen(QPixmap(".\\data\\source_image\\logo.png"))
    splash.setFont(QFont('Microsoft YaHei UI', 12))
    splash.show()
    splash.showMessage("程序初始化中... 0%", QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom, QtCore.Qt.black)
    time.sleep(0.3)
    splash.showMessage("正在加载模型配置文件...60%", QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom, QtCore.Qt.black)
    splash.showMessage("正在加载模型配置文件...100%", QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom, QtCore.Qt.black)
    ui_p = picture()
    ui_p.show()

    splash.close()
    sys.exit(app.exec_())


