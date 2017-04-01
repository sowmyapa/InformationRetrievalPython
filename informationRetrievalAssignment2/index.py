#Python 3.0
import re
import os
import collections
import time
import math
from random import randint
from copy import deepcopy

#import other modules as needed

class index:
    def __init__(self, path):
        self.path = path;
        self.inverterIndexMap = {};
        self.docIDToFnameMap = {};
        self.championList={};
        self.docIDToTermsMap={};
        self.N=0;

    def determine_threshold(self,idf,length):
        """function to determine r value for creating champion list"""
        return min(20,length);

    def createRandomLeaders(self):
        """function for creating cluster leaders using random number generator"""
        randint(0, len(self.docIDToFnameMap) - 1)
        self.leaders = {};
        for i in range(math.floor(math.sqrt(self.N))):
            random_number = randint(0, len(self.docIDToFnameMap) - 1);
            while (random_number in self.leaders):
                random_number = randint(0, len(self.docIDToFnameMap) - 1);
            else:
                self.leaders[random_number] = [];

        return self.leaders;


    def determineTopKDocuments(self,scores,k):
        """function to determine top k documents based on the cosine scores"""
        candidateCounter = 0;
        for i in sorted(scores, key=scores.get, reverse=True):
            candidateCounter += 1;
            print ("Document : " + self.docIDToFnameMap[i]);
            if (candidateCounter == int(k)):
                break;
        print ("candidateCounter",candidateCounter);

    def determine_k_documents_cosine_similarity(self,query_terms,queryfrequency,k,is_champion_search):
        """function to calculate cosine similarity of documeny wrt query.
        it determines wtd for query terms based n the frequency of query terms in query.
        then for each term in the query it calculates the score for all documents containing the query term.
        then divides above score by length of query and document for each document."""
        if(queryfrequency is None):
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
                if(is_champion_search):
                    docList = self.championList[query];
                else:
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


    def createClusters(self):
        """Creates clusters of documents based on cosine score.
        1) Generates random cluster leader = sqrt(N)
        2) For each document which is not a leader it calculates the document cosine score with all leaders.
        3) Takes the leader with highest cosine score and becomes it's follower."""
        self.createRandomLeaders();
        for followerDocID in self.docIDToTermsMap:
            if followerDocID not in self.leaders:
                scores={}
                followerDOCTermsMap=self.docIDToTermsMap[followerDocID];
                for terms in followerDOCTermsMap:
                    query_tfidf = self.docIDToTermsMap[followerDocID][terms];
                    for leaderDocID in self.leaders:
                        if(terms in self.docIDToTermsMap[leaderDocID]):
                            tfid = self.docIDToTermsMap[leaderDocID][terms];
                            if leaderDocID in scores:
                                scores[leaderDocID]+=tfid*query_tfidf;
                            else:
                                scores[leaderDocID]=tfid*query_tfidf;
                for docInScores in scores:
                    scores[docInScores] = scores[docInScores] / (self.docLengths[docInScores] * self.docLengths[followerDocID]);
                for i in sorted(scores, key=scores.get, reverse=True):
                    followerList = self.leaders[i];
                    followerList.append(followerDocID);
                    break;


    def buildChampionList(self):
        """Builds the champion list for each term in the dictionary by taking the top "r" documents
        in the posting list with highes wtd value."""
        for terms in self.inverterIndexMap:
            docDetailsMap=self.inverterIndexMap[terms]["docIDs"];
            threshold = self.determine_threshold(self.inverterIndexMap[terms]["idf"], len(docDetailsMap));
            tempList=[-1]*threshold;
            counter=0;
            for i in sorted(docDetailsMap, key=lambda x: docDetailsMap[x]["wtd"],reverse=True):
                if (counter == threshold):
                    break;
                tempList[counter]=i;
                counter+=1;
            self.championList[terms]=tempList;



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
            self.stop_words.append(l.strip());

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
                    self.docIDToTermsMap[docID][key]=docDetailMap["wtd"]*termMap["idf"];
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
            }"""
        files = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]
        docID = 0;
        for fname in files:
            pos = 1;
            self.docIDToFnameMap[docID] = fname;
            self.docIDToTermsMap[docID] = {};
            for l in open(os.path.join(self.path, fname), 'rt').readlines():
                l.strip();
                for word in re.split('\W+', l.lower()):
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


    def exact_query(self, query_terms, k):
        #function for exact top K retrieval (method 1)
	    #Returns at the minimum the document names of the top K documents ordered in decreasing order of similarity score
        self.determine_k_documents_cosine_similarity(query_terms,None,k,False);

    def inexact_query_champion(self, query_terms, k):
        # function for exact top K retrieval using champion list (method 2)
        # Returns at the minimum the document names of the top K documents ordered in decreasing order of similarity score
        self.determine_k_documents_cosine_similarity(query_terms,None,k,True);


    def inexact_query_index_elimination(self, query_terms, k):
        # function for exact top K retrieval using index elimination (method 3)
        # Returns at the minimum the document names of the top K documents ordered in decreasing order of similarity score
        """It determines unique terms in the query, and sorts he query terms by idf value and picks the top half of query terms for
        calculating cosine similarity."""
        queryfrequency = {}
        for word in re.split('\W+', query_terms.lower()):
            if (word != '' and word not in self.stop_words):
                if word in queryfrequency:
                    lst=list(queryfrequency[word]);
                    lst[0]=lst[0]+1;
                    queryfrequency[word]=tuple(lst);
                else:
                    queryfrequency[word] = (1,self.inverterIndexMap[word]["idf"]);
        new_query_terms="";
        counter=0;
        new_query_terms_frequency={};
        number_of_terms=math.ceil(len(queryfrequency)/2.0);
        for query in sorted(queryfrequency,key=lambda x: queryfrequency[x][1],reverse=True):
            if(counter==number_of_terms):
                break;
            new_query_terms_frequency[query]=queryfrequency[query][0];
            new_query_terms=new_query_terms+" "+query;
            counter+=1;
        self.determine_k_documents_cosine_similarity(new_query_terms,new_query_terms_frequency,k,False);

    def determineCandidateSet(self,scores,k):
        """For cluster pruning determines candidate set by picking the leader and it's follower with highest score,
        if we dont have enough documents for answering the query, it picks the next best leader and it's followers, so on
        untill we have enough documents for answering the query."""
        counter = 0;
        candidateSet = []
        for i in sorted(scores, key=scores.get, reverse=True):
            if (counter >= int(k)):
                break;
            else:
                candidateSet.append(i);
                counter += 1;
                for followers in self.leaders[i]:
                    candidateSet.append(followers);
                    counter += 1;
        return candidateSet;

    def determineCandidateScores(self,queryfrequency,candidateSet,queryscores,query_length):
        """It calculates cosine score of the query with all the documents
        determined in candidate set."""
        candidateScores={}
        for query in queryfrequency:
            for docID in candidateSet:
                tfid=0.0;
                if query in self.docIDToTermsMap[docID]:
                    tfid=self.docIDToTermsMap[docID][query];
                if docID in candidateScores:
                    candidateScores[docID]+=tfid*queryscores[query];
                else:
                    candidateScores[docID] = tfid * queryscores[query];
        for docID in candidateScores:
            candidateScores[docID] = candidateScores[docID] / (self.docLengths[docID] * query_length);
        return candidateScores;


    def inexact_query_cluster_pruning(self, query_terms, k):
        #function for exact top K retrieval using cluster pruning (method 4)
        #Returns at the minimum the document names of the top K documents ordered in decreasing order of similarity score
        """This functions calculates cosine score of the query with all leaders of the cluster. It picks the candidate set basesd
        on these scores. Uses the candidate set to determine top k documents for the query."""
        queryfrequency = self.computer_query_frequency(query_terms);
        query_length = 0;
        scores = {};
        queryscores={};
        for query in queryfrequency:
            termDetailMap=self.inverterIndexMap[query];
            idf=termDetailMap["idf"]
            query_tfidf=idf*(1+math.log10(queryfrequency[query]));
            queryscores[query]=query_tfidf;
            query_length+=(query_tfidf**2);
            for docID in self.leaders:
                tfid =0.0;
                if query in self.docIDToTermsMap[docID]:
                    tfid=self.docIDToTermsMap[docID][query];
                    if docID in scores:
                        scores[docID]+=tfid*query_tfidf;
                    else:
                        scores[docID] = tfid*query_tfidf;
        query_length=float(math.sqrt(query_length));
        for docID in scores:
            scores[docID]=scores[docID]/(self.docLengths[docID]*query_length);
        candidateSet=self.determineCandidateSet(scores,k);
        candidateScores=self.determineCandidateScores(queryfrequency,candidateSet,queryscores,query_length);
        self.determineTopKDocuments(candidateScores,k);

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

def main():
    stop_words_path = input("Enter path of file containing stop words\n");
    #stop_words_path="/Users/sowmyaparameshwara/Desktop/Assignments/IR_Assignments/informationRetrievalAssignment2/stop-list.txt";
    path = input("Enter directory path containing all documents\n");
    #path = "/Users/sowmyaparameshwara/Desktop/Assignments/IR_Assignments/informationRetrievalAssignment2/collection";
    invertedIndex=index(path);
    invertedIndex.process_stop_words(stop_words_path);
    start = time.time();
    invertedIndex.buildIndex();
    stop = time.time();
    print ("Index built in",stop - start);

    start = time.time();
    invertedIndex.buildChampionList();
    stop = time.time();
    print ("Champion List built in", stop - start);


    start = time.time();
    invertedIndex.createClusters();
    stop = time.time();
    print ("Cluster created in", stop - start);

    query_path=input("Enter path of the file containing the queries\n");
    #query_path="/Users/sowmyaparameshwara/Desktop/Assignments/IR_Assignments/informationRetrievalAssignment2/queries.txt"
    query_terms=invertedIndex.read_lines(query_path);
    search_strategy=input("Enter 1 for exact search, 2 for champion list, 3 for index elimination, 4 for Cluster Pruning\n");
    k=input("Enter number of documents to be retrieved\n");
    for query in query_terms:
        queryStartTime = time.time();
        print ("output for query : ", query);
        if(search_strategy=="1"):
            invertedIndex.exact_query(query,k);
        elif(search_strategy=="2"):
            invertedIndex.inexact_query_champion(query,k);
        elif(search_strategy=="3"):
            invertedIndex.inexact_query_index_elimination(query,k);
        elif (search_strategy == "4"):
            invertedIndex.inexact_query_cluster_pruning(query, k);
        queryEndTime = time.time();
        print ("Retrieved in ",(queryEndTime-queryStartTime)," seconds ");

    print_dictionary = input("Do you want to print dictionary (y/n)\n");
    if (print_dictionary == 'y'):
        print ("Print dictionary");
        invertedIndex.print_dict();
    print_doc_list = input("Do you want to print doc id to file name list (y/n)\n");
    if (print_doc_list == 'y'):
        print ("Print document id to file name list");
        invertedIndex.print_doc_list();



if __name__ == '__main__':
    main()
