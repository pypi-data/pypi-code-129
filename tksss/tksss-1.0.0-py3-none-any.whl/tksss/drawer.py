from PIL import Image, ImageDraw, ImageFont

MAX_RATIO = 0.8

FONT_MAX_SIZE = 256
FONT_MIN_SIZE = 24

FONT_NAME = '/c/Windows/Fonts/arialbd.ttf'
FONT_COLOR_RED = (255, 0, 0, 0)

OUTPUT_NAME = 'tksss_output.png'
OUTPUT_FORMAT = 'png'


def save_with_message(fp, message):
    # fp →　画像のファイルオブジェクト
    image = Image.open(fp)
    draw = ImageDraw.Draw(image)

    image_width, image_height = image.size
    message_area_width = image_width * MAX_RATIO
    message_area_height = image_height * MAX_RATIO

    # 1 ポイントずつ小さくしながら、最適なフォントサイズを求める
    for font_size in range(FONT_MAX_SIZE, FONT_MIN_SIZE, -1):
        font = ImageFont.truetype(FONT_NAME, font_size)

        text_width, text_height = draw.textsize(message, font=font)
        w = message_area_width - text_width
        h = message_area_height - text_height

        # 文字が文字描画先の範囲に収まる値を採用する
        if w > 0 and h > 0:
            position = ((image_width - text_width) / 2,
                        (image_height - text_width / 2))
            # 文字を描画する
            draw.text(position, message, fill=FONT_COLOR_RED, font=font)
            break
    image.save(OUTPUT_NAME, OUTPUT_FORMAT)
