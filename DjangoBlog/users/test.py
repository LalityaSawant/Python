import os

email_name = os.environ.get('EMAIL_USER')
email_pasword = os.environ.get('EMAIL_PASS')

print(email_name)
print(email_pasword)