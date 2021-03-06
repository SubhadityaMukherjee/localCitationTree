# Local Citation Tree

- Every wanted to grab related papers from google scholar easily? 
- How about getting a list of citation counts and related bibtext information directly
- Heres a library of sorts for doing exactly that

## How to run

- Just open the notebook, change the name_sc variable and you are good to go
- The script works too. Just uncomment the lines you need and you are good to go

## Requirements
- This requires scholarly and tqdm
- pip install -r requirements.txt

## What is provided
- grab_related(cp, max_no=10): grab max no number of papers that are the highest cited amongst the ones that cite the initial paper and their information 
- grab_paper_links(lis) : grab the paper links from a list of returned info. Eg from the output of grab_related
- get_citation_counts(lis): get all the citation counts for a list or single object. Eg returned from either of the functions before

## Usage

- The function names are pretty self explantory
- You can refer to the notebook provided for examples

## Contributions

- Feel free to suggest changes or add features
