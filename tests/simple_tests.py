
import unittest


__author__ = 'robodasha'
__email__ = 'damirah@live.com'


class SimpleTests(unittest.TestCase):

    def setUp(self):
        print('Setup {0}'.format(self.__class__.__name__))

    def tearDown(self):
        print('Tear down {0}'.format(self.__class__.__name__))

    def test_basic(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
