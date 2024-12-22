from PyQt5.QtWidgets import *
from pip._internal import main

import ii

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

Play_Btn.cliked.connect(ii.game)

window.setLayout(main_Line)
window.show()
app.exec()