class PModel:
    def __init__(self, lastname, firstname, birth, gender, score, rank=0):
        self.lastname = lastname
        self.firstname = firstname
        self.birth = birth
        self.gender = gender
        self.score = score
        self.tournament_score = 0
        self.rank = rank
        self.played_with = []

    def __str__(self):
        return f"{self.lastname} {self.firstname} [{self.tournament_score} pts]"

    @staticmethod
    def players():
        player = []  # create an empty list to store the players

        # create 8 players using a for loop
        for i in range(8):
            player.append("Player " + str(i + 1))

        # print the list of players
        print(player)

    def win(self):
        self.score += 1

    def tie(self):
        self.score = 0.5


players = PModel()
