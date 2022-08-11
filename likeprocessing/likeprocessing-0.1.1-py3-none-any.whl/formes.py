import likeprocessing.processing as processing
import pygame



def rect(x: int, y: int, largeur: int, hauteur: int):
    if processing.__no_fill is False:
        pygame.draw.rect(processing.screen, processing.__fill_color,
                         (x + processing.__dx, y + processing.__dy, largeur, hauteur), 0)
    if processing.__border_width > 0:
        pygame.draw.rect(processing.screen, processing.__border_color,
                         (x + processing.__dx, y + processing.__dy, largeur, hauteur), processing.__border_width)


def square(x: int, y: int, largeur: int):
    # pygame.draw.rect(processing.screen, processing.__fill_color,
    #                  (x + processing.__dx, y + processing.__dy, largeur, largeur), processing.__border_width)
    processing.rect(x, y, largeur, largeur)

def point(x: int, y: int):
    square(x, y, 2)


def line(x1: int, y1: int, x2: int, y2: int):
    pygame.draw.line(processing.screen, processing.__fill_color, (x1 + processing.__dx, y1 + processing.__dy),
                     (x2 + processing.__dx, y2 + processing.__dy), processing.__border_width)


def ellipse(x: int, y: int, largeur: int, hauteur: int):
    if processing.__no_fill == False:
        pygame.draw.ellipse(processing.screen, processing.__fill_color,
                            (x - largeur // 2 + processing.__dx, y - hauteur // 2 + processing.__dy, largeur, hauteur),
                            0)
    if processing.__border_width > 0:
        pygame.draw.ellipse(processing.screen, processing.__border_color,
                            (x - largeur // 2 + processing.__dx, y - hauteur // 2 + processing.__dy, largeur, hauteur),
                            processing.__border_width)


def arc(x: int, y: int, largeur: int, hauteur: int, angleDebut: float, angleFin: float):
    pygame.draw.arc(processing.screen, processing.__fill_color,
                    (x - largeur // 2 + processing.__dx, y - hauteur // 2 + processing.__dy, largeur, hauteur),
                    angleDebut, angleFin,
                    processing.__border_width)


def circle(x: int, y: int, diametre: int):
    ellipse(x, y, diametre, diametre)


def triangle(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int):
    line(x1 + processing.__dx, y1 + processing.__dy, x2 + processing.__dx, y2 + processing.__dy)
    line(x2 + processing.__dx, y2 + processing.__dy, x3 + processing.__dx, y3 + processing.__dy)
    line(x3 + processing.__dx, y3 + processing.__dy, x1 + processing.__dx, y1 + processing.__dy)


def quad(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int, x4: int, y4: int):
    line(x1 + processing.__dx, y1 + processing.__dy, x2 + processing.__dx, y2 + processing.__dy)
    line(x2 + processing.__dx, y2 + processing.__dy, x3 + processing.__dx, y3 + processing.__dy)
    line(x3 + processing.__dx, y3 + processing.__dy, x4 + processing.__dx, y4 + processing.__dy)
    line(x1 + processing.__dx, y1 + processing.__dy, x4 + processing.__dx, y4 + processing.__dy)
