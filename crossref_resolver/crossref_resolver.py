
import json
import logging
import urllib.parse
import urllib.request

__author__ = 'robodasha'
__email__ = 'damirah@live.com'


class CrossrefResolver(object):

    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self._endpoint = 'http://search.labs.crossref.org/'
        self._method = 'dois'

    def _remove_non_aplha(self, text):
        """
        :param text:
        :return:
        """
        if text is None or len(text) < 1:
            self._logger.debug('Input string was empty')
            return ''
        return ''.join(ch for ch in text if ch.isalpha())

    def resolve(self, reference_string, reference_title):
        """
        :param reference_string:
        :param reference_title:
        :return:
        """
        query = urllib.parse.urlencode({'q': reference_string})
        request = urllib.parse.urljoin(self._endpoint, self._method)
        request += '?{}'.format(query)
        self._logger.debug('CrossRef query: {}'.format(request))
        response = urllib.request.urlopen(request).read().decode('utf-8')
        if len(response) > 0:
            first_result = json.loads(response)[0]
            result_title = self._remove_non_aplha(first_result['title']).lower()
            original_title = self._remove_non_aplha(reference_title).lower()
            self._logger.debug('Comparing normalized titles: {}, {}'.format(
                result_title, original_title))
            if result_title == original_title:
                self._logger.debug('Got a DOI: {}'.format(first_result['doi']))
                return first_result['doi']
        self._logger.debug('No DOI for citation: {}'.format(reference_title))
        return None
