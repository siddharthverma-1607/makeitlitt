"""
Tasks:
1. Scrap data from each URL
2. Get question and question vote count
3. Check total Answers present in page
    If present:
        1. Get Answer and anser vote count
        2. Scrap code from answer
        3. Display answer and vote count

4. Argumrents to get detailed or summarized results [flag]
5. Check for exceptions and internet connection 
6. Create snippet result for a quick view for user
7. ADD 'Beautify; - [Optional Parameter] to print snippet in a box
8. ADD functionality: 
    > to let user see answer 1 by 1, by clicking Enter for next or Press 'X' to break and move to next PAGE
    > Press 'ESC' to end loop off PAGE
9. ADD 'result' to get the complete output as a STRING, instead of printing result
"""
# --------------------- IMPORTS -----------------------
import requests
import re
from bs4 import BeautifulSoup as bs

# -------------------- Decorator Function For highlighting answer body --------------------------


def highlight(char='-', n=0):
    if n == 1:
        print("\n" + char*100)
    elif n == 2:
        print(char*100 + "\n")
    else:
        print(char * 100)


def get_google_searchResult_Links(query, website=0):
    """
    Method to get urls results from google search engine

    Parameters:
    query [STRING]: stack overflow query to search.
    website [STRING]: To filter the result based on a particular website.
                    [Default]: 0 --> Get All results

    Return:
    result_links [List]:
        [...,] - Result Urls scraped for the search page
        [-1] - If no result found for filtered website with requested query
        [0] - If no result found on the Internet
    """

    result_links = []

    # Add Try and Except to check for internet and other exceptions
    try:
        page = requests.get("https://www.google.dz/search?q="+query)
    except Exception as e:
        #print("ConnectionError: Please check your system is connected to a network.")
        if e.__class__.__name__ == "ConnectionError":
            raise SystemExit(
                "ConnectionError! Please check your system is connected to a network.")
        else:
            raise SystemExit(e)

    soup = bs(page.content, features="html.parser")
    links = soup.findAll("a")

    if website == 0:
        # Return all search result as no website filter applied
        result_links = [re.split(":(?=http)", link["href"].replace("/url?q=", ""))[0].split(
            '&')[0] for link in soup.find_all("a", href=re.compile("(?<=/url\?q=)(htt.*://.*)"))]

        if len(result_links) == 2:
            # If no result found on the Internet
            # We will always get 2 urls because of the google support links present in the search page
            return [0]
        else:
            return result_links

    for link in soup.find_all("a", href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
        result = re.split(":(?=http)", link["href"].replace("/url?q=", ""))
        if result[0].find(website) != -1:
            # Check if result contains url with filtered website
            result_links.append(result[0].split('&')[0])

    if len(result_links) == 0:
        # No result found for filtered website with requested query
        return [-1]
    else:
        return result_links

# ----------------------------------------------


def scrap_stackoverflow_page(page, ans_format):
    """
    Method to scrap the Stack Overflow page and return the required fields

    Parameters:
    page [Beautifulsoup obj]: HTML page as Beautifulsoup obj to be scrapped
    ans_format [INT]: 
        0 - Display only code snippets from answer (DEFAULT)
        1 - Display detailed answer

    Return:
    [-1,stackoverflow_page_title]: No Answer for the query in current stack overflow page
    [1,{stackoverflow_page_title, answer_count,all_votes, answer_body} ]: DETAILED[1] Format, Answer Present for the query in current stack overflow page
    [0,{stackoverflow_page_title, answer_count,all_votes, answer_body} ]: SNIPPET[0] Format, Answer Present for the query in current stack overflow page
    """

    # Title of the page
    stackoverflow_page_title = ' '.join(
        page.find("title").get_text(strip=True).split('-')[0:-1])

    # Total number of answers on the page
    answer_count = page.find(
        "h2", {'data-answercount': True}).get_text(strip=True).split()[0]

    # No answer for current page
    #print("scrap_stackoverflow_page() --> No answer for current page")
    if answer_count == '0':
        return [-1, stackoverflow_page_title]

    # First Vote is for the Question, rest are for answers
    # So, all_votes - 1 = answer_count
    all_votes = [vote.get_text(strip=True) for vote in page.find_all(
        "div", class_='js-vote-count flex--item d-flex fd-column ai-center fc-black-500 fs-title')]

    # post_body contains question body + answer body
    # Just taking answer body by [1:]
    answer_body = page.find_all("div", class_='s-prose js-post-body')[1:]

    # DETAILED answer requested in arguments
    if ans_format == 1:
        return [1, {'stackoverflow_page_title': stackoverflow_page_title, 'answer_count': answer_count, 'all_votes': all_votes, 'answer_body': answer_body}]

    # Summarised CODE SNIPPETS requested in arguments
    if ans_format == 0:
        #print("scrap_stackoverflow_page() --> Snippet Summarized format answer returned")
        answer_per_snippet_collection = []

        # Traversing each answer present in current page
        for body in answer_body:
            snippet_collection = []
            #print("Code Block, Total Snippets in ans->",len(body.find_all("pre")))

            # Traversing each Code Snippet in an answer
            for snippet in body.find_all("pre"):
                #print("Inside Snnippet loop\n\nSnippert containts->",len(snippet.get_text()))
                snippet_collection.append(snippet.get_text())
            answer_per_snippet_collection.append(snippet_collection)

        return[0, {'stackoverflow_page_title': stackoverflow_page_title, 'answer_count': answer_count, 'all_votes': all_votes, 'answer_body': answer_per_snippet_collection}]


# ----------------------------------------------


def get_stackoverflow_result(query, limit=2, **parameters):
    """
    Method to show stack overflow results.

    Parameters:
    query [STRING]: stack overflow query to search
    limit [INT]: Number of results to display per page (DEFAULT - 2)

    Optional keyword arguments::
    ans_format [INT]: 
        0 - Display only code snippets from answer (DEFAULT)
        1 - Display detailed answer
    """

    default_parameters = {'ans_format': 0}
    # parameter check & update
    for parameter_key in parameters.keys():
        if parameter_key not in ['ans_format']:
            raise TypeError(
                "'{}' is an invalid keyword argument for get_myString() \nFor more details for valid parameters try:\nhelp(get_myString) OR\nget_myString.__doc__", parameter_key)

        else:
            default_parameters[parameter_key] = parameters[parameter_key]

    query_links = get_google_searchResult_Links(
        query+" stack overflow", 'stackoverflow.com')

    # Check if stackoverflow results exists
    if query_links[0] == -1 or query_links[0] == 0:
        # No results found with query
        return "No Stack Overflow result for Query. :(\nPlease Try again by modifying the query!"

    else:
        page_count = 0
        # Results found with query search
        # To run test for  result

        highlight(char='*', n=1)
        highlight(char='*')
        print("Stack Overflow Results:")
        highlight(char='*')

        for url in query_links[0:2]:
            page_count += 1
            resp = requests.get(url)
            #print(url + " --> Status Code: " + str(resp.status_code))
            soup = bs(resp.text, features="html.parser")

            #print("Hitting scrap_stackoverflow_page() with ans_format= ",default_parameters["ans_format"])
            page_result = scrap_stackoverflow_page(
                soup, default_parameters["ans_format"])

            # -----------------------------------------------------------------
            # --------------------  NO ANSWER PRESENT -------------------------
            # -----------------------------------------------------------------
            if page_result[0] == -1:
                # No Answer for the query in current stack overflow page
                highlight(n=1)
                print(
                    f"Page {page_count} Title - ", page_result[1])
                print("\n\t----> NO ANSWERS PRESENT for Current Page <-----")
                highlight(n=2)

            # -----------------------------------------------------------------
            # -----------------  DETAILED ANSWER FORMAT -----------------------
            # -----------------------------------------------------------------
            elif page_result[0] == 1:
                # DETAILED[1] Answer Present for the query in current stack overflow page
                page_details = page_result[1]
                #{'stackoverflow_page_title': stackoverflow_page_title, 'answer_count': answer_count, 'all_votes': all_votes, 'answer_body': answer_body}

                highlight(n=1)
                highlight()
                print(
                    f"Page {page_count} Title - ", page_details["stackoverflow_page_title"])
                print(
                    f"Page Vote: {page_details['all_votes'][0]} | \tTotal Answers Present: {page_details['answer_count']} | \tAnswer Limit: {limit} | \tFormat: DETAILED")

                ans_count = 0
                for body in page_details['answer_body'][0:limit]:
                    ans_count += 1
                    highlight(char='*', n=1)
                    print(
                        f"--> ANSWER VOTES: {page_details['all_votes'][ans_count]} <--")
                    print(body.get_text())
                    highlight(char='*', n=2)

                highlight(n=1)

            # -----------------------------------------------------------------
            # -----------------  SNIPPET ANSWER FORMAT -----------------------
            # -----------------------------------------------------------------
            elif page_result[0] == 0:
                # Summarised CODE SNIPPETS[0] Answer Present for the query in current stack overflow page
                page_details = page_result[1]
                #{'stackoverflow_page_title': stackoverflow_page_title, 'answer_count': answer_count, 'all_votes': all_votes, 'answer_body': answer_body}

                highlight(char="*")
                print(
                    f"\nPage ({page_count}) TITLE - ", page_details["stackoverflow_page_title"])
                print(
                    f"Page Vote: {page_details['all_votes'][0]} | \tTotal Answers Present: {page_details['answer_count']} | \tAnswer Limit: {limit} | \tFormat: CODE-SNIPPET")

                ans_count = 0  # To count the answer number and get votes based on index
                limit_breaker = 0  # To check the number of answer printed and break when reached limit

                # print(page_details['answer_body'])
                for snippet_collection in page_details['answer_body']:
                    # snippet_collection is list of all snippets present in that answer
                    ans_count += 1

                    # Skip if no snippet in the answer
                    if len(snippet_collection) == 0:
                        continue

                    # Incrementing limit breaker only for printed answer
                    limit_breaker += 1
                    highlight(n=1)
                    print(
                        f"--> ANSWER No. {ans_count} || VOTES: {page_details['all_votes'][ans_count]} <--")

                    # Traversing all snippets in snippet_collection of answer
                    for snippet in snippet_collection:
                        print(snippet)
                        print("."*100)

                    highlight(n=2)

                    # Break if limit for answer to be displayed is reached
                    if limit_breaker == limit:
                        break


# ------------------------------------------------
if __name__ == '__main__':
    print("Process Initiated:")
    #query = "create lambda function in python" + " stack overflow"
    query = "create lambda function in python"
    #query_with_noAnswers = "Hybris navigation component anatomy"
    # query="sa5d64sa6"
    #website = 'stackoverflow.com'
    # print(*get_google_searchResult_Links(query,website),sep="\n")
    # scrap_stackoverflow_page(query)
    get_stackoverflow_result(query, ans_format=0)
    #get_stackoverflow_result(query_with_noAnswers, ans_format=1)
