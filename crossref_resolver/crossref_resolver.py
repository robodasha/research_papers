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

    def _remove_non_aplha(self, str):
        """
        :param str:
        :return:
        """
        return ''.join(ch for ch in str if ch.isalpha())

    def resolve(self, reference_string, reference_title):
        """
        :param reference_string:
        :param reference_title:
        :return:
        """
        query = urllib.parse.urlencode({'q': reference_string})
        request = urllib.parse.urljoin(self._endpoint, self._method)
        request += '?{}'.format(query)
        response = urllib.request.urlopen(request).read().decode('utf-8')
        if len(response) > 0:
            first_result = json.loads(response)[0]
            result_title = self._remove_non_aplha(first_result['title'])
            original_title = self._remove_non_aplha(reference_title)
            if result_title.lower() == original_title.lower():
                return first_result['doi']
        return None
