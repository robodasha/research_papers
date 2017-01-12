
import logging

from mendeley import Mendeley
from mendeley.exception import MendeleyException

__author__ = 'robodasha'
__email__ = 'damirah@live.com'


class MendeleyResolver(object):

    FIELDS = ['id', 'title', 'type', 'abstract', 'source', 'year', 'authors',
              'identifiers', 'keywords', 'link', 'month', 'day', 'revision',
              'pages', 'volume', 'issue', 'websites', 'publisher', 'city',
              'edition', 'institution', 'series', 'chapter', 'editors',
              'file_attached', 'reader_count',
              'reader_count_by_academic_status',
              'reader_count_by_subdiscipline', 'reader_count_by_country',
              'group_count']

    def __init__(self, client_id, secret):
        self._logger = logging.getLogger(__name__)
        mendeley_object = Mendeley(client_id, secret)
        auth = mendeley_object.start_client_credentials_flow()
        self._mendeley = auth.authenticate()

    def _remove_non_aplha(self, text):
        """
        :param text:
        :return:
        """
        if text is None or len(text) < 1:
            self._logger.debug('Input string was empty')
            return ''
        return ''.join(ch for ch in text if ch.isalpha())

    def get_document_by_doi(self, doi):
        """
        :param doi:
        :return: document metadata (all possible fields are listed in
                 MendeleyResolver.FIELDS) or None if document wasn't found
        """
        self._logger.info('Resolving document from Mendeley by DOI: {}'
                          .format(doi))
        try:
            doc = self._mendeley.catalog.by_identifier(doi=doi, view='all')
            self._logger.debug('Found document')
            return doc
        except MendeleyException:
            pass
        return None

    def get_document_by_title_and_year(self, title, year):
        """
        :param title:
        :param year:
        :return: document metadata (all possible fields are listed in
                 MendeleyResolver.FIELDS) or None if document wasn't found
        """
        self._logger.info('Resolving document from Mendeley by title and year: '
                          '{}, {}'.format(title, year))
        orig_title = self._remove_non_aplha(title).lower()
        try:
            page = self._mendeley.catalog.advanced_search(title=title,
                                                          view='all').list()
            for doc in page.items:
                mendeley_title = self._remove_non_aplha(doc.title).lower()
                self._logger.debug('Comparing titles {}, {}'
                                   .format(mendeley_title, orig_title))
                if mendeley_title == orig_title and int(doc.year) == int(year):
                    return doc
        except MendeleyException:
            pass
        return None
