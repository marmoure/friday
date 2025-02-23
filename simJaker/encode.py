from gsmmodem import pdu

# # Encode a message
# msg = pdu.encodeSmsSubmitPdu(
#     number="+213xxxxxxxxxxxxxx",
#     text="Hello, World!"
# )

# address = pdu._encodeAddressField("12345678900")

# print(address.hex())

def encode_phone_number(phone_number):
    # Ensure the phone number is in international format
    if not phone_number.startswith('+'):
        phone_number = '+' + phone_number

    # Remove the '+' sign for encoding
    phone_number = phone_number[1:]

    # Add the length of the phone number in semi-octets
    length = len(phone_number)
    
    # Add the type of number (TON) and numbering plan identification (NPI)
    # 0x91 indicates international number
    encoded_number = '{:02X}91'.format(length)

    # Convert the phone number to BCD and swap nibbles
    for i in range(0, len(phone_number), 2):
        if i + 1 < len(phone_number):
            encoded_number += phone_number[i+1] + phone_number[i]
        else:
            encoded_number += 'F' + phone_number[i]

    return encoded_number

phone_number = "213xxxxxxxxxxxx"
encoded_phone_number = encode_phone_number(phone_number)
print(encoded_phone_number)

# 0C91125306600836

# 0C91126365699031
# 0041000C911253066008367FF63802700000330D0000000050534800000000000042230121020744382E3130353105160604313035312D0C1003830607911263656990312B00