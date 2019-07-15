################################################################################
# Created By Kyle Howard Krug                                                  # 
# Created on 7/10/2019                                                         #
# This was created to be used as a template on how to send a file as an email  #
# with python                                                                  #
#Plan to use for creating automated reports and sending them to the user       #
#WARNING: The automated email is ot secured what so ever; no two factor and    #
#         must allow less secure apps through!                                 #
################################################################################
#Update: 7/10/2019: system is now setup to work with microsoft office 365 server
#        will now work with an exchange email address.
################################################################################
import smtplib #used for sending emails
#########################################################
#           Used to fill the email fields               # 
#########################################################
from email.mime.text import MIMEText                    #
from email.mime.multipart import MIMEMultipart          #
from email.mime.base import MIMEBase                    #
from email import encoders                              #
#########################################################

import os.path          
import datetime

timeanddate=datetime.datetime.now()

#################################
#setup for all the email fields##
#################################
myemail = ''
mypassword = ''# your email password
rEmail = ''# recipents email, to add more simple use a list
subject= '[Auto Generated] ... Report'
#msg = open('AutoMessage.txt')
with open('AutoMessage.txt', 'r') as file:
    msg = file.read()
msg = msg + '\nTime completed: ' + str(timeanddate)
file_loc= 'test.csv'# location of the file
#setup for the attachment on the
file_name = os.path.basename(file_loc)
print(file_name)
attach = open(file_loc, 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload(attach.read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % file_name)

###################################
#generates the lines for the email#
###################################
message = MIMEMultipart()
message['From'] = myemail
message['To'] = rEmail
message['Subject']= subject
message.attach(MIMEText(msg, 'plain'))
message.attach(part)

###########################################################
#                       server setup                      #
###########################################################
#tell server to login and send the report to a specific port
server = smtplib.SMTP('smtp.office365.com', 587) # if 587 doesn't work try 25 or 465
server.starttls()
server.login(myemail, mypassword)
text= message.as_string()
server.sendmail(myemail, rEmail, text)
server.quit()