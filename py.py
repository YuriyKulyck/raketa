from PyQt5.QtWidgets import *
import os
from PIL.ImageFilter import *
from PyQt5.QtGui import QPixmap, QImage
from PIL import Image

def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif  im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap

app = QApplication([])

window = QWidget()
window.resize(800, 600)
window.setWindowTitle("ІЗІ ФОТОШОП")

folderBtn = QPushButton("Папка")
leftBtn = QPushButton("Ліворуч")
rightBtn = QPushButton("праворуч")
mirrorBtn = QPushButton("дзеркало")
blurBtn = QPushButton("Розмиття")

imgLbl = QLabel("фоточка")
fileList = QListWidget()

mainLine = QHBoxLayout()
columnLeft = QVBoxLayout()
columnLeft.addWidget(folderBtn)
columnLeft.addWidget(fileList)
mainLine.addLayout(columnLeft)
columnRight = QVBoxLayout()
columnRight.addWidget(imgLbl)
line1 = QHBoxLayout()
line1.addWidget(leftBtn)
line1.addWidget(rightBtn)
line1.addWidget(mirrorBtn)
line1.addWidget(blurBtn)
columnRight.addLayout(line1)
mainLine.addLayout(columnRight)

class ImageProcessor:
    def __init__(self):
        self.folder = None
        self.filename = None
        self.image = None

    def picture_load(self):
        image_path = os.path.join(self.folder, self.filename)
        self.image = Image.open(image_path)

    def image_show(self):
        pixel = pil2pixmap(self.image)
        imgLbl.setPixmap(pixel)

    def mirror_image(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.image_show()


image_processor = ImageProcessor()

def open_directory():
    folder = QFileDialog.getExistingDirectory()
    image_processor.folder = folder
    files = os.listdir(folder)
    for file in files:
        fileList.addItem(file)

def show_chosen_image():
    image_processor.filename = fileList.currentItem().text()
    image_processor.picture_load()
    image_processor.image_show()


fileList.currentRowChanged.connect(show_chosen_image)
folderBtn.clicked.connect(open_directory)
mirrorBtn.clicked.connect(image_processor.mirror_image)

window.setLayout(mainLine)
window.show()
app.exec_()

