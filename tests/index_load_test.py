import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):

        # http://127.0.0.1/moho_extractor/LoadFileAsBase64?name=EpicPlanet_1.png
        # 200 OK
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
