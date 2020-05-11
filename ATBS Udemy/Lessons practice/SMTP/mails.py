import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.starttls()
''' MS smtp server and port
smtp.office365.com
Port: 587'''

type(conn)
conn.ehlo()
conn.login('rg6393@gmail.com', 'so06ny03g1993')
conn.sendmail('rg6393@gmail.com', 'rahul.goyal@iongroup.com', 'Subject: This is test \n\nDear Rahul,\n\nThe test mail is successfull. Try something difficult.\n\nRahul')
conn.quit()