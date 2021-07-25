import os
import shutil
import sys

from PyQt5.QtWidgets import QApplication, QLineEdit, QFileDialog, QWidget, QPushButton, QMessageBox, QLabel

from PyQt5.QtCore import QCoreApplication


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('alert error')


class Myapp(QWidget):
    def __init__(self):
        super().__init__()
        self.btn2 = QPushButton('정리하기', self)
        self.btn1 = QPushButton('폴더 선택', self)
        self.Ie = QLineEdit(self)
        self.Label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.Label = QLabel(self)
        self.Label.setText('PDF,MP4,PDF,ZIP 형식에 따라서 폴더를 생성후 분류합니다.')
        self.Label.move(30,30)
        self.btn1.move(250, 50)
        self.btn2.move(350, 50)
        self.Ie.resize(200, 20)
        self.Ie.move(30, 55)
        self.btn1.clicked.connect(self.OpenFolder)
        self.btn2.clicked.connect(self.Distribution)
        self.setWindowTitle('File distributor')
        self.setGeometry(300, 300, 400, 200)
        self.resize(450, 100)
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Complete', 'Are you sure to quit?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def finishEvent(self):
        reply = QMessageBox.question(self, 'Complete', '정리완료. 프로그램을 종료할까요?', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            QCoreApplication.instance().quit()

    def warningEvent(self):
        reply = QMessageBox.warning(self, '오류발생', '프로그램을 다시 시작해주세요')

    def OpenFolder(self):
        fame = QFileDialog.getExistingDirectory(self, "Searching Folder", "D:\\abc")
        if fame:
            self.Ie.setText(fame)

    def Distribution(self):
        try:
            path_file = self.Ie.text()
            file_list = os.listdir(path_file)
            os.chdir(path_file)
            # 파일들을 확장자에 따라 구별
            for file in file_list:
                if file.endswith(".mp4"):
                    createFolder("mp4")
                    path_file2 = os.path.join(path_file, file)
                    dst_path = os.path.join(os.getcwd(), 'mp4')
                    shutil.move(path_file2, dst_path)
                elif file.endswith(".pdf"):
                    createFolder("pdf")
                    path_file2 = os.path.join(path_file, file)
                    dst_path = os.path.join(os.getcwd(), "pdf")
                    shutil.move(path_file2, dst_path)
                elif file.endswith(".zip"):
                    createFolder("zip")
                    path_file2 = os.path.join(path_file, file)
                    dst_path = os.path.join(os.getcwd(), 'zip')
                    shutil.move(path_file2, dst_path)
                elif file.endswith(".xlsx"):
                    createFolder("xlsx")
                    path_file2 = os.path.join(path_file, file)
                    dst_path = os.path.join(os.getcwd(), 'xlsx')
                    shutil.move(path_file2, dst_path)
                elif file.endswith(".png"):
                    createFolder("png")
                    path_file2 = os.path.join(path_file, file)
                    dst_path = os.path.join(os.getcwd(), 'png')
                    shutil.move(path_file2, dst_path)
                elif file.endswith(".pptx"):
                    createFolder("pptx")
                    path_file2 = os.path.join(path_file, file)
                    dst_path = os.path.join(os.getcwd(), 'pptx')
                    shutil.move(path_file2, dst_path)
                elif file.endswith(".rar"):
                    createFolder("rar")
                    path_file2 = os.path.join(path_file, file)
                    dst_path = os.path.join(os.getcwd(), 'rar')
                    shutil.move(path_file2, dst_path)
                elif file.endswith(".hwp"):
                    createFolder("hwp")
                    path_file2 = os.path.join(path_file, file)
                    dst_path = os.path.join(os.getcwd(), 'hwp')
                    shutil.move(path_file2, dst_path)
                elif file.endswith(".7z"):
                    createFolder("7z")
                    path_file2 = os.path.join(path_file, file)
                    dst_path = os.path.join(os.getcwd(), '7z')
                    shutil.move(path_file2, dst_path)
                elif file.endswith(".txt"):
                    createFolder("Txt")
                    path_file2 = os.path.join(path_file, file)
                    dst_path = os.path.join(os.getcwd(), 'txt')
                    shutil.move(path_file2, dst_path)
                else:
                    if file not in ["hwp", "rar", 'mp4', 'pptx', 'png', 'pdf', 'zip', 'xlsx','Txt','7z']:
                        createFolder("Something")
                        path_file2 = os.path.join(path_file, file)
                        dst_path = os.path.join(os.getcwd(), 'Something')
                        shutil.move(path_file2, dst_path)
            self.finishEvent()

        except:
            self.warningEvent()


# GUi 생성


# 지금 다운로드 폴더에 있는 파일 리스트 불러오기


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Myapp()
    sys.exit(app.exec_())
