import pygame, simpleGE
import random


gameIcon = pygame.image.load("tre.png")
pygame.display.set_icon(gameIcon)

class Character(simpleGE.BasicSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("tree.png")
        self.setSize(170, 170)
        self.moveSpeed = 5
        self.y = 400
        
    def checkEvents(self):
        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.x +=self.moveSpeed
        if self.scene.isKeyPressed(pygame.K_DOWN):
            self.y += self.moveSpeed
        if self.scene.isKeyPressed(pygame.K_UP):
            self.y -= self.moveSpeed
            
class Water(simpleGE.BasicSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("wa.png")
        self.setSize(60,60)
        self.waterSound = pygame.mixer.Sound("waterSound.flac")
        self.reset()
    
    def reset(self):
        waterX = random.randint(0, 100)
        self.x = waterX
        self.y = 10
        self.dy = random.randint(5, 10)
    
    def checkEvents(self):
        if self.collidesWith(self.scene.char):
            self.scene.Water += 1
            self.waterSound.play()
            self.reset()
            
        if self.scene.Water == 10:
            self.setImage("niw.png")
            self.waterSound = pygame.mixer.Sound("fanfare - victory road II.mp3")
            
    def checkBounds(self):
        if self.rect.bottom > self.screen.get_height():
            self.reset()
    
class Mon(simpleGE.BasicSprite):
    def __init__ (self, scene):
        super().__init__(scene)
        self.setImage("mon.gif")
        self.setSize(60, 60)
        self.deathSound = pygame.mixer.Sound("vgdeathsound.wav")
        self.reset()
    
    def reset(self):
        monX = random.randint(0, 100)
        self.x = monX
        self.y = 10
        self.dy = random.randint(2,4)
    
    def checkEvents(self):
        if self.collidesWith(self.scene.char):
            self.scene.Water -= 2
            self.deathSound.play()
            self.reset()
        if self.scene.Water == 10:
            self.setImage("ni.png")
            self.deathSound.stop()
    
    def checkBounds(self):
        if self.rect.bottom > self.screen.get_height():
            self.reset()

class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.char = Character(self)
        pygame.display.set_caption("Save the Tree")
        self.waters = []
        for i in range (1):
            self.waters.append(Water(self))
        
        self.mons = []
        for i in range (1):
            self.mons.append(Mon(self))
            
        self.lblWater = simpleGE.Label()
        self.lblWater.text = "Water: 0"
        self.lblWater.center = (60, 60)
        self.lblWater.fgColor = (100, 93, 110)
        self.lblWater.bgColor = ("black")
        self.Water = 0
        
        self.sprites = [self.lblWater, self.char, self.waters, self.mons]
        
    
    def update(self):
        self.lblWater.text = f"Water: {self.Water}"
        
        if self.Water == 10:
            print("YOU WIN!!!")
            
def main():
    
    game = Game()
    game.start()
    print(f"final water: {game.Water}")

if __name__ == "__main__":
    main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            