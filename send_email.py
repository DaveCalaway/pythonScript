# The script sents an email to show the ip address

import smtplib, ssl, subprocess, time
time.sleep(15) # wait for the connection

port = 465  # For SSL
password = "xyz" # sender mail pass
sender_email = "sender@gmail.com"
receiver_email = "receiver@gmail.com"

# is it online?
isOnline = True
while isOnline:
    # text = get the output in stout in a string format
    ping_out = subprocess.run(['ping', '-c', '1', '-W', '3', '8.8.8.8'], text=True, capture_output=True)
    ping_out = ping_out.stdout
    if ping_out.find("1 packets received") > 0:
        print("Connected")
        isOnline = False
    else:
        print("Not connected, i'm trying again..")
        time.sleep(10)

# Mail body
addr = subprocess.run(['ifconfig'], text=True, capture_output=True)
message = """\
Subject: Hi there from the Rpi Immergas.

This is the ip from Rpi:\n\n """  + addr.stdout

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    # Send email here
    server.sendmail(sender_email, receiver_email, message)
