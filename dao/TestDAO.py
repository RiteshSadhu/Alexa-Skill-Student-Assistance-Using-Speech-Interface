from sqlalchemy.orm import sessionmaker
from dao import engine

Session = sessionmaker(bind=engine)
session = Session()

print("in testDAO")

class TestDAO:
    def insertTestData(self, testVO):
        print("in insert test data")
        session.add(testVO)
        session.commit()

