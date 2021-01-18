from sqlalchemy import create_engine

print("in dao __init__")


class DatabaseConnection:
    def connectDatabase(self):
        print('in connectDatabase')
        engine = create_engine(
            'mysql+pymysql://root:rootroot@rdspython.cmiy6lo9qske.us-east-1.rds.amazonaws.com:3306/pythondb')

        return engine


databaseConnection = DatabaseConnection()
engine = databaseConnection.connectDatabase()
