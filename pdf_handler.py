import re
import PyPDF2
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

HOD_HASHRON = 'כ לתשלום בש'


def read_pdf_with_pdf2(pdf_path):
    pdf_file_obj = open(pdf_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    print(pdf_reader.numPages)
    page_obj = pdf_reader.getPage(0)
    page_test = page_obj.extractText()
    print(page_test)
    information = pdf_reader.getDocumentInfo()
    print(information)
    pdf_file_obj.close()


def read_pdf_with_miner(pdf_path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(pdf_path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos = set()
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching,
                                  check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return get_sum_for_pay(text)


def get_sum_for_pay(text):
    return re.search(r".*:ח״שב  םולשתל כ״הס\s+(?P<result>\d+\.\d+)", text).group("result")


