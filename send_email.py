# This i will use a gmail server so try to use gmail as possible

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Gmail account credentials
sender_email = "youremail@example.com" # Replace it with your real email
sender_password = "drgt nkad rddf vxhr"  # Use the App Password generated earlier

# Email details
recipient_email = "recipient@example.com" # enter a recipient email
subject = "Send emails in kali linux using the terminal"
message = "This is a test email sent using Python."
message += "Yes you can real send emails from the terminal using kali linux by simple steps if you wish please tell me at "
message += "sender_email@example.com"  # I used my gmail accont here

# Create the email message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = recipient_email
msg["Subject"] = subject

# Attach the message body
msg.attach(MIMEText(message, "plain"))

# Establish a secure connection with Gmail's SMTP server
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)  # gmail server port
    server.starttls()
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, recipient_email, msg.as_string())
    print("Email sent successfully!")

except Exception as e:
    print("Email could not be sent. Error:", str(e))

finally:
    server.quit()
