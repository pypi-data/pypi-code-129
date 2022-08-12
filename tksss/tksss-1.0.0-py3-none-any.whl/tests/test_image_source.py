# test_image_source.py はテスト用
import os
import unittest
from unittest.mock import patch, Mock


class LocalImageTest(unittest.TestCase):
    def test_get_image(self):
        from tksss.image_source import LocalImage

        path = os.path.dirname(__file__) + '/data/test_image.jpg'
        with LocalImage(path).get_image() as f:
            actual = f.read()
        with open(path, 'rb') as f:
            expected = f.read()
        self.assertEqual(expected, actual)


class RemoteImageTest(unittest.TestCase):
    def test_get_image(self):
        from tksss.image_source import RemoteImage

        url = 'https://raw.githubusercontent.com/rhoboro/lgtm/master/tests/data/test_image.jpg'
        with RemoteImage(url).get_image() as f:
            actual = f.read()

        path = os.path.dirname(__file__) + '/data/test_image.jpg'
        with open(path, 'rb') as f:
            expected = f.read()
        self.assertEqual(expected, actual)


class KeywordImageTest(unittest.TestCase):
    def test_get_image(self):
        from tksss.image_source import KeywordImage

        with patch('tksss.image_source.requests.get') as mock:
            path = os.path.dirname(__file__) + '/data/test_image.jpg'
            with open(path, 'rb') as f:
                expected = f.read()
            response = Mock()
            response.content = expected
            mock.return_value = response

            with KeywordImage('dog').get_image() as f:
                actual = f.read()

            self.assertEqual(expected, actual)

            # 意図通りの URL を参照していることを確認
            mock.assert_called_once_with('https://loremflickr.com/800/600/dog')


class ImageSourceTest(unittest.TestCase):
    def test_http(self):
        from tksss.image_source import ImageSource, RemoteImage

        # RemoteImage が意図通りに動くことを確認
        actual = ImageSource('http://www.example.com')
        self.assertEqual(RemoteImage, type(actual))

    def test_https(self):
        from tksss.image_source import ImageSource, RemoteImage

        # RemoteImage が意図通りに動くことを確認
        actual = ImageSource('https://www.example.com')
        self.assertEqual(RemoteImage, type(actual))

    def test_localpath(self):
        from tksss.image_source import ImageSource, LocalImage

        # LocalImage が意図通りに動くことを確認
        path = os.path.dirname(__file__) + '/data/test_image.jpg'
        actual = ImageSource(path)
        self.assertEqual(LocalImage, type(actual))

    def test_keyword(self):
        from tksss.image_source import ImageSource, KeywordImage

        # KeywordImage が意図通り動くことを確認
        actual = ImageSource('dog')
        self.assertEqual(KeywordImage, type(actual))


class GetImageTest(unittest.TestCase):
    def test_get_image(self):
        from tksss.image_source import get_image

        # get_image が一度の呼び出しで一度のみ動作していることの確認
        with patch('tksss.image_source.ImageSource') as mock:
            get_image('dog')
            mock.assert_called_once_with('dog')
