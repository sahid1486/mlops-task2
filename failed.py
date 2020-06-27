import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
host_address = "e1bf3b71cc3435"
host_pass = "e4cc7a5f55f27b"
guest_address = "sahidmatrix00@gmail.com"
subject = "Regarding failure of main.py"
content = '''Hello, 
				Your mail is sent successfully.Developer used the commit and it failed
			THANK YOU'''
message = MIMEMultipart()
message['From'] = host_address
message['To'] = guest_address
message['Subject'] = subject
message.attach(MIMEText(content, 'plain'))
session = smtplib.SMTP('smtp.mailtrap.io', 2525)
session.starttls()
session.login(host_address, host_pass)
text = message.as_string()
session.sendmail(host_address, guest_address  , text)
session.quit()
print('Successfully sent your mail')




