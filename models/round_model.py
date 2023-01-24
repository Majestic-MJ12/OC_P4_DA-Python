# This is the file that is used for the rounds


class RModel:
    """Class of the round model"""

    def __init__(self, r_name: str, start_datetime: str, end_datetime: str):
        """Init of the round model"""
        self.r_name = r_name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.matches = []

    def get_pairing(self, player_1, player_2):
        """Create a match pairing tuple from player_1 and player_2 and append it to the matches list"""
        match = (
            f"{player_1['last_name']}, {player_1['first_name']}",
            player_1["rank"],
            player_1["score"],
            f"{player_2['last_name']}, {player_2['first_name']}",
            player_2["rank"],
            player_2["score"]
        )
        self.matches.append(match)

    def set_the_round(self):
        """Return round info as list, including the matches"""
        return [
            self.r_name,
            self.start_datetime,
            self.end_datetime,
            self.matches
        ]
