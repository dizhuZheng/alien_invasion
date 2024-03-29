import pygame.font

class Button():

    def __init__(self, screen, x, y, msg, width, height, size):
        """Initialize button attributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #set the dimensions and properties of the button
        self.width, self.height = width, height
        self.button_color = (252, 186, 3)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, size)
        #build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = x
        self.rect.centery = y
        self.prep_msg(msg)


    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
