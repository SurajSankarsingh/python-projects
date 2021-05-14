# email sender with html content

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = #sender name in ''
email['to'] = #destination email in ''
email['subject'] = #subject in ''

email.set_content(html.substitute({'name': 'Joe'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
  smtp.ehlo()
  smtp.starttls()
  smtp.login(#sender email in '', #enter email passwrd in '')
  smtp.send_message(email)
  print('all good boss!!')

