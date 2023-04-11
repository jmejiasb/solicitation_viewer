from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def _createSolicitationTable():
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS Solicitation (
        IdSolicitation TEXT PRIMARY KEY UNIQUE NOT NULL,
        Name TEXT NOT NULL,
        "SBR?" TEXT,
        SubmissionMethod TEXT NOT NULL,
        ClosingDate TEXT NOT NULL,
        PlaceOfDelivery TEXT NOT NULL,
        TimeOfDelivery TEXT NOT NULL,
        IssuingAgency TEXT,
        PoCName TEXT,
        PoCEmail TEXT,
        PocPhone TEXT,
        Comments TEXT
        )
        """
    )

def createConnection(databaseName):
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databaseName)

    if not connection.open():
        QMessageBox.warning(
            None,
            "Solicitation Viewer",
            f"DB Error: {connection.lastError().text()}",
        )

        return False
    print("connected!")
    _createSolicitationTable()
    return True