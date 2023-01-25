# This is the file that is used for the tournaments
# Import what is needed
from tinydb import TinyDB


class TModel:
    """Class of the tournament model"""

    def __init__(self, t_id: int, t_name: str, t_location: str, t_start_date: str,
                 t_end_date: str, t_description: str, t_time_control: str,
                 t_current_round: int, t_players: list, t_rounds: list, t_rounds_total=4):
        """Init of the tournament model"""
        self.t_id = t_id
        self.t_name = t_name
        self.t_location = t_location
        self.t_start_date = t_start_date
        self.t_end_date = t_end_date
        self.t_description = t_description
        self.t_time_control = t_time_control
        self.t_current_round = t_current_round
        self.t_rounds_total = t_rounds_total
        self.t_players = t_players
        self.t_rounds = t_rounds

        self.t_tournament_database = TinyDB('DB-data/tournaments.json')

    def t_serialize_tournament(self):
        """Convert the tournament object to a dictionary"""
        return {
            "t_id": self.t_id,
            "t_name": self.t_name,
            "t_location": self.t_location,
            "t_start_date": self.t_start_date,
            "t_end_date": self.t_end_date,
            "t_description": self.t_description,
            "t_time_control": self.t_time_control,
            "t_current_round": self.t_current_round,
            "t_rounds_total": self.t_rounds_total,
            "t_players": self.t_players,
            "t_rounds": self.t_rounds,
        }

    @staticmethod
    def t_load_tournament_db():
        """Load tournament database and return as a list"""
        t_tournament_database = TinyDB('DB-data/tournaments.json')
        t_tournament_database.all()
        t_tournaments_list = []
        for item in t_tournament_database:
            t_tournaments_list.append(item)
        return t_tournaments_list

    def t_sort_players_by_rank(self):
        """Sort players by rank in ascending order"""
        self.t_players = sorted(self.t_players, key=lambda x: x.get('p_rank'))

    def t_sort_players_by_score(self):
        """Sort players by score in descending order"""
        self.t_players = sorted(self.t_players, key=lambda x: x.get('p_score'), reverse=True)

    def t_split_the_players(self):
        """Split player in 2 halves (top and bottom players)"""
        t_half = len(self.t_players) // 2
        return self.t_players[:t_half], self.t_players[t_half:]

    def t_merge_the_players(self, t_top_players, t_bottom_players):
        """Merge top and bottom players in order of matches"""
        t_merged_players = []
        for i in range(len(self.t_players) // 2):
            t_merged_players.append(t_top_players[i])
            t_merged_players.append(t_bottom_players[i])

        self.t_players = t_merged_players

    def t_save_tournament_db(self):
        """Save new tournament to database
        Set tournament ID as document ID
        """
        t_db = self.t_tournament_database
        self.t_id = t_db.insert(self.t_serialize_tournament())
        t_db.update({'t_id': self.t_id}, doc_ids=[self.t_id])

    def t_update_tournament_db(self):
        """Update tournament info (after each round) in database"""
        db = self.t_tournament_database
        db.update({'t_rounds': self.t_rounds}, doc_ids=[self.t_id])
        db.update({'t_players': self.t_players}, doc_ids=[self.t_id])
        db.update({'t_current_round': self.t_current_round}, doc_ids=[self.t_id])

    def t_update_the_timer(self, timer, info):
        """Update start or end timer of tournament"""
        db = self.t_tournament_database
        db.update({info: timer}, doc_ids=[self.t_id])
