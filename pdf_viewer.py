# pdf_viewer.py

import fitz
from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QPushButton, QFileDialog, QGraphicsView, \
    QGraphicsScene, QGraphicsPixmapItem, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys



class PDFViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('PDF Viewer')
        self.setGeometry(100, 100, 800, 600)

        self.scene = QGraphicsScene(self)
        self.view = QGraphicsView(self.scene)
        self.view.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        layout = QVBoxLayout()
        layout.addWidget(self.view)

        self.load_button = QPushButton('Open PDF', self)
        self.load_button.clicked.connect(self.load_pdf)
        layout.addWidget(self.load_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def load_pdf(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_name, _ = QFileDialog.getOpenFileName(self, "Open PDF File", "", "PDF Files (*.pdf);;All Files (*)", options=options)

        if file_name:
            self.display_pdf(file_name)

    def display_pdf(self, file_path):
        doc = fitz.open(file_path)
        pixmap_items = []

        for page_number in range(doc.page_count):
            page = doc.load_page(page_number)
            image = page.get_pixmap()

            pixmap_item = QGraphicsPixmapItem(QPixmap(image.get_data()))
            pixmap_items.append(pixmap_item)

        self.scene.clear()
        self.scene.setSceneRect(0, 0, self.width(), self.height())

        for i, pixmap_item in enumerate(pixmap_items):
            pixmap_item.setPos(0, i * self.height())
            self.scene.addItem(pixmap_item)

        doc.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = PDFViewer()
    viewer.show()
    sys.exit(app.exec_())
