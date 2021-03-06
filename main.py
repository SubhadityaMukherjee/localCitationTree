import glob
import string

from scholarly import scholarly
from tqdm import tqdm


def grab_info(qu):
    # grabs info for 1 query
    search_query = scholarly.search_pubs(qu)
    pap1 = next(search_query)
    return pap1


def grab_related(cp, max_no=10):
    # grab max_no number of papers that are the highest cited amongst the
    #ones that cite the initial paper and their information
    cites = []
    count = 0
    for citation in tqdm(scholarly.citedby(cp), total=max_no):
        if count > max_no:
            break
        else:
            cites.append(citation)
        count += 1

    return cites


def grab_paper_links(lis):
    # grab the paper links from a list of returned info. Eg from the output of grab_related
    if type(lis) == dict:
        return lis['eprint_url']
    else:
        return [x['eprint_url'] for x in lis]


def get_citation_counts(lis):
    if type(lis) == dict:
        return lis['num_citations']
    else:
        return [(x['num_citations'], x['bib']) for x in lis]

#  name_sc = "The Consciousness Prior"
#  cp = grab_info(name_sc)
#  print(cp)
#  related = grab_related(cp, 3)
#  print(related)
#  print(grab_paper_links(related))
#  print(grab_paper_links(cp))
#  print(get_citation_counts(related))
#  print(get_citation_counts(cp))
