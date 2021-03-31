import pygame
import pygame.freetype
from pygame.sprite import Sprite
from pygame.rect import Rect
from enum import Enum
import sys

BLUE = (106, 159, 181)
WHITE = (255, 255, 255)
BLACK = (0,0,0)


def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    """ Returns surface with text written on """
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()

class GameState(Enum):
    QUIT=-1
    TITLE=0
    HUMAN_MODE=1
    PC_MODE=2
    FILL=3
    UNFILL=4
    HINT=5

class UIElement(Sprite):
    """ An user interface element that can be added to a surface """

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
        """
        Args:
            center_position - tuple (x, y)
            text - string of text to write
            font_size - int
            bg_rgb (background colour) - tuple (r, g, b)
            text_rgb (text colour) - tuple (r, g, b)
        """
        self.mouse_over = False  # indicates if the mouse is over the element

        # create the default image
        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        # create the image that shows when mouse is over the element
        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        # add both images and their rects to lists
        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        # calls the init method of the parent sprite class
        super().__init__()

        self.action = action

    # properties that vary the image and its rect when the mouse is over the element
    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)

def main_menu(screen):
    human_mode = UIElement(
        center_position=(400, 250),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="1. Human Mode",
        action=GameState.HUMAN_MODE,
    )
    pc_mode = UIElement(
        center_position=(400, 325),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="2. PC Mode",
        action=GameState.PC_MODE,
    )
    quit_btn = UIElement(
        center_position=(400,400),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="3. Exit",
        action=GameState.QUIT,
    )

    title = UIElement(
        center_position=(400, 125),
        font_size=50,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="MAIN MENU",
    )
    
    buttons = [human_mode, pc_mode,quit_btn,title]
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.draw.line(screen,WHITE,(0,75),(pygame.Surface.get_width(screen),75))
        pygame.draw.line(screen,WHITE,(0,175),(pygame.Surface.get_width(screen),175))

        pygame.display.flip()

def human_mode(screen):
    fill = UIElement(
        center_position=(160, 850),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Fill",
        action=GameState.FILL,
    )
    unfill = UIElement(
        center_position=(320, 850),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Unfill",
        action=GameState.UNFILL,
    )
    hint = UIElement(
        center_position=(480,850),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Hint",
        action=GameState.HINT,
    )

    quit_btn = UIElement(
        center_position=(640, 850),
        font_size=20,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Exit",
        action=GameState.QUIT,
    )

    title = UIElement(
        center_position=(400, 50),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="AQUARIUM",
    )
    buttons = [title, quit_btn,fill, unfill, hint]

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLUE)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)


        pygame.draw.line(screen,WHITE,(0,20),(pygame.Surface.get_width(screen),20))
        pygame.draw.line(screen,WHITE,(0,80),(pygame.Surface.get_width(screen),80))
        displayAquarium(screen)

        pygame.display.flip()


def displayAquarium(screen):
    pygame.draw.rect(screen,WHITE, ((125,125),(550,550)))
    n=550/6 #NxN N=6
    start_width=125
    start_height=125
    for i in range(5):
        pygame.draw.line(screen,BLUE,(start_width,start_height+(i+1)*n),(675,start_height+(i+1)*n),3)
        pygame.draw.line(screen,BLUE,(start_width+(i+1)*n,start_height),(start_width+(i+1)*n,675),3)
    #displayRowCap()
    #displayColCap()

def pc_mode(screen):
    pygame.quit()
    sys.exit("TODO pc mode") 

def fill(screen):
    pygame.quit()
    sys.exit("TODO fill") 


def unfill(screen):
    pygame.quit()
    sys.exit("TODO unfill") 

def hint(screen):
    pygame.quit()
    sys.exit("TODO hint") 


def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 900))
    game_state = GameState.TITLE

    while True:
        if game_state == GameState.TITLE:
            game_state = main_menu(screen)

        if game_state == GameState.HUMAN_MODE:
            game_state = human_mode(screen)
        
        if game_state == GameState.PC_MODE:
            game_state = pc_mode(screen)
        
        if game_state == GameState.FILL:
            game_state = fill(screen)

        if game_state == GameState.UNFILL:
            game_state = unfill(screen)
        
        if game_state == GameState.HINT:
            game_state = hint(screen)

        if game_state == GameState.QUIT:
            pygame.quit()
            return

main()