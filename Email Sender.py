from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SendEmail:

    def __init__(self, sender_email, receiver_email, subject):
        self.message = MIMEMultipart()
        self.message["From"] = sender_email
        self.message["To"] = receiver_email
        self.message["Subject"] = subject

    def secure_connection(self):
        import smtplib
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(user='mahadnaeem416@gmail.com', password='rguuwaeyqpcvwkup')
        s.sendmail(from_addr='mahadnaeem416@gmail.com', to_addrs='mahadnaeem416@gmail.com',
                   msg=self.message.as_string())
        s.quit()

    def message_body(self, text):
        self.message.attach(MIMEText(text))


def __main__():
    p = SendEmail('mahadnaeem416@gmail.com', 'mahadnaeem416@gmail.com', 'First Email')
    p.message_body("Hello How are you!!!")
    p.secure_connection()


if __name__ == '__main__':
    __main__()









# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart


# class SendEmail:

#     def __init__(self, sender_email, receiver_email, subject):
#         self.message = MIMEMultipart()
#         self.message["From"] = sender_email
#         self.message["To"] = receiver_email
#         self.message["Subject"] = subject

#     def secure_connection(self):
#         import smtplib
#         s = smtplib.SMTP('smtp.gmail.com', 587)
#         s.starttls()
#         s.login(user='mahadnaeem416@gmail.com', password='rguuwaeyqpcvwkup')
#         s.sendmail(from_addr='mahadnaeem416@gmail.com', to_addrs=email,
#                    msg=self.message.as_string())
#         s.quit()

#     def message_body(self, text):
#         self.message.attach(MIMEText(text))


# def __main__():
#     for x in email:
#         p = SendEmail('mahadnaeem416@gmail.com', x, 'First Email')
#         p.message_body("Hello How are you!!!")
#         p.secure_connection()


# if __name__ == '__main__':
#     email = ["mahadnaeem416@gmail.com'", "hammadzulfiqar555@gmail.com"]
#     __main__()
