from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from restaurant import Base, Restaurant
from customer import Customer
from review import Review

engine = create_engine('sqlite:///lib/restaurants_database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()