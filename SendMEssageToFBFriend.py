# TAkes username, password and message and takes the name of friend to send the message to 
import fbchat
from getpass import getpass
username = str(raw_input("Username: "))
print (username)
client = fbchat.Client(username, getpass())
no_of_friends = int(raw_input("Number of friends: "))
for i in xrange(no_of_friends):
    name = str(input("Name: "))
    friends = client.getUsers(name)  # return a list of names
    friend = friends[0]
    print (friend)
    name = input("just a stopper - do you want to continue");
    msg = str(input("Message: "))
    sent = client.send(friend.uid, msg)
    if sent:
        print("Message sent successfully!")
