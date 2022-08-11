"""Gets the players skin"""
import math
import os
import numpy
from tkinter import Tk, Canvas

import requests
from mojang import MojangAPI
from PIL import Image, ImageTk

#TODO
# - Make all PIL.Image instances use a custom Image (Image) that is a subclass of PIL.Image but can be converted to PhotoImage for tkinter. or tk canvas.

# The folder to place cache the fetched skins
HERE = os.getcwd()

class PlayerNotFoundError(Exception): pass
class CapeNotFoundError(Exception): pass

class Bone:
    HEAD = 'head'
    CAPE = 'cape'
    TORSO = 'torso'
    LEFT_LEG = 'left_leg'
    RIGHT_LEG = 'right_leg'
    LEFT_ARM = 'left_arm'
    RIGHT_ARM = 'right_arm'
    HEAD_OVERLAY = 'head_overlay'
    TORSO_OVERLAY = 'torso_overlay'
    LEFT_LEG_OVERLAY = 'left_leg_overlay'
    RIGHT_LEG_OVERLAY = 'right_leg_overlay'
    LEFT_ARM_OVERLAY = 'left_arm_overlay'
    RIGHT_ARM_OVERLAY = 'right_arm_overlay'

class Face:
    FRONT = 'front'
    BACK = 'back'
    LEFT = 'left'
    RIGHT = 'right'
    TOP = 'top'
    BOTTOM = 'bottom'

class Model:
    CLASSIC = 'classic'
    SLIM = 'slim'

class _renderBone:
    def __init__(self, hat:bool=True, jacket:bool=True, leftSleeve:bool=True, rightSleeve:bool=True, leftPantsLeg:bool=True, rightPantsLeg:bool=True):
        self.hat=hat
        self.jacket=jacket
        self.leftSleeve=leftSleeve
        self.rightSleeve=rightSleeve
        self.leftPantsLeg=leftPantsLeg
        self.rightPantsLeg=rightPantsLeg

class Skin():
    def __init__(self, skin_file:str, model:Model=Model.CLASSIC, cape_file:str=None):
        """
        Load skin from file
        
        Properties
        ----
        `skin_file` - The path to the skin image.

        `model` - The model that the skin image uses. Can be CLASSIC or SLIM.

        `cape_file` - The path to the cape image.
        """
        self.image = Image.open(skin_file, formats=['PNG']).convert('RGBA')
        self.model = model
        self.has_cape = False

        # The cape file
        if cape_file!=None:
            self.has_cape = True
            self.cape = Image.open(cape_file, formats=['PNG']).convert('RGBA')
        else: self.cape = None

    def _scale(self, scale, *values):
        """Internal function"""
        out = []
        for value in values: out.append(math.floor(value * scale))
        return out

    def _cutout_mask(self, image:Image, alpha:int=255):
        """Internal function"""
        mask = image.copy()
        pixels = mask.load() # create the pixel map
        for i in range(mask.size[0]):
            for j in range(mask.size[1]):
                if pixels[i,j][3] == 255: # Alpha channel must be completely solid
                    pixels[i,j] = (0, 0, 0, alpha) # Replace filled with white (Solid)
                else: pixels[i,j] = (255, 255, 255) # Replace transparent with black (transparent area)
        return mask

    def _pos(self, bone:Bone, face:Face, scale:float=1.0): # Returns with the bones position
        """internal function"""
        DATA = { #TODO should remove the _scale and use the raw numbers. then at the return line scale the values.
            'classic': {
                'head': {
                    'front': self._scale(scale, 4,0),
                    'back': self._scale(scale, 4,0),
                    'left': self._scale(scale, 4,0),
                    'right': self._scale(scale, 4,0),
                    'top': self._scale(scale, 4,6),
                    'bottom': self._scale(scale, 4,6)
                },
                'torso': {
                    'front': self._scale(scale, 4,8),
                    'back': self._scale(scale, 4,8),
                    'left': None,
                    'right': None,
                    'top': self._scale(scale, 4,8),
                    'bottom': None
                },
                'left_leg': {
                    'front': self._scale(scale, 4,20),
                    'back': self._scale(scale, 8,20),
                    'left': self._scale(scale, 6,20),
                    'right': None,
                    'top': None,
                    'bottom': self._scale(scale, 4,8)
                },
                'right_leg': {
                    'front': self._scale(scale, 8,20),
                    'back': self._scale(scale, 4,20),
                    'left': None,
                    'right': self._scale(scale, 6,20),
                    'top': None,
                    'bottom': self._scale(scale, 8,8)
                },
                'left_arm': {
                    'front': self._scale(scale, 0, 8),
                    'back': self._scale(scale, 12, 8),
                    'left': self._scale(scale, 6, 8),
                    'right': None,
                    'top': self._scale(scale, 0, 8),
                    'bottom': self._scale(scale, 0, 8)
                },
                'right_arm': {
                    'front': self._scale(scale, 12,8),
                    'back': self._scale(scale, 0,8),
                    'left': None,
                    'right': self._scale(scale, 6,8),
                    'top': self._scale(scale, 12,8),
                    'bottom': self._scale(scale, 12,8)
                },
                'cape': {
                    'front': self._scale(scale, 3,8),
                    'back': self._scale(scale, 3,8),
                    'left': self._scale(scale, 5,8),
                    'right': self._scale(scale, 10,8),
                    'top': self._scale(scale, 3,7),
                    'bottom': self._scale(scale, 3,7)
                }
            },

            'slim': {
                'head': {
                    'front': self._scale(scale, 3,0),
                    'back': self._scale(scale, 3,0),
                    'left': self._scale(scale, 3,0),
                    'right': self._scale(scale, 3,0),
                    'top': self._scale(scale, 3,6),
                    'bottom': self._scale(scale, 3,6)
                },
                'torso': {
                    'front': self._scale(scale, 3,8),
                    'back': self._scale(scale, 3,8),
                    'left': None,
                    'right': None,
                    'top': self._scale(scale, 3,8),
                    'bottom': None
                },
                'left_leg': {
                    'front': self._scale(scale, 3,20),
                    'back': self._scale(scale, 7,20),
                    'left': self._scale(scale, 5, 8),
                    'right': None,
                    'top': None,
                    'bottom': self._scale(scale, 3,8)
                },
                'right_leg': {
                    'front': self._scale(scale, 7,20),
                    'back': self._scale(scale, 3,20),
                    'left': None,
                    'right': self._scale(scale, 5,20),
                    'top': None,
                    'bottom': self._scale(scale, 7,8)
                },
                'left_arm': {
                    'front': self._scale(scale, 0, 8),
                    'back': self._scale(scale, 11, 8),
                    'left': self._scale(scale, 5,20),
                    'right': None,
                    'top': self._scale(scale, 0, 8),
                    'bottom': self._scale(scale, 0, 8)
                },
                'right_arm': {
                    'front': self._scale(scale, 11,8),
                    'back': self._scale(scale, 0,8),
                    'left': None,
                    'right': self._scale(scale, 5,8),
                    'top': self._scale(scale, 11,8),
                    'bottom': self._scale(scale, 11,8)
                },
                'cape': {
                    'front': None,
                    'back': None,
                    'left': None,
                    'right': None,
                    'top': None,
                    'bottom': None
                }
            }
        }
        return DATA[self.model][bone][face]
    pos = _pos #TODO remove underscore

    #TODO
    def origin(self, bone:Bone, face:Face, scale:float=1.0): # Returns with the bones origin
        DATA = {
            'classic': {
                'head': {
                    'front': self._scale(scale, 4,8)
                },
                'torso': {
                    'front': self._scale(scale, 4,6)
                },
                'left_leg': {
                    'front': self._scale(scale, 2,0)
                },
                'right_leg': {
                    'front': self._scale(scale, 2,0)
                },
                
                #TODO
                'left_arm': {
                    'front': self._scale(scale, 1,2)
                },
                'right_arm': {
                    'front': self._scale(scale, 1,2)
                },
                'cape': {
                    'front': self._scale(scale, 0,0)
                }
            }
        }
        return DATA[self.model][bone][face]

    def bone(self, bone: Bone, scale:float=1.0):
        """
        Returns with the PIL.Image of the body bones faces
        
        Properties
        ----
        `bone` - The bone to get.

        `scale` - The scale of the bone.
        """
        CLASSIC_UV = {
            'head': [(0,0, 32,16), self._scale(scale, 32, 16)],
            'head_overlay': [(32,0, 64,16), self._scale(scale, 32, 16)],
            'torso': [(16,16, 40,32), self._scale(scale, 24, 16)],
            'torso_overlay': [(16,32, 40,48), self._scale(scale, 24, 16)],
            'left_arm': [(40,16, 56,32), self._scale(scale, 16,16)],
            'left_arm_overlay': [(40,32, 56,48), self._scale(scale, 16,16)],
            'left_leg': [(0,16, 16,32), self._scale(scale, 16,16)],
            'left_leg_overlay': [(0,32, 16,48), self._scale(scale, 16,16)],
            'right_arm': [(32,48, 48,64), self._scale(scale, 16,16)],
            'right_arm_overlay': [(48,48, 64,64), self._scale(scale, 16,16)],
            'right_leg': [(16,48, 32,64), self._scale(scale, 16,16)],
            'right_leg_overlay': [(0,48, 16,64), self._scale(scale, 16,16)]
        }

        SLIM_UV = {
            'head': [(0,0, 32,16), self._scale(scale, 32, 16)],
            'head_overlay': [(32,0, 64,16), self._scale(scale, 32, 16)],
            'torso': [(16,16, 40,32), self._scale(scale, 24, 16)],
            'torso_overlay': [(16,32, 40,48), self._scale(scale, 24, 16)],
            'left_leg': [(0,16, 16,32), self._scale(scale, 16,16)],
            'left_leg_overlay': [(0,32, 16,48), self._scale(scale, 16,16)],
            'right_leg': [(16,48, 32,64), self._scale(scale, 16,16)],
            'right_leg_overlay': [(0,48, 16,64), self._scale(scale, 16,16)],
            'left_arm': [(40,16, 54,32), self._scale(scale, 14,16)],
            'left_arm_overlay': [(40,32, 54,48), self._scale(scale, 14,16)],
            'right_arm': [(32,48, 46,64), self._scale(scale, 14,16)],
            'right_arm_overlay': [(48,48, 62,64), self._scale(scale, 14,16)]
        }

        LEGACY_CLASSIC_UV = {
            'head': [(0,0, 32,16), self._scale(scale, 32, 16)],
            'torso': [(16,16, 40,32), self._scale(scale, 24, 16)],
            'left_arm': [(40,16, 56,32), self._scale(scale, 16,16)],
            'left_leg': [(0,16, 16,32), self._scale(scale, 16,16)],
            'right_arm': [(40,16, 56,32), self._scale(scale, 16,16)],
            'right_leg': [(0,16, 16,32), self._scale(scale, 16,16)],
            'head_overlay': [(32,0, 64,16), self._scale(scale, 32, 16)],
            'torso_overlay': None,
            'left_arm_overlay': None,
            'right_arm_overlay': None,
            'left_leg_overlay': None,
            'right_leg_overlay': None
        }
        
        LEGACY_SLIM_UV = {
            'head': [(0,0, 32,16), self._scale(scale, 32, 16)],
            'torso': [(16,16, 40,32), self._scale(scale, 24, 16)],
            'left_leg': [(0,16, 16,32), self._scale(scale, 16,16)],
            'right_leg': [(0,16, 16,32), self._scale(scale, 16,16)],
            'head_overlay': [(32,0, 64,16), self._scale(scale, 32, 16)],
            'left_arm': [(40,16, 54,32), self._scale(scale, 14,16)],
            'right_arm': [(40,16, 54,32), self._scale(scale, 14,16)],
            # 'right_arm': [(32,48, 46,64), self._scale(scale, 14,16)],
            'torso_overlay': None,
            'left_arm_overlay': None,
            'right_arm_overlay': None,
            'left_leg_overlay': None,
            'right_leg_overlay': None,

        }

        CAPE_UV = [(0,0, 22,17), self._scale(scale, 22, 17)]

        if bone!=Bone.CAPE:
            if self.image.size == (64,32):
                if self.model == Model.CLASSIC:
                    if LEGACY_CLASSIC_UV[bone]!=None: img = self.image.crop(LEGACY_CLASSIC_UV[bone][0]).resize(LEGACY_CLASSIC_UV[bone][1], Image.NEAREST)
                    else: return None
                elif self.model == Model.SLIM:
                    if LEGACY_SLIM_UV[bone]!=None: img = self.image.crop(LEGACY_SLIM_UV[bone][0]).resize(LEGACY_SLIM_UV[bone][1], Image.NEAREST)
                    else: return None
                else: raise KeyError(self.model)

            elif self.model == Model.CLASSIC:
                if CLASSIC_UV[bone]!=None: img = self.image.crop(CLASSIC_UV[bone][0]).resize(CLASSIC_UV[bone][1], Image.NEAREST)
                else: return None
            
            elif self.model == Model.SLIM:
                if SLIM_UV[bone]!=None: img = self.image.crop(SLIM_UV[bone][0]).resize(SLIM_UV[bone][1], Image.NEAREST)
                else: return None
            else: raise KeyError(self.model)

        else:
            if self.cape!=None: img = self.cape.crop(CAPE_UV[0]).resize(CAPE_UV[1], Image.NEAREST)
            # else: raise CapeNotFoundError('Player "%s" does not have a cape.'%('sgdfkhj'))
            else: return None

        # Make base layer opaque, but then make overlay transparent
        if bone.endswith('_overlay') or bone==Bone.CAPE: return img.convert('RGBA') # Make transparent overlay
        else: return img.convert('RGB') # Make solid

    def bone_face(self, bone:Bone, face:Face, scale:float=1.0, angle:float=0):
        """
        Returns with the PIL.Image of the bones face
        
        Properties
        ----
        `bone` - The bone to get.

        `face` - The face to get.

        `scale` - The scale of the bone.
        """
        img = self.bone(bone, scale)

        origin = self.origin(bone, face, scale)

        if img!=None:
            UV = {
                'head': {
                    'front': self._scale(scale, 8,8, 16,16),
                    'back': self._scale(scale, 24,8, 32,16),
                    'left': self._scale(scale, 0,8, 8,16),
                    'right': self._scale(scale, 16,8, 24,16),
                    'top': self._scale(scale, 8,0, 16,8),
                    'bottom': self._scale(scale, 16,0, 24,8)
                },
                'common': {
                    'front': self._scale(scale, 4,4, 8,16),
                    'back': self._scale(scale, 12,4, 16,16),
                    'left': self._scale(scale, 0,4, 4,16),
                    'right': self._scale(scale, 8,4, 12,16),
                    'top': self._scale(scale, 4,0, 8,4),
                    'bottom': self._scale(scale, 8,0, 12,4)
                },
                'torso': {
                    'front': self._scale(scale, 4,4, 12,16),
                    'back': self._scale(scale, 16,4, 24,16),
                    'left': self._scale(scale, 0,4, 4,16),
                    'right': self._scale(scale, 12,4, 16,16),
                    'top': self._scale(scale, 4,0, 12,4),
                    'bottom': self._scale(scale, 12,0, 20,4)
                },
                'cape': {
                    'front': self._scale(scale, 1,1, 11,17),
                    'back': self._scale(scale, 12,1, 22,17),
                    'left': self._scale(scale, 0,1, 1,17),
                    'right': self._scale(scale, 11,1, 12,17),
                    'top': self._scale(scale, 1,0, 11,1),
                    'bottom': self._scale(scale, 11,0, 21,1)
                }
            }

            SLIM_ARM_UV = {
                'front': self._scale(scale, 4,4, 7,16),
                'back': self._scale(scale, 11,4, 14,16),
                'left': self._scale(scale, 0,4, 4,16),
                'right': self._scale(scale, 7,4, 11,16),
                'top': self._scale(scale, 4,0, 7,4),
                'bottom': self._scale(scale, 7,0, 10,4)
            }
            bone = bone.replace('_overlay', '') # Remove overlay suffix
            if self.model==Model.SLIM and (bone==Bone.LEFT_ARM or bone==Bone.RIGHT_ARM): return img.crop(SLIM_ARM_UV[face]).rotate(angle, Image.NEAREST, center=origin)
            else:
                if bone == Bone.LEFT_ARM or bone==Bone.RIGHT_ARM or bone==Bone.LEFT_LEG or bone==Bone.RIGHT_LEG: bone = 'common'
                return img.crop(UV[bone][face]).rotate(angle, Image.NEAREST, center=origin)
        else:
            return None

    def paperdoll(self, face:Face, scale:float=1.0, renderOverlay:bool=True, renderCape:bool=True):
        """
        Creates a paperdoll from the skin.
        
        Properties
        ----
        `face` - The direction that the doll is facing.

        `scale` - The scale of the doll.

        `renderOverlay` - Whether or not to render the overlay.

        `renderCape` - Whether or not to render the cape.
        """
        if type(renderOverlay) == tuple: render = _renderBone(*renderOverlay)
        else: render = _renderBone(renderOverlay, renderOverlay, renderOverlay, renderOverlay, renderOverlay, renderOverlay)

        if self.model == Model.SLIM: base = Image.new('RGBA', self._scale(scale, 14, 32))
        else: base = Image.new('RGBA', self._scale(scale, 16, 32))
        
        head = self.bone_face(Bone.HEAD, face, scale)
        torso = self.bone_face(Bone.TORSO, face, scale)
        left_leg = self.bone_face(Bone.LEFT_LEG, face, scale)
        right_leg = self.bone_face(Bone.RIGHT_LEG, face, scale)
        left_arm = self.bone_face(Bone.LEFT_ARM, face, scale)
        right_arm = self.bone_face(Bone.RIGHT_ARM, face, scale)
        cape = self.bone_face(Bone.CAPE, face, scale)
        
        head_overlay = self.bone_face(Bone.HEAD_OVERLAY, face, scale)
        torso_overlay = self.bone_face(Bone.TORSO_OVERLAY, face, scale)
        left_leg_overlay = self.bone_face(Bone.LEFT_LEG_OVERLAY, face, scale)
        right_leg_overlay = self.bone_face(Bone.RIGHT_LEG_OVERLAY, face, scale)
        left_arm_overlay = self.bone_face(Bone.LEFT_ARM_OVERLAY, face, scale)
        right_arm_overlay = self.bone_face(Bone.RIGHT_ARM_OVERLAY, face, scale)

        #TODO Bone positions Should get replaced by self._bone_pos()
        if face == Face.FRONT:
            cape_pos = self._scale(scale, 3,8)
            if self.model ==Model.SLIM:
                head_pos = self._scale(scale, 3,0)
                torso_pos = self._scale(scale, 3,8)
                left_leg_pos = self._scale(scale, 3,20)
                right_leg_pos = self._scale(scale, 7,20)
                left_arm_pos = self._scale(scale, 0, 8)
                right_arm_pos = self._scale(scale, 11,8)
            else:
                head_pos = self._scale(scale, 4,0)
                torso_pos = self._scale(scale, 4,8)
                left_leg_pos = self._scale(scale, 4,20)
                right_leg_pos = self._scale(scale, 8,20)
                left_arm_pos = self._scale(scale, 0, 8)
                right_arm_pos = self._scale(scale, 12,8)

        elif face==Face.BACK:
            cape_pos = self._scale(scale, 3,8)
            if self.model == Model.SLIM:
                head_pos = self._scale(scale, 3,0)
                torso_pos = self._scale(scale, 3,8)
                left_leg_pos = self._scale(scale, 7,20)
                right_leg_pos = self._scale(scale, 3,20)

                left_arm_pos = self._scale(scale, 11, 8)
                right_arm_pos = self._scale(scale, 0,8)
            else:
                head_pos = self._scale(scale, 4,0)
                torso_pos = self._scale(scale, 4,8)
                left_leg_pos = self._scale(scale, 8,20)
                right_leg_pos = self._scale(scale, 4,20)
                left_arm_pos = self._scale(scale, 12, 8)
                right_arm_pos = self._scale(scale, 0,8)

        elif face==Face.LEFT:
            cape_pos = self._scale(scale, 5,8)
            torso_pos = None
            right_arm_pos = None
            right_leg_pos = None
            if self.model==Model.SLIM:
                head_pos = self._scale(scale, 3,0)
                left_arm_pos = self._scale(scale, 5, 8)
                left_leg_pos = self._scale(scale, 5,20)
            else:
                head_pos = self._scale(scale, 4,0)
                left_arm_pos = self._scale(scale, 6, 8)
                left_leg_pos = self._scale(scale, 6,20)

        elif face==Face.RIGHT:
            torso_pos = None
            left_arm_pos = None
            left_leg_pos = None
            cape_pos = self._scale(scale, 10,8)
            if self.model == Model.SLIM:
                head_pos = self._scale(scale, 3,0)
                right_arm_pos = self._scale(scale, 5,8)
                right_leg_pos = self._scale(scale, 5,20)
            else:
                head_pos = self._scale(scale, 4,0)
                right_arm_pos = self._scale(scale, 6,8)
                right_leg_pos = self._scale(scale, 6,20)

        elif face==Face.TOP:
            left_leg_pos = None
            right_leg_pos = None
            cape_pos = self._scale(scale, 3,7)

            if self.model==Model.SLIM:
                head_pos = self._scale(scale, 3,6)
                torso_pos = self._scale(scale, 3,8)
                left_arm_pos = self._scale(scale, 0, 8)
                right_arm_pos = self._scale(scale, 11,8)
            else:
                head_pos = self._scale(scale, 4,6)
                torso_pos = self._scale(scale, 4,8)
                left_arm_pos = self._scale(scale, 0, 8)
                right_arm_pos = self._scale(scale, 12,8)

        elif face==Face.BOTTOM:
            cape_pos = self._scale(scale, 3,7)
            torso_pos = None
            if self.model==Model.SLIM:
                head_pos = self._scale(scale, 3,6)
                left_arm_pos = self._scale(scale, 0, 8)
                right_arm_pos = self._scale(scale, 11,8)
                left_leg_pos = self._scale(scale, 3,8)
                right_leg_pos = self._scale(scale, 7,8)
            else:
                head_pos = self._scale(scale, 4,6)
                left_arm_pos = self._scale(scale, 0, 8)
                right_arm_pos = self._scale(scale, 12,8)
                left_leg_pos = self._scale(scale, 4,8)
                right_leg_pos = self._scale(scale, 8,8)

        else: raise KeyError(face)

        # Apply base layer
        if face!=Face.BACK and face!=Face.BOTTOM: # Render the cape behind all layers
            if cape_pos!=None and renderCape==True: base.paste(cape, cape_pos)

        if torso_pos!=None: base.paste(torso, torso_pos)
        if head_pos!=None: base.paste(head, head_pos)
        if left_leg_pos!=None: base.paste(left_leg, left_leg_pos)
        if right_leg_pos!=None: base.paste(right_leg, right_leg_pos)
        if left_arm_pos!=None: base.paste(left_arm, left_arm_pos)
        if right_arm_pos!=None: base.paste(right_arm, right_arm_pos)


        # Apply overlays
        if self.model==Model.SLIM:
            mask = Image.new('RGBA', self._scale(scale, 14, 32))
            overlay = Image.new('RGBA', self._scale(scale, 14, 32))
        else:
            mask = Image.new('RGBA', self._scale(scale, 16, 32))
            overlay = Image.new('RGBA', self._scale(scale, 16, 32))

        if render.jacket == True:
            if torso_overlay !=None and torso_pos!=None:
                overlay.paste(torso_overlay, torso_pos)
                mask.paste(torso_overlay, torso_pos)

        if render.hat == True:
            if head_overlay !=None and head_pos!=None:
                overlay.paste(head_overlay, head_pos)
                mask.paste(head_overlay, head_pos)

        if render.leftSleeve == True:
            if left_arm_overlay !=None and left_arm_pos!=None:
                overlay.paste(left_arm_overlay, left_arm_pos)
                mask.paste(left_arm_overlay, left_arm_pos)

        if render.rightSleeve == True:
            if right_arm_overlay !=None and right_arm_pos!=None:
                overlay.paste(right_arm_overlay, right_arm_pos)
                mask.paste(right_arm_overlay, right_arm_pos)

        if render.leftPantsLeg == True:
            if left_leg_overlay !=None and left_leg_pos!=None:
                overlay.paste(left_leg_overlay, left_leg_pos)
                mask.paste(left_leg_overlay, left_leg_pos)

        if render.rightPantsLeg == True:
            if right_leg_overlay !=None and right_leg_pos!=None:
                overlay.paste(right_leg_overlay, right_leg_pos)
                mask.paste(right_leg_overlay, right_leg_pos)

        mask2 = self._cutout_mask(mask)
        base = Image.composite(base,overlay,mask2).convert('RGBA')

        if face==Face.BACK or face==Face.BOTTOM: # Render the cape above all layers
            if cape_pos!=None and renderCape==True: base.paste(cape, cape_pos)
        return base

    def show(self, title:str=None):
        """Displays this image. This method is mainly intended for debugging purposes."""
        self.image.show(title)

    def bone_face_imageTk(self, bone:Bone, face:Face, scale:float=1.0, angle:int=0):
        """Returns a imageTk for tkinter"""
        bone = self.bone_face(bone, face, scale, angle)
        if bone==None: return None
        else: return ImageTk.PhotoImage(bone)

class MojangSkin(Skin):
    def __init__(self, username:str):
        """
        Load skin from the player's username
        
        Properties
        ----
        `username` - The username of the player's skin to get. throws PlayerNotFoundError if player is not found.
        """
        os.makedirs(os.path.join(HERE, '.cache'), exist_ok=True) # Make cache folder
        uuid = MojangAPI.get_uuid(username)
        if uuid!=None:
            profile = MojangAPI.get_profile(uuid)
            skin = os.path.join(HERE, '.cache', os.path.basename(profile.skin_url))
            if os.path.exists(skin)==False and os.path.isfile(skin)==False: # Check if skin is already in .cache before downloading it.
                skin_file = requests.get(profile.skin_url)
                with open(skin, 'wb') as w: w.write(skin_file.content)
            
            # Cape
            if profile.cape_url!=None:
                cape = os.path.join(HERE, '.cache', os.path.basename(profile.cape_url))
                if os.path.exists(cape)==False and os.path.isfile(cape)==False: # Check if the cape is already in .cache before downloading it.
                    cape_file = requests.get(profile.cape_url)
                    with open(cape, 'wb') as w: w.write(cape_file.content)
            else:
                cape=None
                    
            super().__init__(skin, profile.skin_model, cape)
        else:
            raise PlayerNotFoundError('No player with the username "%s" exists'%(username))

class SkinCanvas(Canvas):
    def __init__(self, master:Tk, scale:float=1.0,**kw):
        super().__init__(master,**kw)
        self.master=master
        self._scale = scale
        self._images = [] # Store tk images globally.

    def _store(self, image):
        """Internal function"""
        self._images.append(image)
        return self._images[-1]

    def create_bone(self, x:int, y:int, skin:Skin, bone:Bone, face:Face, angle:float=0, tag:str=None, **kw):
        """Create a bone and place it on the canvas"""
        if tag==None: tags = [bone]
        else: tags = [tag, tag+'.'+ bone]

        if bone.startswith('left_') or bone.startswith('right_'):
            t = bone.replace('left_', '').replace('right_', '')
            if tag==None: tags.append(t+'s')
            else: tags.append(tag+'.'+t+'s')

        image = self._store(skin.bone_face_imageTk(bone, face, self._scale, angle))
        return self.create_image(x,y, image=image, tags=tags, **kw)

    def create_paperdoll(self, x:int, y:int, skin:Skin, face:Face, renderOverlay:bool=True, renderCape:bool=True, tag:str=None, **kw):
        """
        Create a paperdoll and place it in the canvas
        
        Properties
        ----
        `x` & `y` - The position on the screen to place the doll

        `skin` - The skin to make the doll for

        `face` - The direction the doll is facing

        `renderOverlay` - Whether or not to render the overlay (2nd skin layer)

        `renderCape` - Whether or not to render the cape if defined.

        `tag` - The tag to apply to all bones. if undefined bone tags are the same as the bone name i.e. `head`. if defined it adds the bone name to the end i.e. `my_tag.head` for the head bone
        """

        # Get bone positions
        head_pos = [skin._pos(Bone.HEAD, face, self._scale)[0]+x, skin._pos(Bone.HEAD, face, self._scale)[1]+y]
        torso_pos = [skin._pos(Bone.TORSO, face, self._scale)[0]+x, skin._pos(Bone.TORSO, face, self._scale)[1]+y]
        left_arm_pos = [skin._pos(Bone.LEFT_ARM, face, self._scale)[0]+x, skin._pos(Bone.LEFT_ARM, face, self._scale)[1]+y]
        right_arm_pos = [skin._pos(Bone.RIGHT_ARM, face, self._scale)[0]+x, skin._pos(Bone.RIGHT_ARM, face, self._scale)[1]+y]
        left_leg_pos = [skin._pos(Bone.LEFT_LEG, face, self._scale)[0]+x, skin._pos(Bone.LEFT_LEG, face, self._scale)[1]+y]
        right_leg_pos = [skin._pos(Bone.RIGHT_LEG, face, self._scale)[0]+x, skin._pos(Bone.RIGHT_LEG, face, self._scale)[1]+y]

        # Create bones
        self.create_bone(*head_pos, skin, Bone.HEAD, face, 0, tag, **kw)
        self.create_bone(*torso_pos, skin, Bone.TORSO, face, 0, tag, **kw)
        self.create_bone(*left_arm_pos, skin, Bone.LEFT_ARM, face, 0, tag, **kw)
        self.create_bone(*right_arm_pos, skin, Bone.RIGHT_ARM, face, 0, tag, **kw)
        self.create_bone(*left_leg_pos, skin, Bone.LEFT_LEG, face, 0, tag, **kw)
        self.create_bone(*right_leg_pos, skin, Bone.RIGHT_LEG, face, 0, tag, **kw)

        if skin.has_cape:
            cape_pos = [skin._pos(Bone.CAPE, face, self._scale)[0]+x, skin._pos(Bone.CAPE, face, self._scale)[1]+y]
            cape = self.create_bone(*cape_pos, skin, Bone.CAPE, face, 0, tag, **kw)

            # Adjust bones so they properly display.
            if face == Face.FRONT: self.tag_lower(cape)

    #TODO
    def bone_configure(self, tag:str, x:int=None, y:int=None, face:Face=None, angle:float=None):
        """Modify the bone"""
        pass

    bone_config = bone_configure

    def paperdoll_configure(self, tag:str, x:int=None, y:int=None, face:Face=None, renderOverlay:bool=None, renderCape:bool=None):
        """Modify the doll"""
        pass

    paperdoll_config = paperdoll_configure

class SkinAnimation():
    def __init__(self, master:SkinCanvas, length:int, loop:bool=False, start_delay:int=0, loop_delay:int=0):
        """
        Animate the paperdoll

        Properties
        ----
        `master` - The SkinCanvas that contains the paperdoll.

        `length` - The entire length of the animation. (in ms)

        `loop` - should this animation stop, loop, or stay on the last frame when finished (true, false, "hold_on_last_frame")

        `start_delay` - How long to wait in ms before playing this animation.

        `loop_delay` - How long to wait in ms before looping this animation.
        """
        self.master = master
        self.length = length
        self.loop = loop
        self.start_delay = start_delay
        self.loop_delay = loop_delay
        self.frames = {}
        self.event_queue = []

    def _triggerEvent(self, tag:str, command:dict=None, rotation:dict=None, position:dict=None, scale:dict=None):
        items = self.master.find_withtag(tag)
        if command!=None: command['post']()
        
        for id in items:
            if rotation!=None: print('ROTATION')

            if position!=None:
                if position['post']!=None:
                    if type(position['post']) == int:
                        x0=position['post']
                        y0=position['post']
                    else:
                        x0=position['post'][0]
                        y0=position['post'][1]
                    self.master.coords(id, x0,y0)
                
                if position['rel']!=None:
                    if type(position['rel']) == int:
                        x0=position['rel']
                        y0=position['rel']
                    else:
                        x0=position['rel'][0]
                        y0=position['rel'][1]
                    
                    x1, y1 = self.master.coords(id)
                    self.master.coords(id, x0+x1,y0+y1)

            if scale!=None: print('SCALE')

    def _catmullrom(self): #TODO lerp
        return 0

    def _linear(self, start:float, stop:float):
        """Internal function"""
        step = (float(stop) - float(start)) / 25 # Tweak this value, Higher value = more frames
        return numpy.arange(float(start), float(stop), step).tolist() # Returns a list of values that are imbetween the start and stop values

    def _add(self, type:str, time:int, tag:str, post, rel):
        """Internal function"""
        data = {'post': post, 'rel': rel}
        if str(tag) not in self.frames: self.frames[str(tag)] = {} # Create tag
        if str(time) not in self.frames[str(tag)]: self.frames[str(tag)][str(time)] = {} # Create time in tag
        self.frames[str(tag)][str(time)][str(type)] = data
        return data

    def _run(self):
        # Save default pos, rot, and scale

        for tag in self.frames:
            tags = self.frames[tag]

            for time in tags:
                times = tags[time]
                id = self.master.after(int(time), lambda t=tag, d=times: self._triggerEvent(t,**d))
                self.event_queue.append(id)

        
        # END
        id = self.master.after(int(self.length), self._end)
        self.event_queue.append(id)

    def _end(self):
        """Insternal function"""
        # Stop all events
        self.stop()

        if self.loop==True:
            id = self.master.after(self.loop_delay, self._run)
            self.event_queue.append(id)


    def command(self, time:int, tag:str, command):
        """
        Add a command

        Properties
        ----
        `time` - The time in the animation to trigger this

        `tag` - The items's tag or id to modify

        `post` - The command to trigger
        """
        return self._add('command', time, tag, command, None)
    
    def rotate(self, time:int, tag:str, post:int=None, rel:int=None):
        """
        Add a rotation

        Properties
        ----
        `time` - The time in the animation to trigger this

        `tag` - The items's tag or id to modify

        `post` - Set the new rotation

        `rel` - Add the rotation to the current rotation
        """
        return self._add('rotation', time, tag, post, rel)

    def scale(self, time:int, tag:str, post:float=None, rel:float=None):
        """
        Add a scale

        Properties
        ----
        `time` - The time in the animation to trigger this

        `tag` - The items's tag or id to modify

        `post` - Set the new scale

        `rel` - Add the scale to the current scale
        """
        return self._add('scale', time, tag, post, rel)

    def translate(self, time:int, tag:str, post:int=None, rel:int=None):
        """
        Add a position

        Properties
        ----
        `time` - The time in the animation to trigger this

        `tag` - The items's tag or id to modify

        `post` - Set the new position

        `rel` - Add the postion to the current position
        """
        return self._add('position', time, tag, post, rel)

    def play(self):
        """Start the animation"""
        self.master.after(self.start_delay, self._run) # run the animation after the delay

    def stop(self):
        """Stop the animation"""
        for id in self.event_queue:
            self.master.after_cancel(id)

