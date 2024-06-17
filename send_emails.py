import dotenv
import json
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = dotenv.get_key('.env', 'SENDGRID_API_KEY')
sg = SendGridAPIClient(SENDGRID_API_KEY)

def send_emails(sg, recipients):
    with open('new_data.json', 'r') as f:
        new_companies = json.load(f)

    with open('modified_data.json', 'r') as f:
        updated_companies = json.load(f)

    for recipient in recipients:
        message = Mail(
            from_email='info@snaac.co.kr',
            to_emails=recipient
        )
        message.template_id = 'd-85349a0224bc49d2907cf6a9070f727a'
        message.dynamic_template_data = {
            "new_companies": new_companies,
            "updated_companies": updated_companies
        }
        
        try:
            response = sg.send(message)
            print(response.status_code, response.body, response.headers)
        except Exception as e:
            print(str(e))

if __name__ == '__main__':
    recipients = ['info@snaac.co.kr']

    send_emails(sg, recipients)