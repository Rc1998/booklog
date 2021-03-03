#!/usr/bin/python

import json
import os

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.tag = "NULL" 
        self.filename = "./data/" + self.title + ".json"
    
    def __init__(self, title, author, tag):
        self.title = title
        self.author = author
        self.tag = tag 
        self.filename = "./data/" + self.title + ".json"
    
    def print_data(self):
        """ print json data for a given book """
        file = open('data.json', 'r')
        try:
            #file operations
            print(json.loads(self.filename))
        finally:
            file.close()

    def writeBook(self):
        """
        writes book and all data to a json file if one does not already exist 
        """
        if (self.isBook()):
            print("Book Exists.")
            self.print_data()
        else:
            # Construct the json to dump
            book = {"title": self.title, "author": self.author,
                    "tag": self.tag}
            
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(book, f, indent=4)

    def loadBook(self):
        """ loads book from json to book object """
        

    def isBook(self):
        """ returns if json file for book exists """
        return os.path.isfile(self.filename)
