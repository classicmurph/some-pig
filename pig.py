import random


def roll():
    return random.randint(1, 6)

class Player():
    def __init__(self):
        self.score = 0

    def take_a_turn(self, turn_total=0):
        first_roll = roll()
        if first_roll == 1:
            return self.score
        else:
            turn_total += first_roll
            if self.play_again():
                self.take_a_turn(turn_total)
            else:
                self.score += turn_total

    def play_again():
        False


class AggressivePlayer(Player):
    def __init__(self):
        super().__init__()
        self.aggression_level = 75

    def play_again(self):
        return random.getrandbits(1)


class CautiousPlayer(Player):
    def __init__(self):
        super().__init__()
        self.aggression_level = 25

    def play_again(self):
        return random.getrandbits(1)


class Game():
    def __init__(self):
        self.turn_limit = 7
        self.turn_count = 0

    def player_rolls(self, player):
        player.take_a_turn(self.turn_count)
        self.turn_count += 1

    def main(self):
        player = AggressivePlayer()
        score = player.score
        while self.turn_count < self.turn_limit and score < 100:
            self.player_rolls(player)
            score += player.score
        print(score)


if __name__ == "__main__":
    game = Game()
    game.main()
