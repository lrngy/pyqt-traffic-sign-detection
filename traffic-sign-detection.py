import cv2
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QTimer, Qt, QSize
from PyQt6.QtGui import QImage, QPixmap
import random
from ultralytics import YOLOv10
from PyQt6.QtWidgets import QFileDialog

class Ui_MainWindow(object):
    yolo = YOLOv10('/home/long/Documents/file weights/bestm.pt')

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1119, 595)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_title = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_title.sizePolicy().hasHeightForWidth())
        self.lbl_title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")
        self.verticalLayout.addWidget(self.lbl_title)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.lbl_showmedia = QtWidgets.QLabel(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_showmedia.sizePolicy().hasHeightForWidth())
        self.lbl_showmedia.setSizePolicy(sizePolicy)
        self.lbl_showmedia.setText("")
        self.lbl_showmedia.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_showmedia.setObjectName("lbl_image")
        self.verticalLayout.addWidget(self.lbl_showmedia)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_opencamera = QtWidgets.QPushButton(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_opencamera.sizePolicy().hasHeightForWidth())
        self.btn_opencamera.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_opencamera.setFont(font)
        self.btn_opencamera.setObjectName("btn_opencamera")
        self.verticalLayout_2.addWidget(self.btn_opencamera)
        self.btn_closecamera = QtWidgets.QPushButton(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_closecamera.sizePolicy().hasHeightForWidth())
        self.btn_closecamera.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_closecamera.setFont(font)
        self.btn_closecamera.setObjectName("btn_closecamera")
        self.verticalLayout_2.addWidget(self.btn_closecamera)
        self.btn_select_image = QtWidgets.QPushButton(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_select_image.sizePolicy().hasHeightForWidth())
        self.btn_select_image.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_select_image.setFont(font)
        self.btn_select_image.setObjectName("btn_select_image")
        self.verticalLayout_2.addWidget(self.btn_select_image)
        self.btn_save_image = QtWidgets.QPushButton(parent=self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save_image.sizePolicy().hasHeightForWidth())
        self.btn_save_image.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btn_save_image.setFont(font)
        self.btn_save_image.setObjectName("btn_save_image")
        self.verticalLayout_2.addWidget(self.btn_save_image)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.horizontalLayout.setStretch(0, 4)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1119, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.postSetupUi()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_title.setText(_translate("MainWindow", "Nhận dạng biển báo giao thông"))
        self.groupBox.setTitle(_translate("MainWindow", "Thao tác"))
        self.btn_opencamera.setText(_translate("MainWindow", "Mở camera"))
        self.btn_closecamera.setText(_translate("MainWindow", "Tắt camera"))
        self.btn_select_image.setText(_translate("MainWindow", "Chọn ảnh"))
        self.btn_save_image.setText(_translate("MainWindow", "Lưu ảnh"))

    def postSetupUi(self):
        self.cap = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.class_colors = {}
        self.btn_opencamera.clicked.connect(self.start_video)
        self.btn_closecamera.clicked.connect(self.stop_video)
        self.btn_select_image.clicked.connect(self.select_image)
        self.btn_save_image.clicked.connect(self.save_image)

    def start_video(self):
        if self.cap is None:  # Check if the camera needs to be reinitialized
            self.cap = cv2.VideoCapture(0)
        self.timer.start(30)  # Adjust the interval as needed
        self.btn_select_image.setEnabled(False) 
        self.btn_save_image.setEnabled(False)  # Disable save button while camera is active

    def stop_video(self):
        self.timer.stop()
        if self.cap is not None:
            self.cap.release()
            self.cap = None 
        self.lbl_showmedia.clear()
        self.btn_select_image.setEnabled(True)
        self.btn_save_image.setEnabled(True)  # Re-enable save button

    def generate_random_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            self.predict(frame)

    def predict(self, frame):
        results = self.yolo.track(frame, stream=True, verbose=False)
        detected = False
        detection_info = []

        for result in results:
            classes_names = result.names
            for box in result.boxes:
                if box.conf[0] > 0.25:
                    detected = True
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    cls_id = int(box.cls[0])

                    if cls_id not in self.class_colors:
                        self.class_colors[cls_id] = self.generate_random_color()
                    color = self.class_colors[cls_id]
                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                    label = f"{classes_names[cls_id]}: {box.conf[0]:.2f}"

                    bbox_height = y2 - y1

                    font_scale = 0.6 * (frame.shape[0] / 480)
                    thickness = int(2 * (frame.shape[0] / 480))
                    ((w, h), _) = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, font_scale, thickness)

                    label_x = x1
                    label_y = y1 - 5

                    if x1 + w > frame.shape[1]:  
                        label_x = x1 - (x1 + w - frame.shape[1])  
                    if y1 - 20 < 0:  
                        label_y = y1 + bbox_height + 20  

                    cv2.rectangle(frame, (label_x, label_y - 20), (label_x + w, label_y), color, -1)

                    cv2.putText(frame, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 0, 0), 3)

                    cv2.putText(frame, label, (label_x, label_y), cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), thickness)
                    detection_info.append({
                        "class": classes_names[cls_id],
                        "confidence": box.conf[0],
                        "bbox": (x1, y1, x2, y2),
                    })
            if detected:
                for info in detection_info:
                    print(f"{info['class']}: {info['confidence']:.2f} {info['bbox']}")

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = image.shape
            step = channel * width
            qImg = QImage(image.data, width, height, step, QImage.Format.Format_RGB888)
            self.lbl_showmedia.setPixmap(QPixmap.fromImage(qImg))
            self.current_image = image  # Save the current image for saving

    def select_image(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Chọn ảnh", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if file_name:
            self.process_image(file_name)

    def process_image(self, file_path):
        frame = cv2.imread(file_path)
        max_label_width = self.lbl_showmedia.width()
        max_label_height = self.lbl_showmedia.height()
        scale = min(max_label_width / frame.shape[1], max_label_height / frame.shape[0])
        new_size = (int(frame.shape[1] * scale), int(frame.shape[0] * scale))
        frame = cv2.resize(frame, new_size, interpolation=cv2.INTER_AREA)
        self.predict(frame)

    def save_image(self):
        if hasattr(self, 'current_image') and self.current_image is not None:
            file_name, _ = QFileDialog.getSaveFileName(None, "Lưu ảnh", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
            if file_name:
                if not file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                    file_name += '.jpg' 
                cv2.imwrite(file_name, cv2.cvtColor(self.current_image, cv2.COLOR_RGB2BGR))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
