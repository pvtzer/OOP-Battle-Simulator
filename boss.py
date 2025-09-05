import random
from enemy import Enemy
class Basilisk(Enemy):
    def stun(self):
        print("The Basilisk stares at you, you are stunned and took ")
        return random.randint(1, 50)
