# scrap-science
A bunch of Jupyter notebooks to scrap some of the most popular web platforms for scientific papers.


## Setup
* python environment
* chrome driver
* pdf2txt

## arxiv
1. get all search result urls and their corresponding number of search results
2. dump these into scrap_arvix.ipynb and get a clean duplicate free list of urls of individual papers
3. get all pdfs
4. scarp data
5. manula quality check

## bioRxiv
1. get all search result urls and their corresponding number of search results
2. dump these into scrap_biorxiv.ipynb and get a clean duplicate free list of urls of individual papers
3. now scarp - this step includes getting the pdf too.
4. manual quality check

## Pubmed
1. search pubmed and download results as .csv into raw_result folder
2. use scrap_pubmed.ipynb to combine all csv's, remove duplicates and finally scrap it (no pdfs)
3. save as .csv and do manual search quality check

## MICCAI
1. get content pdfs from springer
* 2014 and 2015 - get urls manually
* 2016 and 2017 - pdfs have urls in them
2. run getMiccaiUrls.py to get the urls in the pdf and dump them in a list as a .npy file
3. read these in scrap_miccai.ipynb and add to them those hardcoded from 2014 and 2015
4. run scrap_miccai.ipynb (no pdfs)

## IEEE
1. go to http://ieeexplore.ieee.org/Xplore/home.jsp
2. enter keywords and download .csv. Link to search will be in the first row.
3. combine and clean the multiple downloaded .csv's using combine_Ieee.ipynb. This produces a single ieee.csv without duplicates.
4. run scrap_ieee.ipynb. We first get as much pdf as we can, then we loop through the csv and convert pdf2txt to get emails. 
5. manual cleanup
