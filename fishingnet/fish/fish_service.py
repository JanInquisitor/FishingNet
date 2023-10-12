from datetime import datetime
from fishingnet.fish.FishModel import Fish
from fishingnet.data import db_session  # Import the SQLAlchemy session


class FishService:

    def create_fish(self, name='fisherman', email='example@gmail.com'):
        # Create a new Fish instance with some information
        fish = Fish()
        fish.name = name
        fish.email = email

        # Set other fields as needed
        fish.last_activity = datetime.utcnow()

        # Add the fish to the database
        # session = db_session.create_session()
        # session.add(fish)
        # session.commit()

        # Return the created fish
        return fish

    def find_fish_by_name(self, name: str):
        # Implement a method to find fish by name
        session = db_session.create_session()
        fish = session.query(Fish).filter(Fish.name == name).first()
        return fish

    def update_fish_information(self, fish_id, new_info):
        # Implement a method to update fish information
        session = db_session.create_session()
        fish = session.query(Fish).filter(Fish.id == fish_id).first()

        if fish:
            # Update the fish's information
            fish.name = new_info.get('name', fish.name)
            fish.email = new_info.get('email', fish.email)
            # Update other fields as needed

            session.commit()

            return fish  # Return the updated fish

        return None  # Fish not found
