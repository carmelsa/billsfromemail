import pdf_handler
import gmail_handler


def main():
    creds = gmail_handler.get_token()
    emails = gmail_handler.get_attachment_from_email(creds)
    all_payments=[]
    for email in emails:
        for attachment in email.pdf_attachments:
            payment_amount = pdf_handler.get_payment_amount(attachment)
            all_payments.append(payment_amount)
    print(all_payments)

if __name__ == '__main__':
     main()
