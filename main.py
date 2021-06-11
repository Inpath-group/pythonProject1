
print("Type Hello for a response")
message = ""

while message != "bye":
    message = input(">").lower()
    if message == "hello":
        print('''
Please select a prompt.
1.How to request for certificate?
2.How long does delivery take? 
3.How much does delivery of certificate cost?
4.How to make payment?
5.What to do if I don't remember my nss number ?
6.What  to do if nss number cannot be certified? 
7.How do I track my order?
8.Lost certificate,  what to do? 
9.Payment not verified after deduction, what to do? .
        ''')
    elif message == "1":
        print('''
Kindly visit nsscertificate.com
Enter your nss number (there's a link below you can use if you don't have your nss number)
NOTE: IF YOU CAN'T FIND YOUR DETAILS IN FROM THE ABOVE STAGE, KINDLY VISIT YOUR REGIONAL OFFICE OR NATIONAL HEADQUARTERS
When you get to stage 2(where the map is), click on the link that says 'I'll type my address '
Fill in your address  details
Make sure you provide an active email address when filling the form(the soft copy will be sent to the email you provide(2019 batch and above)
Give consent
Make payment(for 2018/2019 year batch and below)
The amount is determined by the system and it will be displayed at the payment section. USE EXPRESS PAY IF MTN MOMO IS UNAVAILABLE 
At the end, you should see that your request is in queue.
For  2017/2018 - 2018/2019 year batch,  a QR code is provided after ordering, which you can scan to view the soft copy
        ''')
    elif message == "2":
        print("Kindly delivery takes 1-7 working days")

    elif message == "3":
        print("The cost is determined by the system and is displayed at the payment section")

    elif message == "4":
        print("Through mobile money or Express pay")

    elif message == "5":
        print("There's a link on the website that says 'Don't know Nss number?' Use that link to search with your other details")

    elif message == "6":
        print("Kindly visit your Regional Office or National headquarters")

    elif message == "7":
        print("Kindly visit nsscertifcate.com and enter your nss number again. The status of your request will be displayed with a link to track your shipment")

    elif message == "8":
        print("Kindly visit your regional office or national headquarters")

    elif message == "9":
        print("Kindly wait for a maximum of 24 hours and refresh the page again.")
        break
    else:
        print("Kindly call the call center for assitance")