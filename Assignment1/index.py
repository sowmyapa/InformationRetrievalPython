#Python 2.7.3
# -*- coding: latin-1 -*-
import re
import os
import collections
import time


class index:
    def __init__(self,path):
        self.path = path;
        self.inverterIndexMap = {};
        self.docIDToFnameMap={};

    def buildIndex(self):
        """function to read documents from collection, tokenize and build the index with tokens
         index should also contain positional information of the terms in the document term: [(ID1,[pos1,pos2,..]), (ID2, [pos1,pos2,…]),…]
         use unique document IDs
           This function loops through all files in the given directory.
           For each file it reads content one line at a time, strips new line characters at beginning and end of each line.
           tokenizes the line using "\W+" and converts each token into lowercase.
           docIDToFnameMap is a map whose value is again a map. This inner map has docID as the key, and list of posIDs in doc as value.
           Now there can be three cases :
           Case 1 : token is a new term in the dictionary : the token is inserted as a fresh entry in map.
           Case 2 : token and docID present in dictionary, new position as to be inserted : We fetch the innerMap using term as key,
                    from this inner map take the position list value using docID as key, now append this new position to the list.
           Case 3 : token is present in dictionary and a new docID as to be inserted into inner map : We fetch the innerMap using term as key,
                    To this inner map add a new entry with docID as key and list of new position as value.
        """
        files = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]
        self.inverterIndexMap = {};
        docID = 1;
        for fname in files:
            pos=1;
            self.docIDToFnameMap[docID] = fname;
            for l in open(os.path.join(self.path, fname), 'rt').readlines():
                l.strip();
                for word in re.split('\W+', l):
                    if(word!=''):
                        lowerCaseWord=word.lower();
                        if(lowerCaseWord in self.inverterIndexMap):
                            tokenMapValue = self.inverterIndexMap[lowerCaseWord] ;
                            if(docID in tokenMapValue):
                                tokenMapValue[docID].append(pos);
                            else:
                                tokenMapValue[docID]= [pos];
                                self.inverterIndexMap[lowerCaseWord]=tokenMapValue;
                        else:
                            self.inverterIndexMap[lowerCaseWord] = {docID: [pos]};
                        pos += 1;
            docID += 1;


    def tokenize(self,line):
        """This function tokenizes the given line using \W+. And returns these tokens as a list. """
        types = re.split("\W+",line);
        tokens=[];
        for term in types:
            if type!='':
                tokens.append(term.lower());
        return tokens;

    def get_docIDs_for_query_tokens(self,query_tokens):
        """This function returns a map. Each query token will be a key in the map.
           The value will be list of docIDs which contains the query token. """
        queryTokenWithDocIDMap={};
        for token in query_tokens:
            tokenDocIDList=[]
            if(token in self.inverterIndexMap):
                docIDs = self.inverterIndexMap[token];
                for key in docIDs:
                    tokenDocIDList.append(key);
            queryTokenWithDocIDMap[token]=tokenDocIDList;
        return queryTokenWithDocIDMap;

    def intersect(self,list1, list2):
        """This function returns a list of docIDs which are present in both list1 and list2."""
        return list(set(list1) & set(list2))

    def and_query(self, query_terms):
        # function for identifying relevant docs using the index
        """This function 1) tokenizes the query terms into a list.
           2) Fetched the list of all docIDs which contain the query terms
           3) sorts the query term in order of the size of the document list containing the term
           4) It then loops through each of the query term in the sorted order.ie., query term with smallest document list is picked first.
           5) Before looping, two query terms documentList are merged and is set to result.
           6) In loop, every iteration the result is merged with the next query term and this result is assigned back to list
           7) At end of this iteration result has the list of all documents in which all query terms are present

           here the idea is, when the query terms are sorted by the size of their posting list. Result will never be greater then the size of
           the smallest document list. Thus optimizing performance."""
        query_tokens=self.tokenize(query_terms);
        queryTokenWithDocIDMap = self.get_docIDs_for_query_tokens(query_tokens);
        sortedByPostingLength=sorted(queryTokenWithDocIDMap, key=lambda k: len(queryTokenWithDocIDMap[k]));
        if len(sortedByPostingLength)>1:
            queryResult = self.intersect(queryTokenWithDocIDMap[sortedByPostingLength[0]],queryTokenWithDocIDMap[sortedByPostingLength[1]]);
            for i in range(2,len(sortedByPostingLength)):
                queryResult = self.intersect(queryResult,
                                             queryTokenWithDocIDMap[sortedByPostingLength[i]]);
            return queryResult;

        else:
            return queryTokenWithDocIDMap[sortedByPostingLength[0]];


    def print_dict(self):
        # function to print the terms and posting list in the index
        for key in self.inverterIndexMap:
            innerMap = self.inverterIndexMap[key];
            valueList=[];
            keylist = innerMap.keys()
            keylist.sort()
            for docID in keylist:
                valueList.append("("+str(docID)+","+str(innerMap[docID])+")");
            print key ,valueList;


    def print_doc_list(self):
        # function to print the documents and their document id
        for key in self.docIDToFnameMap:
            print "Doc ID:"+str(key)+" ==> "+str(self.docIDToFnameMap[key]);


    def read_lines(self,filename):
        """This function return a list of all lines in the given file"""
        query_terms = [];
        for l in open( filename, 'rt').readlines():
            query_terms.append(l.strip());
        return query_terms;



def main():
    path = raw_input("Enter directory path containing all documents\n");
    invertedIndex=index(path);
    start = time.time();
    invertedIndex.buildIndex();
    stop = time.time();

    print "Index built in",stop - start

    query_path=raw_input("Enter path of the file containing the queries\n");
    query_terms=invertedIndex.read_lines(query_path);
    for queries in query_terms:
        queryStartTime = time.time();
        query_result = invertedIndex.and_query(queries);
        queryEndTime = time.time();
        print "Results for the Query: %s "% (queries);
        print "Total Docs retrieved: %d"%(len(query_result));
        for docID in query_result:
            print invertedIndex.docIDToFnameMap[docID];
        if(len(query_result)==0):
            print "Query not found"
        print "Retrieved in ",(queryEndTime-queryStartTime)," seconds ";
    print_dictionary = raw_input("Do you want to print dictionary (y/n)\n");
    if(print_dictionary=='y'):
        print "Print dictionary";
        invertedIndex.print_dict();
    print_doc_list = raw_input("Do you want to print doc id to file name list (y/n)\n");
    if (print_doc_list == 'y'):
        print "Print document id to file name list";
        invertedIndex.print_doc_list();

if __name__ == '__main__':
    main()
