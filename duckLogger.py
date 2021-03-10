
class user:
    def __init__(self, name, ducks):
        self.name = name
        self.timesDucked = ducks
    def formatReturn(self):
        return f'{self.name}-{self.timesDucked}'

def inUserList(name, list):
    for i in range(len(list)):
        if list[i].name == name:
            return i
    return "no user with that name"

def getInfo():
    f = open("ducks.txt", "r")
    returnUsers = []
    users = f.read().split("|")
    # print(users)
    # if len(users) > 0:
    if users != ['']:
        for person in users:
            attributes = person.split("-")
            returnUsers.append(user(attributes[0], attributes[1]))
    f.close()
    return returnUsers

def writeInfo(users):
    f = open("ducks.txt", "w")
    returnUsers = ""
    for person in users:
        returnUsers = returnUsers + person.formatReturn()
        if person != users[len(users) - 1]:
            returnUsers = returnUsers + "|"

    f.write(returnUsers)
    f.close()

if __name__ == "__main__":
    james = user("james", 0)

    ian = user("ian", 0)

    users = []
    users.append(james)
    users.append(ian)
    writeInfo(users)
    print(getInfo())

# Txt file structure:
# name-numberOfDucks|name-numberOfDucks