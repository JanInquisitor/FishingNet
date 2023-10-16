from datetime import datetime
from fishingnet.fish.model import Fish
from fishingnet.data import db_session  # Import the SQLAlchemy session


class FishService:

    def create_fish(self, name, email, description):
        # Create a new Fish instance with some information
        fish = Fish()
        fish.name = name
        fish.email = email
        fish.created_at = datetime.utcnow()
        fish.addresses = description

        # Set other fields as needed
        fish.last_activity = datetime.utcnow()

        # Add the fish to the database
        session = db_session.create_session()
        session.add(fish)
        session.commit()

        # Refresh the fish object to avoid DetachedInstanceError
        session.refresh(fish)

        # Close the session
        session.close()

        # Return the created fish (if needed)
        return fish

    def find_fish_by_id(self, id: int):
        session = db_session.create_session()
        fish = session.query(Fish).filter(Fish.id == id).first()
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
            fish.addresses = new_info.get('addresses', fish.addresses)
            fish.social_network = new_info.get('social_network', fish.social_network)
            fish.phone_number = new_info.get('phone_number', fish.phone_number)
            fish.last_activity = new_info.get('last_activity', fish.last_activity)
            fish.last_locations = new_info.get('last_locations', fish.last_locations)
            fish.pictures = new_info.get('pictures', fish.pictures)
            fish.description = new_info.get('description', fish.description)
            fish.evidence_of_activity = new_info.get('evidence_of_activity', fish.evidence_of_activity)
            # Update other fields as needed

            session.commit()

            return fish  # Return the updated fish

        return None  # Fish not found

    def get_all_fish(self):
        session = db_session.create_session()
        fish_records = session.query(Fish).all()
        session.close()
        return fish_records

    def count_all_fish(self):
        session = db_session.create_session()

        try:
            # Query the Fish table and count the rows
            fish_count = session.query(Fish).count()
            return fish_count
        except Exception as e:
            # Handle any exceptions here, such as database errors
            print(f"Error counting fish: {str(e)}")
            return 0  # Return 0 if an error occurs
        finally:
            session.close()
