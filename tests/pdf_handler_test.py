import os
import pdf_handler


def test_pdf_handler_arnona():
    file_name_by_payment = {"arnona_bill_1.pdf": 564.7, "arnona_bill_2.pdf": 563.60, "arnona_bill_3.pdf": 574.10}
    pdf_handler_base_test(file_name_by_payment, "arnona")


def test_pdf_handler_water():
    file_name_by_payment = {"water_bill_1.pdf": 117.59, "water_bill_2.pdf": 152.92, "water_bill_3.pdf": 175.03}
    pdf_handler_base_test(file_name_by_payment, "water")


def test_pdf_handler_gaz():
    file_name_by_payment = {"gaz_bill_1.pdf": 59.47, "gaz_bill_2.pdf": 66.16, "gaz_bill_3.pdf": 79.55}
    pdf_handler_base_test(file_name_by_payment, "gaz")


def test_pdf_handler_electricity():
    file_name_by_payment = {"electricity_bill_1.pdf": 351.44, "electricity_bill_2.pdf": 329.24,
                            "electricity_bill_3.pdf": 792.52}
    pdf_handler_base_test(file_name_by_payment, "electricity")


def pdf_handler_base_test(file_name_by_payment, dir_name):
    current_path = os.path.dirname(__file__)
    for file_name, payment in file_name_by_payment.items():
        resource_path = os.path.join(current_path, "resources", dir_name, file_name)
        payment_result = pdf_handler.read_pdf_with_slate(resource_path)
        assert payment == payment_result
