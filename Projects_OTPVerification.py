class OTPVerification:
    def __init__(self):
        import random
        otp = random.randint(100000, 999999)
        self.myOTP = otp
        print(self.myOTP)

    def secure_connection(self):
        import smtplib
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(user='mahadnaeem416@gmail.com', password='rguuwaeyqpcvwkup')
        email_id = input("Enter email: ")
        s.sendmail(from_addr=email_id, to_addrs=email_id, msg=str(self.myOTP))

    def verify_otp(self):

        user_otp = input('Enter Your OTP: ')
        if int(self.myOTP) == int(user_otp):
            print("Verified!!!")
        else:
            print("Wrong")

    def quit_connection(self, s):
        import smtplib
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.quit()


def __main__():
    p = OTPVerification()
    p.secure_connection()
    p.verify_otp()
    p.quit_connection(p)


if __name__ == '__main__':
    __main__()
