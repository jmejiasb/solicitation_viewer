from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def _createContactsTable():
    createTableQuery = QSqlQuery()
    return createTableQuery.exec(
        """
        CREATE TABLE IF NOT EXISTS Solicitation (
        IdSolicitation INTEGER PRIMARY KEY UNIQUE NOT NULL,
        Name VARCHAR(40) NOT NULL,
        SBR? VARCHAR(10),
        Submission Method VARCHAR(10) NOT NULL,
        ClosingDate DATE NOT NULL,
        PlaceOfDelivery VARCHAR(40) NOT NULL,
        TimeOfDelivery DATE NOT NULL
        Issuing Agency 
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
            f"DB Error: {connection.lastError().text()}"
        )

        return False
    
    return True