from PyQt5.QtWidgets import *
from pip._internal import main

import ii
import shop13

app = QApplication([])
window = QWidget()




Play_Btn = QPushButton("грати")
seeting_Btn = QPushButton("налаштування")
level_Btn = QPushButton("рівні")
shop_Btn = QPushButton("магазин")

main_Line = QHBoxLayout()
main_Line.addWidget(Play_Btn)
main_Line.addWidget(seeting_Btn)
main_Line.addWidget(level_Btn)
main_Line.addWidget(shop_Btn)

Play_Btn.clicked.connect(ii.game)
shop_Btn.clicked.connect(shop13.open_shop)


window.setLayout(main_Line)
window.show()
app.exec()