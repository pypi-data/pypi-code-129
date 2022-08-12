import requests
from io import BytesIO
from pathlib import Path


class LocalImage:
    """ファイルパスから画像を取得する"""
    def __init__(self, path):
        self._path = path

    def get_image(self):
        # rb → パス先にあるファイルを byte オブジョクトのままの状態で読み取る
        return open(self._path, 'rb')


class RemoteImage:
    """ URL から画像を取得する"""
    def __init__(self, path):
        self._url = path

    def get_image(self):
        # バイトデータをファイルオブジェクト(data)に変換
        data = requests.get(self._url)
        # BytesIO → インメモリで、格納したファイルを byte オブジョクトのままの状態で読み取る
        return BytesIO(data.content)


class _LoremFlickr(RemoteImage):
    """キーワード検索で画像を取得する"""
    # LoremFlickr のサービスは、https://loremflickr.com/<WIDTH>/<HEIGHT>/<KEYWORD>にアクセスすると、
    # 指定したサイズでキーワードに沿ったランダムな画像を返してくれる
    LOREM_FLICKR_URL = 'https://loremflickr.com'
    WIDTH = 800
    HEIGHT = 600

    def __init__(self, keyword):
        super().__init__(self._build_url(keyword))

    def _build_url(self, keyword):
        return (f'{self.LOREM_FLICKR_URL}/'
                f'{self.WIDTH}/{self.HEIGHT}/{keyword}')


# LoremFlickr を利用していることがわかるように _LoremFlickr クラスを定義し、
# KeywordImage という別名で参照できるようにする
KeywordImage = _LoremFlickr


def ImageSource(keyword):
    # コンストラクタとして利用するため、単語を大文字始まりにしてクラスのように見せる
    if keyword.startswith(('http://', 'https://')):
        return RemoteImage(keyword)
    elif Path(keyword).exists():
        return LocalImage(keyword)
    else:
        return KeywordImage(keyword)


def get_image(keyword):
    """画像のファイルオブジェクトを返す"""
    return ImageSource(keyword).get_image()
