from pytextbelt import Textbelt

recipient = Textbelt.Recipient("4408640725", "us")
response = recipient.send("Hi its sai")
print(response)