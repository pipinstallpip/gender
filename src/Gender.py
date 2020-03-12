import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, Query
from data.Mapping import Name, Country

DB_NAME = 'Gender.db'


class Gender:

    MALE = 0
    FEMALE = 1

    def __init__(self):
        self.engine = db.create_engine('sqlite:///data/%s' % DB_NAME)
        self.session = sessionmaker(bind=self.engine)
        self.get = self.session()

    def __count(self, name: str, gender: int) -> int:
        return self.get.query(Name).filter(Name.value == name).filter(Name.gender == gender).count() > 0

    def __is(self, name: str, gender: int) -> bool:
        return self.__count(name, gender) > 0

    def __isnationality(self, name: str, country_id: int) -> bool:
        return self.get.query(Name).join(Country).\
                   filter(Name.value == name).filter(Country.id == country_id).count() > 0

    def __getnamesfromgender(self, gender: int) -> Query:
        return self.get.query(Name).filter(Name.gender == gender)

    # start gender
    def isfemale(self, name: str) -> bool:
        return self.__is(name, self.FEMALE)

    def ismale(self, name: str) -> bool:
        return self.__is(name, self.MALE)

    def isunisex(self, name: str) -> bool:
        return self.ismale(name) and self.isfemale(name)
    # end gender

    # start nationality
    def isenglish(self, name: str) -> bool:
        return self.__isnationality(name, 1)

    def isgerman(self, name: str) -> bool:
        return self.__isnationality(name, 2)

    def isfrench(self, name: str) -> bool:
        return self.__isnationality(name, 3)

    def isdutch(self, name: str) -> bool:
        return self.__isnationality(name, 4)

    def isspanish(self, name: str) -> bool:
        return self.__isnationality(name, 5)

    def isgreek(self, name: str) -> bool:
        return self.__isnationality(name, 6)

    def isportoguese(self, name: str) -> bool:
        return self.__isnationality(name, 7)

    def isicelandic(self, name: str) -> bool:
        return self.__isnationality(name, 8)

    def isswedish(self, name: str) -> bool:
        return self.__isnationality(name, 9)

    def isitalian(self, name: str) -> bool:
        return self.__isnationality(name, 10)

    def isafrican(self, name: str) -> bool:
        return self.__isnationality(name, 11)

    def isargentine(self, name: str) -> bool:
        return self.__isnationality(name, 12)

    def isturkish(self, name: str) -> bool:
        return self.__isnationality(name, 13)

    def isjapanese(self, name: str) -> bool:
        return self.__isnationality(name, 14)
    # end nationality

    def getfemalenames(self) -> list:
        return self.__getnamesfromgender(self.FEMALE).all()

    def getmalenames(self) -> list:
        return self.__getnamesfromgender(self.MALE).all()

    def getcountries(self, name: str) -> list:
        return self.get.query(Name.country_id).join(Country).filter(Name.value == name).all()
