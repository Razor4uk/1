class Computergame:
    def __init__(self, name, developer, year):
        self.name = name
        self.developer = developer
        self.year = year

    def description_of_game(self):
        return f"Игра: {self.name}, Разработчик: {self.developer}, Год выпуска: {self.year}"


game = Computergame("Fortnite", "Epick games", 2017)
print(game.description_of_game())
