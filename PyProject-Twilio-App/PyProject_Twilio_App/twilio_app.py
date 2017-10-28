from twilio.rest import Client


with open("testNumber.txt", "r") as file:
    testNumber = file.read()


def SendSMS(to, body):

    # Grab credentials.
    with open("accountSID.txt", "r") as file:
        accountSID = file.read()

    with open("authToken.txt", "r") as file:
        authToken = file.read()

    with open("twilioNumber.txt", "r") as file:
        twilioNumber = file.read()

    client = Client(accountSID, authToken)

    client.messages.create(
        to = to,
        from_ = twilioNumber,
        body = body)