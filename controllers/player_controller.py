class PController:
    def __init__(self):
        # Asking players data
        self.lastname = input("Enter the player's last name : ")
        self.firstname = input("Enter the player's first name : ")
        self.birth = input("Enter the player's date of birth : ")
        self.gender = input("Enter player's gender : ")
        self.score = input("Enter player ranking : ")


player_controller = PController()


