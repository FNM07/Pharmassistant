from abc import ABC, abstractmethod
from Classes.Utilities import Iterator, Container
from Classes import Statics

class AccessDatabaseAccounts(Container.Container):

    def __init__(self):
        super(Container.Container, self).__init__()


    def getIterator(self):
        return AccessDatabaseAccounts.DatabaseAccounts()



    class DatabaseAccounts(Iterator.Iterator):
        def __init__(self, index=0):
            self.index=0

        def hasNext(self):
            if self.index < Statics.userList.__len__():
                return True
            else:
                return False

        def next(self):
            if self.hasNext():
                a = Statics.userList.__getitem__(self.index)
                self.index += 1
                return a
            else:
                self.index=0

        def add(self, toAdd):
            temp=toAdd
            #pass temp to a database management class method

        def remove(self, toBeRemove):
            temp=toBeRemove
            #pass temp to a database management class method

        def update(self, username, attribute, newValue):
            temp=username
            #dowork

        def search(self, toSearch):
            temp=""
            #pass temp to a database management class method which returns the search result
            return temp
