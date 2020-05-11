import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.starttls()
''' MS smtp server and port
smtp.office365.com
Port: 587'''
