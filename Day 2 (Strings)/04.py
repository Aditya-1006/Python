letter = '''Hello <|name|>,
    greeting from ABC company coding house
    I am Happy to tell you that you
    are selected for the SDE-1 role
    Bill Regards!
<|date|>'''

name=input("Enter Name: ")
date=input("Enter Date: ")

letter=letter.replace("<|name|>",name)
letter=letter.replace("<|date|>",date)

print(letter)




