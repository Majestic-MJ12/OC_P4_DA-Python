# This is the file that is used for the players
# Import what is needed
from tinydb import TinyDB


class PModel:
    """Class of the player model"""

    def __init__(self, p_id: int, last_name: str, first_name: str, birthday: str, gender: str, rank: int):
        """Init of the player model"""
        self.p_id = p_id
        self.last_name = last_name
        self.first_name = first_name
        self.birthday = birthday
        self.gender = gender
        self.rank = rank
        self.score = 0.0
        self.opponents = []

        self.player_database = TinyDB('DB-data/players.json')

    @staticmethod
    def load_player_db():
        """Retrieve all players from the database and return as a list. """
        players_database = TinyDB('DB-data/players.json')
        players_database.all()
        players = []
        for item in players_database:
            players.append(item)
        return players

    def serialize_player(self):
        """Convert the player object to a dictionary"""
        return {
            "id": self.p_id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "date_of_birth": self.birthday,
            "gender": self.gender,
            "rank": self.rank,
            "score": self.score,
            "opponents": self.opponents
        }

    def save_player_db(self):
        """Insert the player's information to the database and set the player's ID as the document ID"""
        players_database = self.player_database
        self.p_id = players_database.insert(self.serialize_player())
        players_database.update({'id': self.p_id}, doc_ids=[self.p_id])

    def update_player_db(self, info, option):
        """Update player information in the database"""
        db = self.player_database
        if option == "rank":
            db.update({option: int(info)}, doc_ids=[self.p_id])
        else:
            db.update({option: info}, doc_ids=[self.p_id])
