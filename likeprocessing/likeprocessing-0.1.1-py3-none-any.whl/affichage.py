import likeprocessing.processing as processing
import pygame
from pygame.colordict import THECOLORS as COLORS

import likeprocessing.processing


def background(couleur: any):
    if isinstance(couleur, pygame.Surface):
        processing.__background_image = couleur
    else:
        c = rgb_color(couleur)
        if c is not None:
            processing.__background_color = c
    processing.draw_background()


def noFill():
    processing.__border_width = 2
    processing.__no_fill = True


def stroke(couleur: any):
    c = rgb_color(couleur)
    if c is not None:
        processing.__border_color = c


def noStroke():
    processing.__border_width = 0


def fill(couleur: any):
    c = rgb_color(couleur)
    if c is not None:
        processing.__fill_color = c
        processing.__no_fill = False


def color(rouge: int, vert: int=None, bleu: int=None):
    if vert is None:
        return (rouge,rouge,rouge)
    return rouge,vert,bleu


def frameRate(valeur=None):
    if valeur is None:
        return processing.__fps
    elif valeur > 0:
        fps = valeur


def setFrameRate(valeur):
    frameRate(valeur)


def getFrameRate():
    return frameRate()


def noLoop():
    processing.__no_loop = True


def loop():
    processing.__no_loop = False


def rgb_color(valeur)->tuple:

    if isinstance(valeur, tuple):
        if len(valeur) == 3:
            return tuple([v for v in valeur]+[255])
        elif len(valeur) == 4:
            return valeur
    elif isinstance(valeur, int):
        return (min(255, valeur), min(255, valeur), min(255, valeur))
    elif isinstance(valeur, str):
        if valeur[0] == '#' and len(valeur) == 7:
            return (int(valeur[1:3], 16), int(valeur[3:5], 16), int(valeur[5:], 16))
        elif COLORS.get(valeur.lower()):
            return COLORS.get(valeur.lower())
    return None


def translate(x: int, y: int):
    processing.__dx += x
    processing.__dy += y


def reset():
    processing.__dx = 0
    processing.__dy = 0
