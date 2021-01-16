# The script sents an email to show the ip address

import smtplib, ssl, subprocess, time
time.sleep(15) # wait for the connection

port = 465  # For SSL
password = "xyz" # sender mail pass
sender_email = "sender@gmail.com"
receiver_email = "receiver@gmail.com"

# Mail body
addr = subprocess.check_output(['ifconfig'], universal_newlines=True)
message = """\
Subject: Hi there from the Rpi Immergas.

This is the ip from Rpi:\n\n """  + addr

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    # Send email here
    server.sendmail(sender_email, receiver_email, message)
