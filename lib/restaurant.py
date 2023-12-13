from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    # Relationship to Review
    reviews = relationship('Review', back_populates='restaurant')

    @classmethod
    def fanciest(cls, session):
        # Return the restaurant instance with the highest price
        return session.query(cls).order_by(cls.price.desc()).first()

    def all_reviews(self):
        # Return a list of strings with all reviews for this restaurant
        reviews_strings = [
            f"Review for {self.name} by {review.customer.full_name()}: {review.star_rating} stars."
            for review in self.reviews
        ]
        return reviews_strings