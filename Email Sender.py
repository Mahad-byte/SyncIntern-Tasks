import email.mime.text as body
import email.mime.multipart as multipart
message = multipart()

class SendEmail: 

    def __init__(self, senderEmail, receiverEmail, subject):
        message["From"] = senderEmail
        message["To"] = receiverEmail
        message["subject"] = subject
        
    def secure_connection(self):
        import smtplib
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(user='mahadnaeem416@gmail.com', password='rguuwaeyqpcvwkup')
        s.sendmail(from_addr='mahadnaeem416@gmail.com', to_addrs='mahadnaeem416@gmail.com', msg=str(self.myOTP))

    def MessageBody(self, text):
        message.attach(body, text)
        
    def quit_connection(self, s):
        import smtplib
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.quit()


def __main__():
    p = SendEmail('mahadnaeem416@gmail.com', 'mahadnaeem416@gmail.com', 'First Email')
    p.secure_connection()
    p.MessageBody('Hello how are you!!!')
    p.quit_connection(p)


if __name__ == '__main__':
    __main__()
