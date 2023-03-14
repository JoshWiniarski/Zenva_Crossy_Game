import pygame
from gameObject import GameObject
from player import Player
from enemy import Enemy

class Game:
    def __init__(self):
        self.width = 800
        self.height = 800
        self.color_white = (255,255,255)
        self.refresh_rate = 60
       
        self.game_window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        self.background = GameObject(0, 0, self.width, self.height, 'Python/PygameProject/assets/background.png')

        self.treasure = GameObject(375, 50, 50, 50, 'Python/PygameProject/assets/treasure.png')

        self.level = 1.0
        
        self.reset_map()
        
    def reset_map(self):
        self.player = Player(375, 700, 50, 50, 'Python/PygameProject/assets/player.png', 10)
        speed = 5 + (self.level * 5)
        if self.level >= 4.0:
            self.enemies = [
                Enemy(50, 500, 50, 50, 'Python/PygameProject/assets/enemy.png', speed - 3),
                Enemy(750, 300, 50, 50, 'Python/PygameProject/assets/enemy.png', speed +2),
                Enemy(0, 150, 50, 50, 'Python/PygameProject/assets/enemy.png', speed -5),
        ]
        elif self.level >= 2.0:
            self.enemies = [
                Enemy(50, 500, 50, 50, 'Python/PygameProject/assets/enemy.png', speed - 3),
                Enemy(750, 300, 50, 50, 'Python/PygameProject/assets/enemy.png', speed +2),
        ]
        else:
            self.enemies = [
                Enemy(50, 500, 50, 50, 'Python/PygameProject/assets/enemy.png', speed - 5),
        ]
        
    #Tell the system to draw in the objects
    def draw_objects(self):
        self.game_window.fill(self.color_white)
        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        # Looping through the enemies
        for enemy in self.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y))
        pygame.display.update()
        
    def move_objects(self, player_direction,):
            self.player.move(player_direction, self.height)
            for enemy in self.enemies:
                enemy.move(self.width)
        
        #Collision Detection
    def check_if_collided(self):
        for enemy in self.enemies:
            if self.detect_collision(self.player, enemy):
                self.level -= 0.5
                return True
        if self.detect_collision(self.player, self.treasure):
            self.level += 0.5
            return True
        return False
    
    def detect_collision(self, object_1, object_2):
        if object_1.y > (object_2.y + object_2.height):
            return False
        elif (object_1.y + object_1.height) < object_2.y:
            return False
        if object_1.x > (object_2.x + object_2.width):
            return False
        elif (object_1.x + object_1.width) < object_2.x:
            return False
        return True
    
        
    def run_game_loop(self):
        player_direction = 0
        
        while True:
        #handle Events 
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_direction = -1
                    elif event.key == pygame.K_DOWN: 
                        player_direction = 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction = 0
                        
            
        #execute logic
            self.move_objects(player_direction)
        
        #update display
            self.draw_objects()
            self.clock.tick(self.refresh_rate)
        
        #Detect Collision
            if self.check_if_collided():
                self.reset_map()
                
            