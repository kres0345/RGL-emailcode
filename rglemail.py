import imaplib, smtplib, getpass, os
variable1 = 0
if os.path.exists("error.txt"):
    os.remove("error.txt")
var1 = raw_input("Please enter your email: ")
print "The following text is hidden, but it is still typed."
var2 = getpass.getpass()
mserver = imaplib.IMAP4_SSL \
	('imap.gmail.com',993)
	
mserver.login(var1,var2)

stat,cnt = mserver.select('Inbox')

stat, dta = mserver.fetch \
			(cnt[0], \
			'(UID BODY[TEXT])')


print dta[0][1]
mserver.close()
mserver.logout()
text_file = open("Email.txt", "w")
text_file.write(dta[0][1])
text_file.close()
if not 'Subject: Sign into Renegade Line' in open('Email.txt').read():
    print("false")
    text_file = open("error.txt", "w")
    text_file.write("Your first email isn't the email from Raw Vengeance Games containing the code")
    text_file.close()
    variable1 = 1
   

text_file = open("Key.txt", "w")
text_file.write(var1)
text_file.close()
if variable1 == 1:
    os.remove("Key.txt")
