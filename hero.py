import random

class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """
    
    def __init__(self, name):
        #TODO Set the hero's name.
        self.name = name
        self.health = 250
        self.attack_power = random.randint(10, 20)
        #TODO Set the hero's health. You might give the hero more health than a goblin.
        #TODO Set the hero's attack power. Should it be more consistent than the goblin's?
    

    def strike(self):
        return random.randint(5, self.attack_power)
        # TODO Implement the hero's attack logic. It could be stronger or more consistent than a goblin's.
    
    def receive_damage(self, damage):
        bandage = 1
        self.health -= damage
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
        # TODO Implement take_damage
        # TODO We should prevent health from going into the NEGATIVE
        if self.health <= 150:
            if bandage == 1:
                self.health == 250
                print("Bandage used")
                bandage = bandage - 1

    def moreBandages(hero, goblin):
        if hero.is_alive and (not goblin.is_alive):
            bandage = bandage + 1

                
    
    #TODO define is_alive
    def is_alive(self):
        return self.health > 0

    
