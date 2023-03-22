import pygame
import random

# Inicializálja a Pygame modult
pygame.init()

# Játék ablak mérete
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Színek
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Betűtípusok
FONT_SMALL = pygame.font.Font(None, 25)
FONT_MEDIUM = pygame.font.Font(None, 50)
FONT_LARGE = pygame.font.Font(None, 80)

# Játék ablak létrehozása
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Alien Invasion")

# Játék elején megjelenő üzenet
def show_message(message, font, color):
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(text, text_rect)
    pygame.display.update()

# Ufó osztály
class UFO(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(1, 5)
    
    def update(self):
        self.rect.y += self.speed

# Lekvár osztály
class Jam(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(1, 5)
    
    def update(self):
        self.rect.y += self.speed

# Játékos osztály
class Player(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH/2
        self.rect.bottom = SCREEN_HEIGHT - 10
    
    def update(self):
        # Mozgatás a nyilakkal
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Nem mehet ki a játéktérből
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

# Játék inicializálása
def init_game():
    # Játékos létrehozása
    player_image = pygame.image.load("player.png").convert_alpha()
    player = Player(player_image)

    # UFO-k létrehozása
    ufo_images = [
        pygame.image.load("ufo1.png").convert_alpha(),
        pygame.image.load("ufo2.png").convert_alpha(),
        pygame.image.load("ufo3.png").convert_alpha()
    ]
    ufos = pygame.sprite.Group()
    for i in range(10):
        ufo_image = random.choice(ufo_images)
        ufo = UFO(ufo_image)
        ufos.add(ufo)

    # Lekvárok létrehozása
    jam_image = pygame.image.load("jam.png").convert_alpha()
   
    # create the UFO and jam jars objects
    ufo_image = pygame.image.load("ufo.png")
    jam_jar_image = pygame.image.load("jam_jar.png")
    ufo_list = []
    jam_jar_list = []

    # set up the game loop
    running = True
    lives = 3
    score = 0
    while running:
        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # get the position of the mouse click
                click_pos = pygame.mouse.get_pos()

                # check if a UFO was clicked
                for ufo in ufo_list:
                    if ufo.rect.collidepoint(click_pos):
                        # remove the UFO and add to the score
                        ufo_list.remove(ufo)
                        score += 1

                # check if a jam jar was clicked
                for jam_jar in jam_jar_list:
                    if jam_jar.rect.collidepoint(click_pos):
                        # remove the jam jar and lose a life
                        jam_jar_list.remove(jam_jar)
                        lives -= 1

        # add a new UFO or jam jar to the game randomly
        if random.random() < ufo_frequency:
            new_ufo = UFO(ufo_image)
            ufo_list.append(new_ufo)
        if random.random() < jam_jar_frequency:
            new_jam_jar = JamJar(jam_jar_image)
            jam_jar_list.append(new_jam_jar)

        # update the game objects and check for collisions
        for ufo in ufo_list:
            ufo.update()
            if ufo.rect.bottom >= SCREEN_HEIGHT:
                # remove the UFO and lose a life
                ufo_list.remove(ufo)
                lives -= 1

        for jam_jar in jam_jar_list:
            jam_jar.update()
            if jam_jar.rect.bottom >= SCREEN_HEIGHT:
                # remove the jam jar and add to the score
                jam_jar_list.remove(jam_jar)
                score += 1

        # draw the game objects
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))

        for ufo in ufo_list:
            screen.blit(ufo.image, ufo.rect)

        for jam_jar in jam_jar_list:
            screen.blit(jam_jar.image, jam_jar.rect)

        # draw the score and lives
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: " + str(score), True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        lives_text = font.render("Lives: " + str(lives), True, (0, 0, 0))
        screen.blit(lives_text, (SCREEN_WIDTH - 100, 10))

        # update the display
        pygame.display.flip()

        # check for game over
        if lives <= 0:
            running = False

    # display game over message
    font = pygame.font.Font(None, 72)
    game_over_text = font.render("Game Over", True, (255, 0, 0))
    game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(game_over_text, game_over_rect)
    pygame.display.flip()

    # wait for 3 seconds before exiting
    pygame.time.wait(3000)

    # quit the game
