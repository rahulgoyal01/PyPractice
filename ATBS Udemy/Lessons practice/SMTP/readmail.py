#below are run in python IDLE

import imapclient
import pyzmail
conn = imapclient.IMAPClient('imap.gmail.com', ssl=True, use_uid=True)
conn.login('rg6393', 'so06ny03g1993')
select_info = conn.select_folder('INBOX')
print("%d messages in INBOX" % select_info[b'EXISTS'])

mails = conn.search(['FROM', 'pujasaha556@gmail.com'])
print("%d mails from Puja" % len(mails))

rawmsg = conn.fetch([14142], ['BODY[]', 'FLAGS'])

msg = pyzmail.PyzMessage.factory(rawmsg[14142][b'BODY[]'])
msg.get_subject()
#if the below is none that means there is no text part
msg.text_part

msg.text_part.get_payload().decode('UTF-8')
conn.list_folders()
conn.logout()