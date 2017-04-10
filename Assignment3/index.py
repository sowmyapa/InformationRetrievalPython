#Python 3.0
import re
import os
import collections
import time
import math
from random import randint
from copy import deepcopy
from itertools import groupby


#import other modules as needed

class index:
    def __init__(self, path):
        self.path = path;
        self.inverterIndexMap = {};
        self.docIDToFnameMap = {};
        self.docIDToTermsMap={};
        self.retrievedDocID=[];
        self.rochhioDictionary={};
        self.N=0;

    def rocchio(self, query_terms,queryfrequency, pos_feedback, neg_feedback, alpha, beta, gamma,k):
        # function to implement rocchio algorithm
        # pos_feedback - documents deemed to be relevant by the user
        # neg_feedback - documents deemed to be non-relevant by the user
        # Return the new query  terms and their weights
        if(queryfrequency is None):
            queryfrequency = self.computer_query_frequency(query_terms);
        self.createRocchioDictionary(queryfrequency);
        posNormaliser = 0.0
        if len(pos_feedback)>0:
            posNormaliser = beta/len(pos_feedback);
        negNormaliser = 0.0;
        if len(neg_feedback)>0:
            negNormaliser = gamma/len(neg_feedback);
        relevantDocumentFrequency = self.calculateDocumentVector(pos_feedback,posNormaliser);
        irrelevantDocumentFrequency = self.calculateDocumentVector(neg_feedback,negNormaliser);
        newQueryTerms=self.determineNewWeightedQuery(queryfrequency,relevantDocumentFrequency,irrelevantDocumentFrequency);
        self.determine_k_documents_based_onrocchio_feedback(newQueryTerms,k)
        print(newQueryTerms)
        return newQueryTerms

    def calculateDocumentVector(self,feedBackList,normaliser):
        documentVector={}
        for docID in feedBackList:
            for term in self.docIDToTermsMap[docID]:
                if term in documentVector:
                    value = documentVector[term];
                    documentVector[term] = value + (normaliser*self.docIDToTermsMap[docID][term]);
                else:
                    documentVector[term]=self.docIDToTermsMap[docID][term]*normaliser;
        return documentVector;

    def determineNewWeightedQuery(self,queryfrequency,relevantDocumentFrequency,irrelevantDocumentFrequency):
        newQueryTerms = {};
        for term in self.rochhioDictionary:
            queryValue = 0.0;
            if term in queryfrequency:
                queryValue = queryfrequency[term];
            relevantValue = 0.0;
            if term in relevantDocumentFrequency:
                relevantValue = relevantDocumentFrequency[term];
            irrevalantValue = 0.0;
            if term in irrelevantDocumentFrequency:
                irrevalantValue = irrelevantDocumentFrequency[term];
            weight = queryValue + relevantValue - irrevalantValue;
            if weight > 0.0:
                newQueryTerms[term] = weight
        return newQueryTerms


    def createRocchioDictionary(self,queryfrequency):
        for docID in self.retrievedDocID:
            for term in self.docIDToTermsMap[docID]:
                if term not in self.rochhioDictionary:
                    self.rochhioDictionary[term] = 0;
        for query in queryfrequency:
            if query not in self.rochhioDictionary:
                self.rochhioDictionary[query] = 0;


    def determineTopKDocuments(self,scores,k):
        """function to determine top k documents based on the cosine scores"""
        candidateCounter = 0;
        self.retrievedDocID=[];
        for i in sorted(scores, key=scores.get, reverse=True):
            candidateCounter += 1;
            self.retrievedDocID.append(i);
            print ("Document : " + str(i));
            if (candidateCounter == int(k)):
                break;

    def determine_k_documents_based_onrocchio_feedback(self,new_weighted_query,k):
        scores = {};
        query_length = 0;
        for query in new_weighted_query:
            if query in self.inverterIndexMap:
                termDetailMap=self.inverterIndexMap[query];
                query_tfidf = new_weighted_query[query];
                query_length +=(query_tfidf**2);
                idf=termDetailMap["idf"]
                docDetailsMap = termDetailMap["docIDs"];
                for docID in docDetailsMap:
                    tfid = idf * docDetailsMap[docID]["wtd"];
                    if docID in scores:
                        scores[docID] += tfid * query_tfidf;
                    else:
                        scores[docID] = tfid * query_tfidf;
        query_length = float(math.sqrt(query_length));
        for docID in scores:
            scores[docID] = scores[docID] / (self.docLengths[docID] * query_length);
        self.determineTopKDocuments(scores, k);




    def determine_k_documents_cosine_similarity(self,query_terms,k):
        """function to calculate cosine similarity of documeny wrt query.
        it determines wtd for query terms based n the frequency of query terms in query.
        then for each term in the query it calculates the score for all documents containing the query term.
        then divides above score by length of query and document for each document."""

        queryfrequency = self.computer_query_frequency(query_terms);
        query_length = 0;
        scores = {};
        for query in queryfrequency:
            if query in self.inverterIndexMap:
                termDetailMap=self.inverterIndexMap[query];
                idf=termDetailMap["idf"]
                query_tfidf=idf*(1+math.log10(queryfrequency[query]));
                query_length+=(query_tfidf**2);
                docDetailsMap=termDetailMap["docIDs"];
                docList = termDetailMap["docIDs"]
                for docID in docList:
                    tfid=idf*docDetailsMap[docID]["wtd"];
                    if docID in scores:
                        scores[docID]+=tfid*query_tfidf;
                    else:
                        scores[docID] = tfid * query_tfidf;
        query_length=float(math.sqrt(query_length));
        for docID in scores:
            scores[docID]=scores[docID]/(self.docLengths[docID]*query_length);
        self.determineTopKDocuments(scores,k);


    def read_lines(self, filename):
        """This function return a list of all lines in the given file"""
        query_terms = [];
        for l in open(filename, 'rt').readlines():
            query_word=l.strip().lower();
            if query_word not in self.stop_words:
                query_terms.append(query_word);
        return query_terms;

    def process_stop_words(self,stop_words_path):
        """This function reads the file containing all stop words and stores them in a list."""
        self.stop_words=[];
        for l in open(stop_words_path, 'rt').readlines():
            self.stop_words.append(l.strip().lower());

    def compute_IDF_WTD_doclengths(self,N):
        """Calculates the document length of each document by adding the square of tdif value for each term in the document
        and taking the final sum's sqrt value."""
        self.docLengths = [0] * N;
        for key in self.inverterIndexMap:
            termMap = self.inverterIndexMap[key];
            termMap["idf"] = math.log10(N / termMap["idf"]);
            docListMap = termMap["docIDs"];
            for docID in docListMap:
                docDetailMap = docListMap[docID];
                termFrequency = docDetailMap["wtd"];
                if (termFrequency != 0):
                    docDetailMap["wtd"] = float(1 + math.log10(termFrequency));
                    self.docIDToTermsMap[docID][key]=termFrequency;
                    self.docLengths[docID] = self.docLengths[docID] + ((termMap["idf"] * docDetailMap["wtd"]) ** 2);
        for i in range(len(self.docLengths)):
            self.docLengths[i] = float(math.sqrt(self.docLengths[i]));



    def buildIndex(self):
        # function to read documents from collection, tokenize and build the index with tokens
        # implement additional functionality to support methods 1 - 4
        # use unique document integer IDs
        """It creates an index of the following structure :
           "{"term1": {"idf":1.0,
                    "docIDs":{
                              "1":{"wtd":1.3,
                                   "positions":[101,103,230]
                                   },
                              "15":{"wtd":1.2,
                                    "positions":[25,30]
                                   }
                              }
                   },
             "term2": {"idf":1.2,
                      "docIDs":{
                              "5":{"wtd":1.3,
                                   "positions":[101,103,230]
                                   },
                              "10":{"wtd":1.2,
                                    "positions":[25,30]
                                   }
                              }
                   }
            }
        files = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]"""

        fileNames = []
        fileContent=[]
        rFile = re.compile("\*+TEXT \d")
        with open(self.path) as files:
            for k, g in groupby(files, key=lambda x: rFile.search(x)):
                if not k:
                    # print list(g)
                    fileContent.append(list(g))
                if k:
                    # print list(g)
                    fileNames.append(list(g))


        docID = 1;
        for fname in fileContent:
            pos = 1;
            fileNameLines = [line.rstrip('\n') for line in fileNames[docID-1]]

            for eachLine in fileNameLines:
                wordList = re.split('\W+', eachLine)

            self.docIDToFnameMap[docID] = wordList[2];
            self.docIDToTermsMap[docID] = {};
            lines = [line.rstrip('\n') for line in fname]

            #for l in open(os.path.join(self.path, fname), 'rt').readlines():
            for eachLine in lines:
                eachLine.strip();
                for word in re.split('\W+', eachLine.lower()):
                    if (word != '' and word not in self.stop_words):
                        termMap=self.docIDToTermsMap[docID];
                        termMap[word]=0.0;
                        if (word in self.inverterIndexMap):
                            tokenMapValue = self.inverterIndexMap[word];
                            docListMap = tokenMapValue["docIDs"];
                            if (docID in docListMap):
                                docDetailMap = docListMap[docID];
                                docDetailMap["wtd"]=docDetailMap["wtd"]+1;
                                docDetailMap["positions"].append(pos);
                            else:
                                tokenMapValue["idf"]=tokenMapValue["idf"]+1;
                                docListMap[docID]={"wtd":1.0,"positions":[pos]}
                        else:
                            self.inverterIndexMap[word] = {"idf": 1.0, "docIDs":{docID:{"wtd":1,"positions":[pos]}}};
                        pos += 1;
            docID += 1;
        self.compute_IDF_WTD_doclengths(docID);
        self.N=len(self.docIDToFnameMap);


    def computer_query_frequency(self,query_terms):
        """Determine the occurence of each term in query."""
        queryfrequency = {}
        for word in re.split('\W+', query_terms.lower()):
            if (word != '' and word not in self.stop_words):
                if word in queryfrequency:
                    queryfrequency[word] = queryfrequency[word] + 1;
                else:
                    queryfrequency[word] = 1;
        return queryfrequency


    def query(self, query_terms, k):
        #function for exact top K retrieval (method 1)
	    #Returns at the minimum the document names of the top K documents ordered in decreasing order of similarity score
        self.determine_k_documents_cosine_similarity(query_terms,k);

    def print_doc_list(self):
        #function to print the documents and their document id
        for key in self.docIDToFnameMap:
            print ("Doc ID:"+str(key)+" ==> "+str(self.docIDToFnameMap[key]));

    def print_dict(self):
        #function to print the terms and posting list in the index
        for key in self.inverterIndexMap:
            termMap = self.inverterIndexMap[key];
            output=key+":["+str(termMap["idf"])+",(";
            docList = termMap["docIDs"];
            for docID in docList:
                output+=str(docID)+","+str(docList[docID]["wtd"])+","+str(docList[docID]["positions"])+"),";
            print (output+"]");

    def executeQuery(self,query_terms):
        k = input("Enter number of documents to be retrieved\n");
        for query in query_terms:
            print("output for query : ", query);
            self.query(query, k);
            run = True;
            queryFrequency = None
            retrievalType = input("Enter 1 for rocchio user feedback, 2 for psuedo-relevance, anything else to exit\n");
            while (run):
                if (retrievalType == '1'):
                    numberOfRelevant = int(input("Enter number of relevant documents \n"))
                    relevantDocIDS = [];
                    for i in range(0, numberOfRelevant):
                        relevantDocIDS.append(int(input("Enter relevant docID\n")))
                    numberOfIrrelevant = int(input("Enter number of irrelevant documents \n"))
                    irrelevantDocIDS = [];
                    for i in range(0, numberOfIrrelevant):
                        irrelevantDocIDS.append(int(input("Enter irrelevant docID\n")))
                    queryStartTime = time.time();
                    queryFrequency = self.rocchio(query,queryFrequency, relevantDocIDS, irrelevantDocIDS, 1.0, 0.75, 0.15, k);
                    queryEndTime = time.time();
                    print("Retrieved in ", (queryEndTime - queryStartTime), " seconds \n");
                elif (retrievalType == '2'):
                    queryStartTime = time.time();
                    relevantDocIDS = []
                    for i in range(0, 3):
                        relevantDocIDS.append(self.retrievedDocID[i]);
                    queryFrequency = self.rocchio(query,queryFrequency, relevantDocIDS, [], 1.0, 0.75, 0.15, k);
                    queryEndTime = time.time();
                    print("Retrieved in ", (queryEndTime - queryStartTime), " seconds \n");
                else:
                    run = False;
                exitStatus = input("Enter 3 to exit else press anything else to run another iteration\n");
                if(exitStatus == '3'):
                    run = False;


def main():
    #stop_words_path = input("Enter path of file containing stop words\n");
    stop_words_path="/Users/sowmyaparameshwara/college/InformationRetrievalPython/Assignment3/time/TIME.STP";
    #path = input("Enter directory path containing all documents\n");
    path = "/Users/sowmyaparameshwara/college/InformationRetrievalPython/Assignment3/time/TIME.ALL";
    invertedIndex=index(path);
    invertedIndex.process_stop_words(stop_words_path);
    start = time.time();
    invertedIndex.buildIndex();
    stop = time.time();
    print ("Index built in",stop - start);

    #query_path=input("Enter path of the file containing the queries\n");
    query_path="/Users/sowmyaparameshwara/college/InformationRetrievalPython/Assignment3/queries.txt"
    query_terms=invertedIndex.read_lines(query_path);
    invertedIndex.executeQuery(query_terms);

    print_dictionary = input("Do you want to print dictionary (y/n)\n");
    if (print_dictionary == 'y'):
        print ("Print dictionary");
        invertedIndex.print_dict();
    print("inverted index dictionary length ",len(invertedIndex.inverterIndexMap));

    print_doc_list = input("Do you want to print doc id to file name list (y/n)\n");
    if (print_doc_list == 'y'):
        print ("Print document id to file name list");
        invertedIndex.print_doc_list();



if __name__ == '__main__':
    main()
