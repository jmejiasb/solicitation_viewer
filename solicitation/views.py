from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QMessageBox,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget
)

from .model import SolicitationModel

class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Solicitation Viewer")
        self.resize(800, 450)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.solicitationModel = SolicitationModel()
        self.setupUI()

    def setupUI(self):
        self.table = QTableView()
        self.table.setModel(self.solicitationModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()

        self.addButton = QPushButton("Add Solicitation")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Delete Solicitation")
        self.addButton.clicked.connect(self.deleteSolicitation)

        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)

    def openAddDialog(self):
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.solicitationModel.addSolicitation(dialog.data)
            self.table.resizeColumnsToContents()
    
    def deleteSolicitation(self):
        row = self.table.currentIndex().row()
        if row < 0:
            return
        
        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Are you sure you want to erase this row?",
            QMessageBox.Ok | QMessageBox.Cancel
        )

        if messageBox == QMessageBox.Ok:
            self.solicitationModel.deleteSolicitation(row)
        

class AddDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setWindowTitle("Añadir")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None

        self.setupUI()

    def setupUI(self):
        self.idField = QLineEdit()
        self.idField.setObjectName("IdSolicitation")
        self.nameField = QLineEdit()
        self.nameField.setObjectName("Name")
        self.sbrField = QLineEdit()
        self.sbrField.setObjectName("SBR?")
        self.submissionField = QLineEdit()
        self.submissionField.setObjectName("Submission Method")
        self.closingDateField = QLineEdit()
        self.closingDateField.setObjectName("Closing Date")
        self.placeDeliveryField = QLineEdit()
        self.placeDeliveryField.setObjectName("Place Of Delivery")
        self.timeDeliveryField = QLineEdit()
        self.timeDeliveryField.setObjectName("Time Of Delivery")
        self.agencyField = QLineEdit()
        self.agencyField.setObjectName("Issuing Agency")
        self.pocNameField = QLineEdit()
        self.pocNameField.setObjectName("PoC Name")
        self.pocEmailField = QLineEdit()
        self.pocEmailField.setObjectName("PoC Email")
        self.pocPhoneField = QLineEdit()
        self.pocPhoneField.setObjectName("PoC Phone")
        self.commentsField = QLineEdit()
        self.commentsField.setObjectName("Comments")
        
        layout = QFormLayout()
        layout.addRow("Id :", self.idField)
        layout.addRow("Name :", self.nameField)
        layout.addRow("SBR?",self.sbrField)
        layout.addRow("Submission Method:", self.submissionField)
        layout.addRow("Closing Date :", self.closingDateField)
        layout.addRow("Place of Delivery :", self.placeDeliveryField)
        layout.addRow("Time of Delivery :", self.timeDeliveryField)
        layout.addRow("Issuing Agency :", self.agencyField)
        layout.addRow("Person of Contact Name :", self.pocNameField)
        layout.addRow("Person of Contact Email :", self.pocEmailField)
        layout.addRow("Person of Contact Phone Number :", self.pocPhoneField)
        layout.addRow("Comments :", self.commentsField)
        self.layout.addLayout(layout)

        self.buttonsBox = QDialogButtonBox(self)
        self.buttonsBox.setOrientation(Qt.Horizontal)
        self.buttonsBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.buttonsBox.accepted.connect(self.accept)
        self.buttonsBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonsBox)

    def accept(self):
        self.data = []
        listOfFields = [
            self.idField,
            self.nameField,
            self.sbrField,
            self.submissionField,
            self.closingDateField,
            self.placeDeliveryField,
            self.timeDeliveryField,
            self.agencyField,
            self.pocNameField,
            self.pocEmailField,
            self.pocPhoneField,
            self.commentsField
        ]
        for field in listOfFields:
            if not field.text():
                QMessageBox.critical(
                    self,
                    "Error!",
                    f"Must fill a {field.objectName()}",
                )
                self.data = None
                return
            
            self.data.append(field.text())

        if not self.data:
            return
        
        super().accept()