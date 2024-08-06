# Learning About Blockchain
 Projects that familiarize me with blockchain technology


blockchain_mock.py : 

I code a mock blockchain using python. I cover basic blockchain concepts like blocks, hashes and chaining. 
I create a class 'SandDollarBlock' which represents a fictious cryptocurency block. 
I define the constructor of SandDollarBlock which takes in self, previous_block_hash, and the transaction_list. Using this constructor, one can create the structure of each block, containing: unique data and an original hash or digital signature. 

This solves the problem of forging transactions. Each block relies on the last to create its hash, if the buyer or sellers hash does not match, something has been changed. 

Video that suppourted my learning:  
https://www.youtube.com/watch?v=pYasYyjByKI
