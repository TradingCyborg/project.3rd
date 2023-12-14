from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Car(Base):
    __tablename__ = 'your_table_name'  # Replace 'your_table_name' with the actual table name

    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)

    @property
    def novel_author(self):
        return f"{self.title} by {self.author}"

class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column("family_name", String)  # Use a column name that is different from the attribute name

class Review(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    content = Column(String)
    star_rating = Column(Integer)
    novel_id =  Column(Integer, Foreign('novels.id'))
    customer_id = Column(Integer, Foreign('customer.id'))
    novel = relationship("Novel", backref="reviews")
    customer =
    def __init__(self, make, model):
        self.make = make
        self.model = model

# Example of how to use the class to interact with the database

# Create an SQLite in-memory database
engine = create_engine('sqlite:///:memory:')

# Create the table in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Create a new car instance
new_car = Car(make='Toyota', model='Camry')

# Add the car to the session and commit the changes to the database
session.add(new_car)
session.commit()

# Query the database to retrieve the car
retrieved_car = session.query(Car).filter_by(make='Toyota').first()

# Print the retrieved car's attributes
print(f"ID: {retrieved_car.id}, Make: {retrieved_car.make}, Model: {retrieved_car.model}")
