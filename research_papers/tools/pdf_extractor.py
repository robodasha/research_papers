
import glob
import os.path
import logging

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine

import research_papers.logutils as logutils


__author__ = 'robodasha'
__email__ = 'damirah@live.com'


class PdfExtractor(object):
    """
    Class for extracting text from PDF files. The library used for
    the extraction is PDFMiner (https://pypi.python.org/pypi/pdfminer/)
    """

    def __init__(self):
        self._logger = logging.getLogger(__name__)

    def _get_text_path_from_pdf_path(self, pdf_path):
        """
        Returns path to text based on given PDF path. The text path is obtained
        by replacing the .pdf extension with .txt (e.g. for PDF
        /path/to/pdf/xyz.pdf the text path will be /path/to/pdf/xyz.txt) or
        by appending .txt to the path in case it doesn't end with .pdf.
        :param pdf_path: string with the PDF path
        :return: text path as string
        """
        return '{}.txt'.format(pdf_path.rsplit('.pdf')[0])

    def pdf_to_txt(self, pdf_path):
        """
        Extracts text from PDF. The text is stored in the same directory in
        a txt file with the name of the PDF (e.g. for PDF xyz.pdf the text will
        be stored in xyz.txt).
        :param pdf_path: path to the PDF to extract text from
        :return: None
        :raise: raises IOError in case the given path doesn't exist
        """
        # check if the file exists to avoid allocating
        # resources which won't be used
        if not os.path.exists(pdf_path):
            msg = 'File {} does not exist'.format(pdf_path)
            self._logger.error(msg)
            raise IOError(msg)

        self._logger.info('Extracting text from {}'.format(pdf_path))
        text_path = self._get_text_path_from_pdf_path(pdf_path)

        # skip if already extracted
        if os.path.exists(text_path):
            self._logger.debug('Text for PDF {} already exists'
                               .format(pdf_path))
        else:
            self._pdf_to_text(pdf_path, text_path)
        return

    def _pdf_to_text(self, pdf_path, text_path):
        """
        This method does the actual text extraction. It uses PdfMiner Python
        library to do the extraction.
        :param pdf_path: path to the input PDF
        :param text_path: path to the output text
        :return: True if successful, False otherwise
        """
        text = ''
        num_pages = 0
        doc = PDFDocument()
        res_mgr = PDFResourceManager()

        device = PDFPageAggregator(res_mgr, laparams=LAParams())
        interpreter = PDFPageInterpreter(res_mgr, device)

        try:
            with open(pdf_path, 'rb') as fp:
                parser = PDFParser(fp)
                parser.set_document(doc)
                doc.set_parser(parser)
                doc.initialize('')
                for page in doc.get_pages():
                    self._logger.debug(
                        'Processing page {}'.format(num_pages + 1))
                    interpreter.process_page(page)
                    layout = device.get_result()
                    for lt_obj in layout:
                        if isinstance(lt_obj, LTTextBox) \
                                or isinstance(lt_obj, LTTextLine):
                            # print(lt_obj.get_text())
                            text += lt_obj.get_text()
                    num_pages += 1
                self._logger.info('Done, extracted {} pages'.format(num_pages))
                self._logger.debug('Storing result in {}'.format(text_path))
                with open(text_path, 'w') as text_fp:
                    text_fp.write(text.strip())
        except:
            self._logger.warning('Extracting text from {} failed'
                                 .format(pdf_path))
            return False
        finally:
            # close resources before exiting
            device.close()
        return text is not None and len(text)

    def pdfs_to_text(self, directory):
        """
        Extracts text from all PDFs found in a directory. The text for each PDF
        is stored in the same directory in a txt file with the name of the PDF
        (e.g. for PDF xyz.pdf the text will be stored in xyz.txt).
        :param directory: the directory with PDFs
        :return: number of
        """
        self._logger.info('Extracting text from PDFs in {}'.format(directory))
        pdfs = glob.glob(os.path.join(directory, '*.pdf'))

        # for logging purposes
        processed = 0
        total = len(pdfs)
        how_often = logutils.how_often(total)
        self._logger.info('Found {} PDFs to be processed'.format(total))

        for pdf in pdfs:
            pdf_fname = os.path.basename(pdf)
            self._logger.debug('Processing PDF {}'.format(pdf_fname))

            pdf_path = os.path.join(directory, pdf)

            # run extraction and save the result
            self._logger.debug('Extracting text from PDF {}'.format(pdf_fname))
            self.pdf_to_txt(pdf_path)

            # log progress
            processed += 1
            if processed % how_often == 0:
                self._logger.info(logutils.get_progress(processed, total))
