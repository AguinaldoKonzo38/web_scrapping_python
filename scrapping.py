from jobartis import scrapping_jobartis
from jobartis import search_keyword
# a import save_to_csv


def get_jobs(keyword):
    result_jobartis = search_keyword(keyword)
    all_result = result_jobartis
    return all_result
