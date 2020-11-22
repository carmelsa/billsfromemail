import os
import pdf_handler


def test_pdf_handler_arnona():
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, "resources", "arnona", "arnona_bill.pdf")
    # pdf_handler.read_pdf_with_pdf2(resource_path)
    sumArnona = pdf_handler.read_pdf_with_slate(resource_path)
    assert 564.7 == sumArnona


def test_pdf_handler_maim():
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, "resources", "water", "water_bill.pdf")
    # pdf_handler.read_pdf_with_pdf2(resource_path)
    sum_water = pdf_handler.read_pdf_with_slate(resource_path)
    assert 117.59 == sum_water


def test_pdf_handler_gaz():
    current_path = os.path.dirname(__file__)
    resource_path = os.path.join(current_path, "resources", "gaz", "gaz1.pdf")
    # pdf_handler.read_pdf_with_pdf2(resource_path)
    sum_gaz = pdf_handler.read_pdf_with_slate(resource_path)
    assert 59.47 == sum_gaz