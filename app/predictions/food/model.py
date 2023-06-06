from sqlalchemy import Column, String
from app.infrastructure.database import Base, get_db

class Food(Base):
    __tablename__ = 'foods'

    id = Column(String(40), primary_key=True)
    food_name = Column(String(100), nullable=False)
    image_url = Column(String(255), nullable=False, unique=True)

    def __init__(self, id, food_name, image_url):
        self.id = id
        self.food_name = food_name
        self.image_url = image_url
    

    @staticmethod
    def get_food_list():
        with get_db() as db:
            foods = db.query(Food).all()
            food_list = []

            for food in foods:
                food_entry = {
                    'id': food.id,
                    'food_name': food.food_name,
                    'image_url': food.image_url
                }
                food_list.append(food_entry)

            return food_list
