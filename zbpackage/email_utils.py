'''
This module is for sending email. This can be imported in any main python file using following import command
from zbpackage import email_utils

'''

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def send_mail(fromaddr,toaddr,sub_data,body,fileattach='default'):
    # fileattach is an optional parameter
    msg = MIMEMultipart()
    msg['Subject'] = sub_data
    msg.attach(MIMEText(body, 'plain'))

    if fileattach != 'default':
        filename=fileattach.split("\\")[-1]
        attachment = open(fileattach, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(part)



    try:
        server = smtplib.SMTP('webmail.zimmer.com')
        server.starttls()
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    send_mail("python@zimmerbiomet.com","ranjeetkumar.singh@zimmerbiomet.com","ts","test")
    file="C:\\Temp\\cpi-script.txt"
    send_mail("python@zimmerbiomet.com","ranjeetkumar.singh@zimmerbiomet.com","ts","test",file)