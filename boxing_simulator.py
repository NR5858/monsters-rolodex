import random
import math


class Boxer:

    def __init__(self, name, height, weight, health, stamina, chin, luck, speed, strength, defense):
        self._name = name
        self._height = height
        self._weight = weight
        self._health = health
        self._stamina = stamina
        self._chin = chin
        self._luck = luck
        self._speed = speed
        self._strength = strength
        self._defense = defense

    def __str__(self):
        print("Name: {}".format(self._name))
        print("Height: {} in".format(self._height))
        print("Weight: {}lbs".format(self._weight))
        print("Stamina: {}/100".format(self._stamina))
        print("Chin: {}/100".format(self._chin))
        print("Luck: {}/100".format(self._luck))
        print("Speed: {}/100".format(self._speed))
        print("Strength: {}/100".format(self._strength))
        print("Defense: {}/100".format(self._defense))

    @property
    def get_health(self):
        return self._health

    @property
    def get_name(self):
        return self._name

    def set_health(self, new_health_amt):
        self._health -= new_health_amt

    def jab(self):
        attack_amount = (self._strength + self._speed) / 3 * random.random()
        return attack_amount

    def left_hook(self):
        attack_amount = self._strength / 2 * random.random()
        return attack_amount

    def right_hook(self):
        attack_amount = self._strength / 2 * random.random()
        return attack_amount

    def left_uppercut(self):
        attack_amount = self._strength / 2 * random.random()
        return attack_amount

    def right_uppercut(self):
        attack_amount = self._strength / 2 * random.random()
        return attack_amount

    def block(self):
        block_amount = (self._defense + self._speed) / 3 * random.random()
        return block_amount

    def slip(self):
        pass


class Fight:

    def start_fight(self, boxer_a, boxer_b):
        while True:
            if self.get_attack_result(boxer_a, boxer_b) == "Game Over":
                print("Game Over for {}".format(boxer_b))
                break
            if self.get_attack_result(boxer_b, boxer_a) == "Game Over":
                print("Game Over for {}".format(boxer_a))
                break

    @staticmethod
    def get_attack_result(boxer_one, boxer_two):
        boxer_one_jab_amt = boxer_one.jab()
        boxer_two_block_amt = boxer_two.block()
        boxer_two_dmg_amt = math.ceil(boxer_one_jab_amt - boxer_two_block_amt)
        boxer_two.set_health(boxer_two.get_health() - boxer_two_dmg_amt)

        print("{} jabs {} and deals {} damage".format(boxer_one.get_name(), boxer_two.get_name(),
                                                      boxer_two_dmg_amt))
        print("{} is down to {} health".format(boxer_two.get_name(), boxer_two.get_health()))

        if boxer_two.get_health() <= 0:
            print("{} has been KO'd! {} has won".format(boxer_two.get_name(), boxer_one.get_name()))
            return "Game Over"
        else:
            return "\n"


def main():
    