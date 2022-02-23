import sys

from smartcard.System import readers

from smartcard.util import toHexString

from smartcard.CardType import AnyCardType

from smartcard.CardConnection import CardConnection

from smartcard.CardRequest import CardRequest


print("Der Reader is verbunden, du kannst beginnen.")

# accepts any NFC card in reader
cardtype = AnyCardType()

while True:

    # wait for ever until card is present, and only trigger if a NEW card is presented to reader

    cardrequest = CardRequest(timeout=None, cardType=cardtype, newcardonly=True)

    cardservice = cardrequest.waitforcard()

    # if card is present, connect to card

    cardservice.connection.connect()

    # debug information - read and show ATR header with the card type

    # print (toHexString( cardservice.connection.getATR()))

    # send command to cards to red the serial number of the card

    apdu = [0xFF, 0xCA, 0x00, 0x00, 0x00]  # this command returns the serial number of the card

    response, sw1, sw2 = cardservice.connection.transmit(apdu)

    # serial number is in response string

    # evaluate response string and see if card is known

    if response == [0x04, 0x22, 0xA5, 0x92, 0x83, 0x5C, 0x80]:
        detectedcard = 'Book1'

    elif response == [0x04, 0x50, 0xA3, 0x92, 0x83, 0x5C, 0x80]:
        detectedcard = 'Book2'

    elif response == [0x04, 0x90, 0xD1, 0x92, 0x83, 0x5C, 0x80]:
        detectedcard = 'Book3'

    elif response == [0x04, 0xB2, 0xCD, 0x92, 0x83, 0x5C, 0x80]:
        detectedcard = 'Book4'

    else:
        detectedcard = 'unknown card'

    #print('card serial number:', toHexString(response), ' - card status words:', "%x %x" % (sw1, sw2), ' - ', detectedcard)
    print(detectedcard)

    # terminate the connection to the card correctly
    cardservice.connection.disconnect()
    z = input()

