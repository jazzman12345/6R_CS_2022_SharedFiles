usernames = ['Cheetara', 'Lion-O', 'Snarf', 'Tygra', 'Panthro', 'Mumm-Ra']


def login_unhandled(usernumber):
    print("\n -- The Basic Version --\n")
    number = int(usernumber)
    print("Welcome", usernames[number], "user number", number,".")
    division = 301 / number
    print(f"301 divided by {number} = {division}")


while True:
    inp = input("\nType in a number: ")
    login_unhandled(inp)
