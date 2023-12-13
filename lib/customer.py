from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from review import Review

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    
    reviews = relationship('Review', back_populates='customer')

    def full_name(self):
        # How can we return the full name of the customer
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        # how can we return the restaurant instance with the highest star rating from this customer
        favorite_review = max(self.reviews, key=lambda x: x.star_rating, default=None)
        return favorite_review.restaurant if favorite_review else None

    def add_review(self, restaurant, rating, session):
        # how we are able to create a new review for the restaurant with the given rating
        new_review = Review(customer=self, restaurant=restaurant, star_rating=rating)
        session.add(new_review)
        session.commit()

    def delete_reviews(self, restaurant, session):
        # how we are able to remove all reviews for a specific restaurant
        reviews_to_delete = [review for review in self.reviews if review.restaurant == restaurant]
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()