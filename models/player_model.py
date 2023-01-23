# the model for the players
from tinydb import TinyDB


class PModel:
    def __init__(self, id_player, lastname, firstname, birth, gender, score, rank):
        """init of what's going to be stored"""
        self.id_player = id_player
        self.lastname = lastname
        self.firstname = firstname
        self.birth = birth
        self.gender = gender
        self.score = score
        self.rank = rank

        self.player_db = TinyDB('database/players.json')

    def serialize_player(self):
        return {
            "id_player": self.id_player,
            "lastname": self.lastname,
            "firstname": self.firstname,
            "birth": self.birth,
            "gender": self.birth,
            "score": self.score,
            "rank": self.rank
        }

    def save_player_db(self):
        """Save new player to database
        Set player ID as document ID
        """
        players_db = self.player_db
        self.id_player = players_db.insert(self.serialize_player())
        players_db.update({'id': self.id_player}, doc_ids=[self.id_player])

    def update_player_db(self, info, option):
        """Update player info (from user input) in database
        @param info: user input (str, or int inf "rank")
        @param option: update info category
        """
        db = self.player_db
        if option == "rank":
            db.update({option: int(info)}, doc_ids=[self.id_player])
        else:
            db.update({option: info}, doc_ids=[self.id_player])

    @staticmethod
    def load_player_db():
        """Load player database
        @return: list of players
        """
        players_db = TinyDB('database/players.json')
        players_db.all()
        players = []
        for item in players_db:
            players.append(item)

        return players
