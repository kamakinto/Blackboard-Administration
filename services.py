class BbUser:
  email = ''
  username = ''
  firstName = ''
  lastName = ''
  def __init__(self, email, firstName, LastName):
    self.email = email
    self.firstName = firstName
    self.lastName = LastName

def testServices():
  return 'testing to see if we can get in this service'

def getUsersToAdd():
  user1 = BbUser('erobinson@aup.edu', 'Everett', 'Robinson')
  user2 = BbUser('kamakinto@aup.edu', 'John', 'Robinson')
  user3 = BbUser('haki_projects@aup.edu', 'mathieu', 'tool')
  user4 = BbUser('kamakuru@aup.edu', 'Ali', 'Macintosh')
  userList = [user1, user2, user3, user4];
  return userList

def createUser(username, firstName, LastName):
  pass

def createListofUsers(userIDList):
  pass

def deleteUser(userID):
  pass

def deleteListofUsers(userIDList):
  pass


