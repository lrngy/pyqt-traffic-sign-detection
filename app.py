import sys
import cv2
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QImage, QPixmap
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget
import random
from ultralytics import YOLOv10

class VideoCaptureWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.video_label = QLabel(self)
        self.video_label.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start_video)

        layout = QVBoxLayout()
        layout.addWidget(self.video_label)
        layout.addWidget(self.start_button)
        self.setLayout(layout)

        self.cap = cv2.VideoCapture(0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

        self.yolo = YOLOv10('best-sign.pt')
        self.class_colors = {}

    def generate_random_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def start_video(self):
        self.timer.start(0)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
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
                    
                        (w, h), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 2)
                        cv2.rectangle(frame, (x1, y1 - 20), (x1 + w, y1), color, -1)
                    
                        cv2.putText(frame, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
                    
                        detection_info.append({
                            "class": classes_names[cls_id],
                            "confidence": box.conf[0],
                            "bbox": (x1, y1, x2, y2),
                        })

            if detected:
                for info in detection_info:
                    print(f"{info['class']}: {info['confidence']:.2f} {info['bbox']}")

        
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format.Format_RGB888)
            self.video_label.setPixmap(QPixmap(image))

    def closeEvent(self, event):
        self.cap.release()
        event.accept()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Real-Time Video Capture with OpenCV")
        self.setGeometry(100, 100, 800, 600)

        self.video_capture_widget = VideoCaptureWidget(self)
        self.setCentralWidget(self.video_capture_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())