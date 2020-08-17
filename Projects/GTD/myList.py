class MyList:

    def __init__(self):
        self.taskList = []

    def setMyList(self,thought):
        self.taskList.append(thought)

    def getMyList(self):
        #print(self.taskList)
        return self.taskList

class MyCompleteList:

    def __init__(self):
        self.myComplteTaskList = []

    def setMyCompleteList(self,Mylist):
        self.myComplteTaskList.extend(Mylist)

    def getMyCompleteList(self):
        return self.myComplteTaskList

    def deleteItemFromMyCompleteList(self,index):
        self.getMyCompleteList

        return self.myComplteTaskList
