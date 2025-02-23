def calculate_cmgs_length(pdu):
    # Convert the PDU string to a list of bytes
    pdu_bytes = bytes.fromhex(pdu)
    
    # The first byte is the length of the SMSC information
    smsc_length = pdu_bytes[0]
    
    # The length for AT+CMGS is the total length minus the SMSC length byte and the SMSC information
    cmgs_length = len(pdu_bytes) - (smsc_length + 1)
    
    return cmgs_length

# Example PDU
pdu = "0041000C911263656990317FF63802700000330D0000000050534800000000000042230121020744382E3130353105160604313035312D0C1003830607911263656990312B00"
length = calculate_cmgs_length(pdu)
print(f"Length for AT+CMGS: {length}")