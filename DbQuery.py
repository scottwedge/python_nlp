# -*- coding: utf-8 -*-

class DbQuery:
    
    def __init__(self):
        print("lolkek4eburek")
    
    def getNewTableTopicList(self):
        return """
CREATE TABLE TopicList (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  topicNum INTEGER,
  numOfTexts INTEGER);
"""

    def getNewTableTexts(self):
        return """
CREATE TABLE Texts (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  topicName TEXT,
  topicNum INTEGER,
  baseText TEXT,
  formattedText TEXT,
  vector TEXT,
  localDictionary TEXT);
"""
        
    def getNewTableDictionary(self):
        return """
CREATE TABLE Dictionary (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  word TEXT,
  value INTEGER);
"""

    def getNewTableInfo(self):
        return """
CREATE TABLE Info (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  language TEXT,
  source TEXT,
  numOfTopics INTEGER,
  numOfTexts INTEGER,
  dictionarySize INTEGER,
  stemType TEXT,
  stopWordsType TEXT,
  metric TEXT,
  neuralNetwork TEXT,
  resultFull TEXT,
  resultVal1 INTEGER,
  resultVal2 INTEGER,
  time TEXT,
  corpus_id INTEGER);
"""

    def getNewStringMain(self):
        return """INSERT INTO Corpuses DEFAULT VALUES;"""
    
    def getNewStringTopicList(self, corpusID):
        return """INSERT INTO TopicList DEFAULT VALUES;"""
    
    def getNewStringTexts(self, corpusID):
        return """INSERT INTO Texts DEFAULT VALUES;"""
    
    def getNewStringDictionary(self, corpusID):
        return """INSERT INTO Dictionary DEFAULT VALUES;"""
    
    def getNewStringInfo(self, corpusID):
        return """INSERT INTO Info DEFAULT VALUES;"""

    def getCountTableMain(self):
        return """SELECT COUNT(id) FROM Corpuses;"""
    
    def getCountTableTopicList(self):
        return """SELECT COUNT(id) FROM TopicList;"""
    
    def getCountTableTexts(self):
        return """SELECT COUNT(id) FROM Texts;"""
    
    def getCountTableDictionary(self):
        return """SELECT COUNT(id) FROM Dictionary;"""
    
    def getCountTableInfo(self):
        return """SELECT COUNT(id) FROM Info;"""

    def getUpdateMain(self, strID, strName, strVal):
        if (isinstance(strVal, int)):
            return """UPDATE Corpuses SET """+strName+""" = """+str(strVal)+""" 
    WHERE id = """+str(strID)+""";"""
        else:
            return """UPDATE Corpuses SET """+strName+""" = \""""+strVal+"""\" 
    WHERE id = """+str(strID)+""";"""
    
    def getUpdateTopicList(self, strID, strName, strVal):
        if (isinstance(strVal, int)):
            return """UPDATE TopicList SET """+strName+""" = """+str(strVal)+""" 
    WHERE id = """+str(strID)+""";"""
        else:
            return """UPDATE TopicList SET """+strName+""" = \""""+strVal+"""\" 
    WHERE id = """+str(strID)+""";"""
    
    def getUpdateTexts(self, strID, strName, strVal):
        if (isinstance(strVal, int)):
            return """UPDATE Texts SET """+strName+""" = """+str(strVal)+""" 
    WHERE id = """+str(strID)+""";"""
        else:
            return """UPDATE Texts SET """+strName+""" = \""""+strVal+"""\" 
    WHERE id = """+str(strID)+""";"""
    
    def getUpdateDictionary(self, strID, strName, strVal):
        if (isinstance(strVal, int)):
            return """UPDATE Dictionary SET """+strName+""" = """+str(strVal)+""" 
    WHERE id = """+str(strID)+""";"""
        else:
            return """UPDATE Dictionary SET """+strName+""" = \""""+strVal+"""\" 
    WHERE id = """+str(strID)+""";"""
    
    def getUpdateInfo(self, strID, strName, strVal):
        if (isinstance(strVal, int)):
            return """UPDATE Info SET """+strName+""" = """+str(strVal)+""" 
    WHERE id = """+str(strID)+""";"""
        else:
            return """UPDATE Info SET """+strName+""" = \""""+strVal+"""\" 
    WHERE id = """+str(strID)+""";"""

    def getDataMain(self, strID, strName):
        return """SELECT ("""+strName+""") FROM Corpuses WHERE id = """+str(strID)+""";"""
    
    def getDataTopicList(self, strID, strName):
        return """SELECT ("""+strName+""") FROM TopicList WHERE id = """+str(strID)+""";"""
    
    def getDataTexts(self, strID, strName):
        return """SELECT ("""+strName+""") FROM Texts WHERE id = """+str(strID)+""";"""
    
    def getDataDictionary(self, strID, strName):
        return """SELECT ("""+strName+""") FROM Dictionary WHERE id = """+str(strID)+""";"""
    
    def getDataInfo(self, strID, strName):
        return """SELECT ("""+strName+""") FROM Info WHERE id = """+str(strID)+""";"""

if __name__ == '__main__':
    q = DbQuery()
    print(q.getNewTableTexts)
    print("rabotaet")