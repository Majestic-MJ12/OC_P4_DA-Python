from controllers.player_controller import player


class PView:

    # Player data display
    print("Last name :", player.last_name)
    print("First name :", player.first_name)
    print("Birth :", player.birth_date)
    print("Gender :", player.gender)
    print("Ranking :", player.ranking)


PView()
