import random

#step 1: define the weapon class
class Weapon:
    def __init__(self,name,damage,ammo_capacity):
        self.name = name
        self.damage = damage
        self.ammo_capacity = ammo_capacity
        # local variable to account for ammo remaining
        self.ammo_remaining = ammo_capacity
    
    def shoot(self):
        if self.ammo_remaining > 0:
            print(f'{self.name} fired! -{self.damage}')            
        else:
            print(f'out of ammo')
#step 2: define the base player class
class Player:
    def __init__(self,name,health):
        self.name = name
        self.health = health
        self.weapon = None
    
    def take_damage(self,damage):
        self.health -= damage
        print(f'{self.name} was hit for {damage} points. current health: {self.health}')

    def equip_weapon(self,weapon):
        self.weapon = weapon
        print(f'{self.name} equipped {weapon.name}')
    
    def shoot(self):
        if self.weapon:
            self.weapon.shoot()
        else:
            print(f'{self.name} has no weapon!')
#step 3: define the game
class FPSGame:
    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
    
    def play_round(self):
        print('new round!')
        self.player1.shoot()
        self.player2.take_damage(self.player1.weapon.damage)
        
        self.player2.shoot()
        self.player1.take_damage(self.player2.weapon.damage)
#step 4: instantiate the objects and play the game
if __name__ == "__main__":
    #create weapons
    assault_rifle = Weapon('Assault Rifle', damage=10, ammo_capacity=30)
    shotgun = Weapon('Shotgun', damage=30, ammo_capacity=8)

    #create players
    player1 = Player('Player 1', health=100)
    player2 = Player('Player 2', health=100)

    #equip weapons
    player1.equip_weapon(assault_rifle)
    player2.equip_weapon(shotgun)

    #create the game
    fps_game = FPSGame(player1,player2)
    
    #play a round
    fps_game.play_round()