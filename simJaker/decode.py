from io import StringIO
from smspdudecoder.fields import SMSSubmit

deliver_pdu = StringIO('0021000C9112636569903100000DC8329BFD6681AE6F399B1C02')
sms_data = SMSSubmit.decode(deliver_pdu)


print(f"Sender: {sms_data}")