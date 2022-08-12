import cv2
import matplotlib.pyplot as plt
import numpy as np


def display(img):
    """
    Plot image with matplotlib, support 3-channel or 1-channel input

    :param img: BGR
    :return: None
    """
    if img.shape[-1] == 3:
        plt.imshow(img[..., ::-1])
    else:
        plt.imshow(img)
    plt.show()


color_r = [0, 0, 255, 0.8]
color_g = [0, 255, 0, 0.8]
color_b = [255, 0, 0, 0.8]

color_r_light = [203, 192, 255, 0.8]
color_g_light = [152, 251, 152, 0.8]
color_b_light = [255, 255, 225, 0.8]

color_default = np.array([
    color_r,
    color_r,
    color_g,
    color_g,
    color_r,
    color_g,

    color_b,
    color_b,
    color_b,
    color_b,

    color_r,
    color_g,
    color_r,
    color_g,

    color_r,
    color_r,
    color_g,
    color_g,
    color_r,
    color_g,

    color_r,
    color_r,
    color_g,
    color_g,

    color_r,
    color_r,
    color_g,
    color_g
])

sklts_simbase_foot = [
    [0, 1], [1, 2], [3, 4], [4, 5], [2, 6], [3, 6],
    [6, 22], [22, 7], [7, 8], [8, 9],
    [12, 22], [13, 22], [2, 22], [3, 22],
    [10, 11], [11, 12], [13, 14], [14, 15], [8, 12], [8, 13],
    [0, 19], [0, 21],
    [5, 16], [5, 18],
    [10, 23], [10, 24],
    [15, 25], [15, 26]
]


def is_visible(confs, idx):
    return confs is None or confs[idx] == 1


def convert_color(color):
    def is_same_color(color1, color2):
        for a, b in zip(color1, color2):
            if a != b:
                return False
        return True

    if is_same_color(color, color_r):
        return color_r_light
    elif is_same_color(color, color_g):
        return color_g_light
    elif is_same_color(color, color_b):
        return color_b_light
    return color


def draw_sklts(img, kpts, kpts_vis=None, color=None, sklts=None, inplace=False, r=2, w=2):
    '''
    Draw keypoints and skeletons on the given image

    :param img:
    :param kpts:
    :param kpts_vis: 1-visible, 2-occluded, 3-out of frame
    :param color: None for predefined color
    :param sklts: default skeleton with 22 keypoints
    :param inplace: whether cover or return a copy of raw image
    :param r: radius of circle
    :param w: line width
    :return: img: a copy of raw image, so you do not need to worry about overwriting raw image
    '''
    img = img.copy() if not inplace else img
    color = color_default if color is None else color
    sklts = sklts_simbase_foot if sklts is None else sklts
    num_kpts = kpts.shape[0]
    kpts = np.array(kpts, dtype=np.int_)
    for i in range(num_kpts):
        cv2.circle(img, (int(kpts[i][0]), int(kpts[i][1])), r, (0, 255, 255), r)

    for i, (pt_a, pt_b) in enumerate(sklts):
        if pt_a >= num_kpts or pt_b >= num_kpts:
            continue
        if kpts[pt_a][0] < 0 or kpts[pt_b][0] < 0:
            continue
        curr_color = color[i % len(color)]
        if not (is_visible(kpts_vis, pt_a) and is_visible(kpts_vis, pt_b)):
            curr_color = convert_color(curr_color)
        cv2.line(img, (int(kpts[pt_a][0]), int(kpts[pt_a][1])), (int(kpts[pt_b][0]), int(kpts[pt_b][1])),
                 curr_color, w)
    return img


def draw_sklts_without_canvas(kpts, kpts_vis=None, color=None, sklts=None, r=2, w=2):
    '''
    Draw keypoints and skeletons on the given image

    :param kpts:
    :param color: None for predefined color
    :param sklts: default skeleton with 22 keypoints
    :return: img: drawn sklts with white background
    '''
    img = np.ones((368, 640, 3), dtype=np.uint8) * 255
    color = color_default if color is None else color
    sklts = sklts_simbase_foot if sklts is None else sklts
    if kpts.max() <= 1:
        kpts[:, 0] *= 640
        kpts[:, 1] *= 368
    kpts = np.array(kpts, dtype=np.int_)
    return draw_sklts(img, kpts, kpts_vis=kpts_vis, color=color, sklts=sklts, r=r, w=w)


color_dict = {'r': (0, 0, 255), 'g': (0, 255, 0), 'b': (255, 0, 0), 'd': (0, 0, 0), 'y': (0, 255, 255)}


def get_color(color='y'):
    if isinstance(color, str):
        color = 'y' if color not in color_dict else color
        color = color_dict[color]
    else:
        assert len(color) == 3, "color should be char or 3-tuple"
    return color


def put_text(img, text: str, pos=(15, 35), color='y', inplace=False, font_scale: float = 1.2, w: int = 2):
    '''
    put text on the given image (default not inplace)
    :param img:
    :param text: str
    :param pos:
    :param color: r, g, b, d(black), y(yellow)
    :param inplace: whether cover or return a copy of raw image
    :param font_scale: float
    :param w: line width
    :return: img (raw image or copy)
    '''
    img = img.copy() if not inplace else img
    color = get_color(color)
    cv2.putText(img, text, pos, cv2.FONT_HERSHEY_SIMPLEX, font_scale, color, w)
    return img


def draw_bbox(img, bbox, color='y', inplace=False, w: int = 2):
    '''
    draw bbox on the given image (default not inplace)
    :param img:
    :param bbox: lefttop_x, lefttop_y, width, height
    :param color: r, g, b, d(black), y(yellow)
    :param inplace: whether cover or return a copy of raw image
    :param w: line width
    :return: img (raw image or copy)
    '''
    img = img.copy() if not inplace else img
    x, y, w_, h = np.array(bbox, dtype=np.int_)
    color = 'y' if color not in color_dict else color
    img = cv2.rectangle(img, (x, y), (x + w_, y + h), color_dict[color], w)
    return img


def draw_points(img, points: np.ndarray, color='y', r: int = 2):
    '''
    draw multiple points on the given image (not inplace)
    :param img:
    :param points: np.ndarray (N, 2)
    :param color: r, g, b, d(black), y(yellow)
    :param r: radius of circle
    :return: img with drawn points
    '''
    assert len(points.shape) == 2, "points should be of shape (N, 2)"
    img = img.copy()
    color = get_color(color)
    for point in points:
        cv2.circle(img, (int(point[0]), int(point[1])), r, color, r)
    return img


def draw_lines(img, start_points: np.ndarray, end_points: np.ndarray, color='y', w: int = 2, arrowed=False):
    '''
    draw multiple lines on the given image (not inplace)
    :param img:
    :param start_points: np.ndarray (N, 2), denote start points of each line
    :param end_points: np.ndarray (N, 2), denote end points of each line
    :param color: r, g, b, d(black), y(yellow)
    :param w: line width
    :return: img with drawn points
    '''
    assert start_points.shape == end_points.shape
    assert len(start_points.shape) == 2
    img = img.copy()
    color = get_color(color)
    for s, e in zip(start_points, end_points):
        if arrowed:
            cv2.arrowedLine(img, (int(s[0]), int(s[1])), (int(e[0]), int(e[1])), color, w, tipLength=0.2)
        else:
            cv2.line(img, (int(s[0]), int(s[1])), (int(e[0]), int(e[1])), color, w)
    return img


__all__ = ["display", "draw_sklts", "put_text", "draw_bbox", "draw_sklts_without_canvas",
           "draw_lines", "draw_points"]
