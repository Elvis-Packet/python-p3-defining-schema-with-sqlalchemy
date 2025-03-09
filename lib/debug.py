#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db import Game, Base  # Ensure Base is imported to create tables

fake = Faker()

if __name__ == '__main__':
    engine = create_engine('sqlite:///seed_db.db')
    Base.metadata.create_all(engine)  # Ensures tables exist

    Session = sessionmaker(bind=engine)
    session = Session()

    # Creating Fake Game Data
    games = [
        Game(name=fake.company(), genre=random.choice(["Action", "RPG", "Sports", "Puzzle"]))
        for _ in range(10)
    ]
    
    session.add_all(games)
    session.commit()

    print("Database seeded successfully!")

    session.close()
