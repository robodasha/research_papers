
import logging
import unittest

import research_papers.logutils as logutils


__author__ = 'robodasha'
__email__ = 'damirah@live.com'


class TestPdfExtractor(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestPdfExtractor, self).__init__(*args, **kwargs)
        logutils.setup_logging()
        self._logger = logging.getLogger(__name__)

    def setUp(self):
        self._logger.info('Setup {0}'.format(self.__class__.__name__))

    def tearDown(self):
        self._logger.info('Tear down {0}'.format(self.__class__.__name__))

    def test_pdf_to_txt(self):
        self.fail()

    def test_pdfs_to_text(self):
        self.fail()


if __name__ == '__main__':
    unittest.main()
