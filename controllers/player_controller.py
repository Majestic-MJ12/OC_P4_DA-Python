class PController:
    def __init__(self):
        # Asking players data
        self.lastname = input("Enter the player's last name : ")
        self.firstname = input("Enter the player's first name : ")
        self.birth = input("Enter the player's date of birth : ")
        self.gender = input("Enter player's gender : ")
        self.score = input("Enter player ranking : ")

    def add_player_data(self):
        self.lastname = input("What's the last name of the player: ")
        self.firstname = input("What's the first name of the player: ")
        self.birth = input("What's the birth date of the player: ")
        self.gender = input("What's the gender of the player :")
        self.score = input("What's the score")
# Creating an object of the Player class


player_controller = PController()


