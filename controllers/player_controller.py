p_controller_list = []


class PController:
    def __init__(self):
        self.lastname = ""
        self.firstname = ""
        self.birth = ""
        self.gender = ""
        self.score = 0

    def add_player(self):
        # Asking players data
        self.lastname = input("Enter the player's last name : ")
        self.firstname = input(" Enter the player's first name : ")
        self.birth = input("Enter the player's date of birth : ")
        self.gender = input("Enter player's gender : ")
        self.score = input("Enter player ranking : ")

        # Converting the character string to integer
        self.score = int(self.score)

        # Adding a player to the database
        p_controller_list.append(self.lastname)
        p_controller_list.append(self.firstname)
        p_controller_list.append(self.birth)
        p_controller_list.append(self.gender)
        p_controller_list.append(self.score)

        return self


# Creating an object of the Player class
player = PController()
print(p_controller_list)


