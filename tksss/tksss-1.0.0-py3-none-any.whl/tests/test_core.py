import os
import unittest
from pathlib import Path
from tksss.drawer import OUTPUT_NAME


class LgtmTest(unittest.TestCase):
    def setUp(self):
        output_path = Path(OUTPUT_NAME)
        if output_path.exists():
            output_path.unlink()

    def tearDown(self):
        output_path = Path(OUTPUT_NAME)
        output_path.unlink()

    def test_lgtm(self):
        from tksss.core import tksss

        path = os.path.dirname(__file__) + '/data/test_image.jpg'
        tksss(path, 'dog')

        output_path = Path(OUTPUT_NAME)
        self.assertTrue(output_path.exists())


