from PyQt5.QtCore import Qt
from PyQt5.QtSql import QSqlTableModel

class SolicitationModel:
    def __init__(self):
        self.model = self._createModel(self)

    @staticmethod
    def _createModel(self):
        tableModel = QSqlTableModel()
        tableModel.setTable("SOLICITATION")
        tableModel.setEditStrategy(QSqlTableModel.OnFieldChange)
        tableModel.select()
        headers = (
            "IdSolicitation",
            "Name",
            "SBR?",
            "Submission Method",
            "Closing Date"  ,
            "Place Of Delivery",
            "Time Of Delivery",  
            "Issuing Agency" ,
            "PoC Name",
            "PoC Email",
            "PoC Phone",
            "Comments"
        )
        for columnIndex, header in enumerate(headers):
            tableModel.setHeaderData(columnIndex, Qt.Horizontal, header)
        
        return tableModel
    
    def addSolicitation(self, data):
        print(data)
        rows = self.model.rowCount()
        self.model.insertRows(rows, 1)
        for column, field in enumerate(data):
            print(column)
            self.model.setData(self.model.index(rows, column), field)
        self.model.submitAll()
        self.model.select()

    def deleteSolicitation(self,row):
        self.model.removeRow(row)
        self.model.submitAll()
        self.model.select()
        