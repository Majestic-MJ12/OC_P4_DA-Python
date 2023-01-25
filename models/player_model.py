# This is the file that is used for the players
# Import what is needed
from tinydb import TinyDB


class PModel:
    """Class of the player model"""

    def __init__(self, p_id: int, p_lastname: str, p_firstname: str, p_birth: str, p_gender: str, p_rank: int):
        """Init of the player model"""
        self.p_id = p_id
        self.p_lastname = p_lastname
        self.p_firstname = p_firstname
        self.p_birth = p_birth
        self.p_gender = p_gender
        self.p_rank = p_rank
        self.p_score = 0.0
        self.p_versus = []

        self.p_player_database = TinyDB('DB-data/players.json')

    def p_serialize_player(self):
        """Convert the player object to a dictionary"""
        return {
            "p_id": self.p_id,
            "p_lastname": self.p_lastname,
            "p_firstname": self.p_firstname,
            "p_date_of_birth": self.p_birth,
            "p_gender": self.p_gender,
            "p_rank": self.p_rank,
            "p_score": self.p_score,
            "p_versus": self.p_versus
        }

    @staticmethod
    def p_load_player_db():
        """Retrieve all players from the database and return as a list. """
        p_players_database = TinyDB('DB-data/players.json')
        p_players_database.all()
        p_players = []
        for item in p_players_database:
            p_players.append(item)
        return p_players

    def p_save_player_db(self):
        """Insert the player's information to the database and set the player's ID as the document ID"""
        p_players_database = self.p_player_database
        self.p_id = p_players_database.insert(self.p_serialize_player())
        p_players_database.update({'p_id': self.p_id}, doc_ids=[self.p_id])

    def p_update_player_db(self, info, option):
        """Update player information in the database"""
        p_db = self.p_player_database
        if option == "p_rank":
            p_db.update({option: int(info)}, doc_ids=[self.p_id])
        else:
            p_db.update({option: info}, doc_ids=[self.p_id])
