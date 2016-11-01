
import logging
import unittest

import research_papers.logutils as logutils
from research_papers.tools.crossref_resolver import CrossrefResolver

__author__ = 'robodasha'
__email__ = 'damirah@live.com'


class TestCrossrefResolver(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestCrossrefResolver, self).__init__(*args, **kwargs)
        logutils.setup_logging()
        self._logger = logging.getLogger(__name__)

    def setUp(self):
        self._logger.info('Setup {0}'.format(self.__class__.__name__))

    def tearDown(self):
        self._logger.info('Tear down {0}'.format(self.__class__.__name__))

    def test_resolve(self):
        """
        The two examples are taked directly from CrossRef API documentation:
        http://search.crossref.org/help/api
        :return:
        """
        cr = CrossrefResolver()
        reference_string_1 = "M. Henrion, D. J. Mortlock, D. J. Hand, and A. " \
                             "Gandy, \"A Bayesian approach to star-galaxy " \
                             "classification,\" Monthly Notices of the Royal " \
                             "Astronomical Society, vol. 412, no. 4, pp. " \
                             "2286-2302, Apr. 2011."
        title_1 = "A Bayesian approach to star-galaxy classification"
        doi_1 = "http://dx.doi.org/10.1111/j.1365-2966.2010.18055.x"

        reference_string_2 = "Renear 2012"
        title_2 = ""
        doi_2 = None

        self.assertEqual(cr.resolve(reference_string_1, title_1), doi_1)
        self.assertEqual(cr.resolve(reference_string_2, title_2), doi_2)


if __name__ == '__main__':
    unittest.main()
