"""
    Cifra de Cesar
"""
import sys
args = []
for param in sys.argv:
    args.append(param)

alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encript(key, message):
    newMessage = ""
    for l in message:
        if l == ' ':
            newMessage += ' '
        else:
            index = alf.index(l.lower())
            index = (index + key) % 26
            newMessage += alf[index]
    return newMessage

def decript(key, code):
    newMessage = ""
    for l in code:
        if l == ' ':
            newMessage += ' '
        else:
            index = alf.index(l.lower())
            index = (index - key) % 26
            newMessage += alf[index]
    return newMessage

# print(args)

if len(args) == 3:
    print("Encripted: " + encript(int(args[1]), args[2]))
elif len(args) == 4:
    print("Decripted: " + decript(int(args[2]), args[3]))
else:
    print(" ~ Invalid arguments")

