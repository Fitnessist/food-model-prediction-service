from sqlalchemy import Column, String, Integer
from app.infrastructure.database import Base, get_db
from functools import lru_cache

class Food(Base):
    __tablename__ = 'foods'

    id = Column(String(40), primary_key=True)
    food_name = Column(String(100), nullable=False)
    calories_per_100gr = Column(Integer())
    image_url = Column(String(255), nullable=False, unique=True)

    def __init__(self, id, food_name, calories_per_100gr, image_url):
        self.id = id
        self.food_name = food_name
        self.calories_per_100gr = calories_per_100gr
        self.image_url = image_url
    

    @staticmethod
    @lru_cache(maxsize=None)
    def get_food_list():
        with get_db() as db:
            foods = db.query(Food).order_by(Food.food_name).all()
            food_list = []

            for food in foods:
                food_entry = {
                    'id': food.id,
                    'food_name': food.food_name,
                    'calories_per_100gr': food.calories_per_100gr,
                    'image_url': food.image_url
                }
                food_list.append(food_entry)

            return food_list
