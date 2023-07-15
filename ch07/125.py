phone_number = input("Type your phone number: ")
phone_number = phone_number.split("-")
telecom = {"011": "SKT", "016": "KT", "019":"LGU", "010":"UNKNOWN"}
if phone_number[0] in telecom.keys():
    print("Your telecom is %s" % (telecom[phone_number[0]]))