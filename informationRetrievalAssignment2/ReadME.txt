================================================================================================================================
                                                  How to Execute
================================================================================================================================

1) Go inside the directory in terminal:
   ex : cd /Users/sowmyaparameshwara/Desktop/Assignments/IR_Assignments/Assignment2
2) Type the following command :
   python3 index.py
3) You will be prompted to enter the path of the file containing stop words :
   Ex : Enter path of file containing stop words
        /Users/sowmyaparameshwara/Desktop/Assignments/IR_Assignments/informationRetrievalAssignment2/stop-list.txt
4) You will be prompted to enter the path of the directory containing document collection:
   Ex : Enter directory path containing all documents
        /Users/sowmyaparameshwara/Desktop/Assignments/IR_Assignments/informationRetrievalAssignment2/collection
5) You will be prompted to enter the file path which containes queries. (File has each query in a different line) :
   Ex : Enter path of the file containing the queries
        /Users/sowmyaparameshwara/Desktop/Assignments/IR_Assignments/informationRetrievalAssignment2/queries.txt
6) You will be prompted to choose the retrieval method:
   Ex: Enter 1 for exact search, 2 for champion list, 3 for index elimination, 4 for Cluster Pruning
       1
7) You will be prompted to choose the number of documents to be retrieved:
   Ex : Enter number of documents to be retrieved
        10
8) It outputs the query result and asks if you wish to print dictionary (Enter 'y' if you wish to print else 'n'):
   Ex : Do you want to print dictionary (y/n)
        y
9) It outputs dictionary and asks if you wish to print docID to fileName mapping (Enter 'y' if you wish to print else 'n'):
   Ex : Do you want to print doc id to file name list (y/n)
        y
10) It outputs the docID to filename mapping.
11) Rerun the program, with command "python3 index.py", to run for a different retrieval startegy.


================================================================================================================================
                                                      Refer
================================================================================================================================

 1) Sample queries :
    queries.txt
 2) Output generated by my code :
    output.txt

================================================================================================================================
                                                    Index Structure
================================================================================================================================
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

================================================================================================================================
