# This is the file that is used for the rounds


class RModel:
    """Class of the round model"""

    def __init__(self, r_name: str, r_start_datetime: str, r_end_datetime: str):
        """Init of the round model"""
        self.r_name = r_name
        self.r_start_datetime = r_start_datetime
        self.r_end_datetime = r_end_datetime
        self.r_matches = []

    def r_get_pairing(self, r_player_1, r_player_2):
        """Create a match pairing tuple from player_1 and player_2 and append it to the matches list"""
        match = (
            f"{r_player_1['p_lastname']}, {r_player_1['p_firstname']}",
            r_player_1["p_rank"],
            r_player_1["p_score"],
            f"{r_player_2['p_lastname']}, {r_player_2['p_firstname']}",
            r_player_2["p_rank"],
            r_player_2["p_score"]
        )
        self.r_matches.append(match)

    def r_set_the_round(self):
        """Return round info as list, including the matches"""
        return [
            self.r_name,
            self.r_start_datetime,
            self.r_end_datetime,
            self.r_matches
        ]
