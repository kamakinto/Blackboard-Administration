from bbusers.models import BbUser as bbuserModel
import pprint
class BbUser:
  email = ''
  username = ''
  firstName = ''
  lastName = ''
  def __init__(self, email, firstName, LastName):
    self.email = email
    self.firstName = firstName
    self.lastName = LastName


def getUserDictList(request):
  #remove the csrfmiddlware token from the payload dictionary
  request.POST._mutable = True
  del request.POST['csrfmiddlewaretoken']

  #create a list of dictionaries (with extra default sections added)
  userRequestList = request.POST.keys()
  userquery= (bbuserModel.objects.filter(username__in = userRequestList))

  userDictList =[]
  for user in userquery:
    userDict = {
      "userName": user.username,
      "password": "",
      "availability": {
        "available": "Yes"
      },
      "name": {
        "given": user.firstName,
        "family": user.lastName,
      },
      "contact":{
        "email": user.email,
      }
    }
    userDictList.append(userDict)

 #pass the list of dictionaries to the celery function (the celery function 1. loops through each item and turnst hat item into a json file
 # then uses that record to send to Blackboard. if it fails  )
  return userDictList



def testServices():
  return 'testing to see if we can get in this service'

def getUsersToAdd():
  user1 = BbUser('erobinson@aup.edu', 'Everett', 'Robinson')
  user2 = BbUser('kamakinto@aup.edu', 'John', 'Robinson')
  user3 = BbUser('haki_projects@aup.edu', 'mathieu', 'tool')
  user4 = BbUser('kamakuru@aup.edu', 'Ali', 'Macintosh')
  userList = [user1, user2, user3, user4]
  return userList

def createUser(username, firstName, LastName):
  
  pass

def createListofUsers(userIDList):
  pass

def deleteUser(userID):
  pass

def deleteListofUsers(userIDList):
  pass


