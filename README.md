# scrap-science
A bunch of Jupyter notebooks to scrap some of the most popular web platforms for scientific papers.


## Setup
* python environment
* chrome driver



## MICCAI
1. Get content pdfs from springer
* 2014 and 2015 - get urls manually
* 2016 and 2017 - pdfs have urls in them
2. run getMiccaiUrls.py to get the urls in the pdf and dump them in a list sa a .npy file
3. read these in scrap_miccai.ipynb and add to them thos from 2014 and 2015
4. run scrap_miccai.ipynb

## IEEE
1. Go to http://ieeexplore.ieee.org/Xplore/home.jsp
2. Enter keywords and download .csv. Link to search will be in the first row.
3. Combine and clean the multiple downloaded .csv's using combine_Ieee.ipynb. This produces a single .csv without duplicates.
4. Run scrap_ieee.ipynb. We first get as much pdf as we can, then we loop through the csv and convert pdf2txt to get emails. 
