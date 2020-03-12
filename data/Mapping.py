from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine

Base = declarative_base()

DB_NAME = 'Gender.db'


class Country(Base):
    __tablename__ = 'country'

    id = Column(Integer, primary_key=True)
    value = Column(String(30))


class Name(Base):
    __tablename__ = 'name'

    id = Column(Integer, primary_key=True)
    value = Column(String(30))
    gender = Column(Integer)
    country_id = Column(Integer, ForeignKey('country.id'))

    def __repr__(self):
        return self.value


if __name__ == "__main__":
    engine = create_engine('sqlite:///%s' % DB_NAME, echo=True)
    Base.metadata.create_all(engine)

    with engine.connect() as con:
        countries = open('sql/countries.sql', 'r').readlines()
        names = open('sql/names.sql', 'r').readlines()

        for country in countries:
            con.execute(country)

        for name in names:
            con.execute(name)

