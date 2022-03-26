import pygame

from color import Color

class App:
    def __init__(self):
        pygame.init()
        
        # Window config
        self.WIDTH = 600
        self.HEIGHT = 500
        self.TITLE = "Fortuna"
        self.icon_path = "ico.png"
        
        # Game config
        self.running = True
        self.FPS = 60
        self.clock = pygame.time.Clock()
        
        #run methods
        self.set_window()
        
    def create_sprites(self):
        # circle
        self.radius = 200
        self.circle = pygame.Circle()
        
    def set_window(self):
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        icon = pygame.image.load(self.icon_path)
        
        pygame.display.set_caption(self.TITLE)
        pygame.display.set_icon(icon)
        
    def draw(self):
        # background
        self.screen.fill(Color.BACKGROUND)
        
        # circle
        
        
    def start(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
            self.draw()
            pygame.display.flip()
                    
if __name__ == '__main__':
    app = App()
    app.start()
        