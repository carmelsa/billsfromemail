import os
import pdf_handler


def test_pdf_handler_arnona():
    current_path = os.path.dirname(os.path.dirname(__file__))
    resource_path = os.path.join(current_path, "resources", "arnona_bill.pdf")
    # pdf_handler.read_pdf_with_pdf2(resource_path)
    pdf_handler.read_pdf_with_miner(resource_path)
    assert 1 == 1


def test_pdf_handler_maim():
    current_path = os.path.dirname(os.path.dirname(__file__))
    resource_path = os.path.join(current_path, "resources", "water_bill.pdf")
    # pdf_handler.read_pdf_with_pdf2(resource_path)
    pdf_handler.read_pdf_with_pdf2(resource_path)
    assert 1 == 1
