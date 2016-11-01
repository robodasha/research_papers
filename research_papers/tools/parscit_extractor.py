
import re
import os.path
import logging
import subprocess

import research_papers.logutils as logutils


__author__ = 'robodasha'
__email__ = 'damirah@live.com'


class ParscitExtractor(object):

    def __init__(self, parscit_dir):
        """
        :param parscit_dir: directory where ParsCit is installed
        """
        self._logger = logging.getLogger(__name__)
        self._parscit_dir = parscit_dir
        self._command = os.path.join(self._parscit_dir, 'bin/citeExtract.pl')

    def _output_path(self, input_path):
        """
        Get output path from input path (essentially just replaces the input
        extension with .xml).
        :param input_path:
        :return:
        """
        return os.path.splitext(input_path)[0] + '.xml'

    def extract_file(self, text_path):
        """
        Extracts citations from text file. The citations are stored in the same
        directory in an xml the name of which matches the original text file
        (e.g. for text file xyz.txt the citations will be stored in xyz.xml).
        :param text_path: path to the text file to extract citations from
        :return: None
        :raise: raises IOError in case the given path doesn't exist
        """
        # check if the file exists to avoid unnecessary allocation of resources
        if not os.path.exists(text_path) or os.path.getsize(text_path) <= 0:
            msg = 'File {} does not exist or is empty'.format(text_path)
            self._logger.error(msg)
            raise IOError(msg)

        text_fname = os.path.basename(text_path)
        self._logger.info('Extracting citations from {}'.format(text_fname))
        out_path = self._output_path(text_path)

        # skip if already extracted
        if os.path.exists(out_path):
            self._logger.debug('Citations for file {} already exist'
                               .format(text_fname))
        else:
            self._logger.info('Extracting citations')
            full_command = ['perl', self._command, '-m', 'extract_all',
                            text_path, out_path]
            subprocess.call(full_command)
            # if the output file doesn't exist at this point, create an empty
            # file instead, so that next time the unsuccessful file is skipped
            if not os.path.exists(out_path):
                with open(out_path, 'w'):
                    pass
        return

    def extract_directory(self, directory):
        """
        Extracts citations from all text files found in a directory. The
        citations for each text file are stored in the same directory in an xml
        file the name of which matches the name of the text file (e.g. for text
        xyz.txt the citations will be stored in xyz.xml).
        :param directory: the directory with text files
        :return: None
        """
        self._logger.info('Extracting citations from text files in {}'
                          .format(directory))
        files = [f for f in os.listdir(directory) if re.match(r'[0-9]+.txt', f)]

        # for logging purposes
        processed = 0
        total = len(files)
        how_often = logutils.how_often(total)
        self._logger.info('Found {} files to be processed'.format(total))

        for text in files:
            self._logger.debug('Processing file {}'.format(text))

            # run extraction and save the result
            self._logger.debug('Extracting citations from file {}'
                               .format(text))
            self.extract_file(os.path.join(directory, text))

            # log progress
            processed += 1
            if processed % how_often == 0:
                self._logger.debug(logutils.get_progress(processed, total))
        return
