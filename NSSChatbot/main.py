from nltk.chat.util import Chat, reflections

pairs = [
    ['my name is (.*)', ['Hi %1, this is Ally how can I help you?']],
    ['(Hi|hello|Hey|Holla)', ['Hello this is Ally your virtual assistant, how can I be of help?']],
    ['good (.*)', ['good %1, how can I help you?']],
    ['(bye|goodbye)', ['Goodbye', 'Bye', 'Have a lovely day']],
    ['(Thank you|thankyou|God bless you|thankyou very much|thank you very much|thanks)', ['You are welcome']],
    ['(.*) help (.*)', ['How may I help you']],
    ['(.*) request for certificate', ['Kindly visit nsscertificate.com and enter your nss number']],
    ['(.*) request for my certificate', ['Kindly visit nsscertificate.com and enter your nss number']],
    ['((.*) delivery take?|(.*) get my certificate|(.*) delivery)', [
        'Kindly delivery takes 1-7 working days, the cost is determined by the system and is displayed at the payment section']],
    ['(.*) payment', ['payment is made through mobile money or Express pay']],
    ['((.*) mobile money|(.*) momo|momo (.*)|mobile money (.*))',
     ["If mobile money isn't working, click the expresspay option and follow the prompts"]],
    ['(.*) your name', ['My name is Ally, how can I be of help?']],
    ['((.*) track order|(.*) track my order|(.*) track my certificate|(.*) track certificate)', [
        'Kindly visit nsscertifcate.com and enter your nss number again. The status of your request will be displayed with a link to track your shipment']],
    ['((.*) lost certificate|(.*) lost my certificate|(.*) her certificate|(.*) his certificate)',
     ['Kindly visit your regional office or national headquarters']],
    ['(.*) allawee', ['I am not privy to that information', 'contact your NSS regional office']],
    ['((.*) deducted|(.*) debited)', ['Kindly wait for a maximum of 24 hours and refresh the page again.']],
    ['(.*) find my nss number', ['click on DONT KNOW NSS NUMBER']],
    ['(.*) find my nss no', ['click on DONT KNOW NSS NUMBER']],
    ['(.*) not found', ['Kindly visit your regional office or national headquarters']]

]


chat = Chat(pairs, reflections)
chat.converse()
