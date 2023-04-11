import pywhatkit
# syntax: phone number with country code, message, hour, minutes, wait time, tab close, close time
phone_number = input()
pywhatkit.sendwhatmsg(phone_number, 'Message 1', 00, 00, 10, True, 2)