import random

class Player():
    def __init__(self):
        self.score = 0

    def take_a_turn(self, turn_total=0):
        




class AggressivePlayer(Player):
    super()__init__(self)
    self.aggression_level = 75

    def play_again(self):
        return random.randgetbits(1)


class CautiousPlayer(Player):
    super()__init__(self)
    self.aggression_level = 25

    def play_again(self):
        return random.randgetbits(1)


class Game():
    def __init__(self):
        self.turn_limit = 7
        self.turn_count = 0

    def roll(self):
        return random.randint(1, 6)

    def player_rolls(self, player):
        player.take_a_turn(self.turn_count)
        self.turn_count += 1

    def main(self):
        player = AggressivePlayer()
        score = player.score
        while self.turn_count < self.turn_limit and score < 100:
            self.player_rolls(player)
            score += player.score
        return score
