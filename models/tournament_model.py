# This is the file that is used for the tournaments
# Import what is needed
from tinydb import TinyDB


class TModel:
    """Class of the tournament model"""

    def __init__(self, t_id: int, t_name: str, location: str, start_date: str,
                 end_date: str, description: str, time_control: str,
                 current_round: int, players: list, rounds: list, rounds_total=4):
        """Init of the tournament model"""
        self.t_id = t_id
        self.t_name = t_name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.time_control = time_control
        self.current_round = current_round
        self.rounds_total = rounds_total
        self.players = players
        self.rounds = rounds

        self.tournament_database = TinyDB('DB-data/tournaments.json')

    @staticmethod
    def load_tournament_db():
        """Load tournament database and return as a list"""
        tournament_database = TinyDB('DB-data/tournaments.json')
        tournament_database.all()
        tournaments_list = []
        for item in tournament_database:
            tournaments_list.append(item)
        return tournaments_list

    def serialize_tournament(self):
        """Convert the tournament object to a dictionary"""
        return {
            "id": self.t_id,
            "name": self.t_name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "time_control": self.time_control,
            "current_round": self.current_round,
            "rounds_total": self.rounds_total,
            "players": self.players,
            "rounds": self.rounds,
        }

    def sort_players_by_rank(self):
        """Sort players by rank in ascending order"""
        self.players = sorted(self.players, key=lambda x: x.get('rank'))

    def sort_players_by_score(self):
        """Sort players by score in descending order"""
        self.players = sorted(self.players, key=lambda x: x.get('score'), reverse=True)

    def split_the_players(self):
        """Split player in 2 halves (top and bottom players)"""
        half = len(self.players) // 2
        return self.players[:half], self.players[half:]

    def merge_the_players(self, top_players, bottom_players):
        """Merge top and bottom players in order of matches"""
        merged_players = []
        for i in range(len(self.players) // 2):
            merged_players.append(top_players[i])
            merged_players.append(bottom_players[i])

        self.players = merged_players

    def save_tournament_db(self):
        """Save new tournament to database
        Set tournament ID as document ID
        """
        db = self.tournament_database
        self.t_id = db.insert(self.serialize_tournament())
        db.update({'id': self.t_id}, doc_ids=[self.t_id])

    def update_tournament_db(self):
        """Update tournament info (after each round) in database"""
        db = self.tournament_database
        db.update({'rounds': self.rounds}, doc_ids=[self.t_id])
        db.update({'players': self.players}, doc_ids=[self.t_id])
        db.update({'current_round': self.current_round}, doc_ids=[self.t_id])

    def update_the_timer(self, timer, info):
        """Update start or end timer of tournament"""
        db = self.tournament_database
        db.update({info: timer}, doc_ids=[self.t_id])
