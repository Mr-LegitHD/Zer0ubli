import json
import os
import sys
from smartcard.System import readers

from smartcard.util import toHexString

from smartcard.CardType import AnyCardType

from smartcard.CardConnection import CardConnection

from smartcard.CardRequest import CardRequest

#Enter Username
print('Gib deinen Name an')
name = input()
#Ask to create or load a plan
print("Neuen Wochenplan laden oder erstellen?\nSchreibe: Laden oder erstellen")
choose = input().lower()
if choose == "erstellen":

  #Welcome the User
  print("Wilkommen " + name.title())
  #Test trying to get acces to database
  print('Welchen Tag möchtest du einrichten?')
  x = input()
  # List every days
  weekdays = ("montag", "dienstag", "mittwoch", "donnerstag", "freitag", "samstag")

  # Make all letters lowercase & Check if Day is in list
  if x.lower() in weekdays:

    #Ask Lessons
    print('Welche Fächer hast du am ' + x+"\nSchreibe: Fach1, Fach2, Fach3,...")
    y = input()

    #ask number of books

    print('Wieviel Bücher hast du für diesen Tag')
    booknumber = input()
    books = 1

    #Scan books
    print("Scannen jetzt deine Bücher für "+x+"\nSchreibe: Start, um zu beginnen")
    startinput = input().lower()
    if startinput == "start":
        print("Schreibe: OK nach jedem Scan")
        print("Der Reader is verbunden, du kannst beginnen.")
        #accepts any NFC card in reader
        cardtype = AnyCardType()
        #wait for ever until card is present, and only trigger if a NEW card is presented to reader
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

        elif response == [0x04, 0xD4, 0xED, 0x92, 0x83, 0x5C, 0x80]:
          detectedcard = 'Book5'

        elif response == [0x04, 0xDD, 0xCF, 0x92, 0x83, 0x5C, 0x80]:
          detectedcard = 'Book6'

        elif response == [0x04, 0x30, 0xA7, 0x92, 0x83, 0x5C, 0x80]:
          detectedcard = 'Book7'

        elif response == [0x04, 0x2F, 0xDA, 0x92, 0x83, 0x5C, 0x80]:
          detectedcard = 'Book8'

        elif response == [0x04, 0x46, 0xD8, 0x92, 0x83, 0x5C, 0x81]:
          detectedcard = 'Book9'

        elif response == [0x04, 0x46, 0xD8, 0x92, 0x83, 0x5C, 0x81]:
          detectedcard = 'Book10'

        else:
          detectedcard = 'unknown card'

       #print('card serial number:', toHexString(response), ' - card status words:', "%x %x" % (sw1, sw2), ' - ', detectedcard)
        print(detectedcard)
        print("Welches Buch ist es?")
        bookname = input()
        print(bookname)
        # terminate the connection to the card correctly
        cardservice.connection.disconnect()

        dayplaner = dict(day=x, lessions=[y], books=[bookname])
        with open(name.lower() + "." + x.lower() + '.json', 'w+') as json_file:
            json.dump(dayplaner, json_file)
            json_file.close()
        print("All done")


        if startinput == "start":
           print("Schreibe: OK nach jedem Scan")
           print("Der Reader is verbunden, du kannst beginnen.")
           #accepts any NFC card in reader
           cardtype = AnyCardType()
           #wait for ever until card is present, and only trigger if a NEW card is presented to reader
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

           elif response == [0x04, 0xD4, 0xED, 0x92, 0x83, 0x5C, 0x80]:
             detectedcard = 'Book5'

           elif response == [0x04, 0xDD, 0xCF, 0x92, 0x83, 0x5C, 0x80]:
             detectedcard = 'Book6'

           elif response == [0x04, 0x30, 0xA7, 0x92, 0x83, 0x5C, 0x80]:
             detectedcard = 'Book7'

           elif response == [0x04, 0x2F, 0xDA, 0x92, 0x83, 0x5C, 0x80]:
             detectedcard = 'Book8'

           elif response == [0x04, 0x46, 0xD8, 0x92, 0x83, 0x5C, 0x81]:
             detectedcard = 'Book9'

           elif response == [0x04, 0x46, 0xD8, 0x92, 0x83, 0x5C, 0x81]:
             detectedcard = 'Book10'

           else:
             detectedcard = 'unknown card'

          #print('card serial number:', toHexString(response), ' - card status words:', "%x %x" % (sw1, sw2), ' - ', detectedcard)
           print(detectedcard)
           print("Welches Buch ist es?")
           bookname = input()
           print(bookname)
           # terminate the connection to the card correctly
           cardservice.connection.disconnect()
           r = open(str(name.lower() + "." + x.lower() + ".json"))
           daten = json.load(r)
           olddata = (str(str(str(daten["books"]))).replace("'", " ").replace("[", "").replace("]", ""))
           dayplaner = dict(day=x, lessions=[y], books=[olddata + bookname])
           with open(name.lower() + "." + x.lower() + '.json', 'w+') as json_file:
               json.dump(dayplaner, json_file)
               json_file.close()
           print("All done")


