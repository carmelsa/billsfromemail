import re
from collections import Counter

import slate3k as slate

SUM_PREFIX = ':ח״שב םולשתל כ״הס'


def get_sum_for_pay(text):
    return re.search(r".*:{0}\s+(?P<result>\d+\.\d+)".format(SUM_PREFIX), text).group("result")


def get_sum_for_pay_before_text(text):
    return re.search((r"(?P<result>\d+\.\d+)\s+%s" % SUM_PREFIX), text).group("result")


def get_sum_for_pay_most_common(text):
    array_all_num_in_text = [item.group("payment") for item in re.finditer(r"(?P<payment>\d+\.\d+)\s", text)]
    most_common = Counter(array_all_num_in_text).most_common(5)
    first_item = most_common[0]
    return max([float(item[0]) for item in most_common if item[1] == first_item[1]])


def read_pdf_with_slate(pdf_path):
    with open(pdf_path, 'rb') as f:
        extracted_text = slate.PDF(f)[0]
    return get_sum_for_pay_most_common(extracted_text)
