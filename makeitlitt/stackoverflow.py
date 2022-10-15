"""
Tasks:
1. Scrap data from each URL -- DONE
2. Get question and question vote count -- DONE
3. Check total Answers present in page -- DONE
    If present:
        1. Get Answer and anser vote count -- DONE
        2. Scrap code from answer -- DONE
        3. Display answer and vote count -- DONE

4. Argumrents to get detailed or summarized results [flag] -- DONE
5. Check for exceptions and internet connection -- DONE
6. Create snippet result for a quick view for user -- DONE
7. ADD method to print snippet in a box. -- DONE
8. ADD functionality: 
    > to let user see page 1 by 1, by clicking Enter for next or Press 'x' + 'ENTER' to break further print results  -- DONE  
9. ADD 'result' [Optional Parameter] - [INT] to get the complete output as a STRING, instead of printing result -- DONE
    > 0 [DEFAULT] - To print the result -- DONE  
    > 1 - To Get search_result {Dictionary} as return for search result -- DONE  
    > 2 - To Get search_result + raw data result as key:value pair -- DONE
10. ADD 'verified' [Optional Parameter] as an optional parameter to only display the verified answer from the page
11. Store complete print in a List[..,answer_pages] named 'search_result' and then later join as String to print/return just as implemented in 'text_in_box()' method.
    Benifits: -- DONE
        > Ease in implementing Break/Next option to move on page over a loop -- DONE  
        > Ease to implement the 'result' [Optional Parameter] -- DONE
        > STORE answer_pages as dictionary as {'page-1':'<page 1 data>', 'page-2':'<page 2 data>',...,'page-n':'<page n data>'} -- DONE
12. Implement a 'print_stackOverflow_result' method to display result with implementing STEP (8) within it -- DONE
13. STRORE page_result[1] for each page excluding answer_body as we will get that from search_result -- DONE
14. Format DETAILED Page better -- DONE
15. Testing + Documentation
"""
# --------------------- IMPORTS -----------------------
from unittest import result
from datetime import datetime
import requests
import re
from bs4 import BeautifulSoup as bs

# -------------------- Decorator Function For highlighting SNIPPETS in answer --------------------------


def text_in_box(value, char='.'):
    """
    >General Method<
    Prints the given string in a Box design format

    Paameters:
    value: String (Single line / multi line)
    char: Char for box pattern [Default is '.']
    """
    length = max([len(line) for line in value.split("\n")])

    textBox = ["\t"+char*(length+8)+"\n"]

    for textLine in value.split("\n"):
        if len(textLine) == 0:
            continue
        textLine = f"\t{char}   "+textLine + \
            (" "*(length-len(textLine)+3)+f"{char}\n")
        textBox.append(textLine)

    textBox.append("\t"+char*(length+8)+"\n")

    return ''.join(textBox)


# -------------------- Decorator Function For highlighting answer body --------------------------
def highlight(char='-', n=0):
    if n == 1:
        pattern = "\n" + char*100
        return pattern
    elif n == 2:
        pattern = char*100 + "\n"
        return pattern
    else:
        pattern = char * 100
        return pattern


# ---------------------- Method to print the stack overflow results ------------------------
def print_stackOverflow_result(search_result):
    """
    Method to print the search results.

    Parameters:    
    @search_result - {DICTIONARY}     
    """
    try:
        print(search_result['result_title'], end='')

        # Printing for results
        for i in range(1, search_result['total_stackoverflow_pages_results']+1):
            user_input = ''  # To catch user action to continue or break the results
            print(search_result['page-'+str(i)], end='')

            user_input = input(
                "\nPress 'ENTER' for next Page or Press 'x' + 'ENTER' to end result\t")
            while(user_input not in ['', 'x']):
                user_input = input(
                    f"\nINVALID INPUT! -> {user_input}\nPress 'ENTER' for next Page or Press 'x' + 'ENTER' to end result\t")

            if user_input == 'x' or (i == search_result['total_stackoverflow_pages_results']):
                print("\nThat's all folks! :)")
                break
    except Exception as e:
        raise SystemExit(
            "Exception caught during print_stackOverflow_result() method.\nStack Trace:\n", e)


# -------------------- Method to get all stack overflow URLs from google for the searched query --------------------------


def get_google_searchResult_Links(query, domain_name=0):
    """
    Method to get urls results from google search engine

    Parameters:
    query [STRING]: stack overflow query to search.
    domain [STRING]: To filter the result based on a particular website.
                    [Default]: 0 --> Get All results irrespective of domain name

    Return:
    result_links [List]:
        [...,] - Result Urls scraped for the search page
        [-1] - If no result found for filtered website with requested query
        [0] - If no result found on the Internet
    """

    result_links = []
    #print("Reaching Base point 1 for get_google_searchResult_Links()")

    # Add Try and Except to check for internet and other exceptions
    try:
        page = requests.get("https://www.google.dz/search?q=" +
                            query)
    except Exception as e:
        if e.__class__.__name__ == "ConnectionError":
            raise SystemExit(
                "ConnectionError! Please check your system is connected to a network.")
        else:
            raise SystemExit(e)

    soup = bs(page.content, features="html.parser")

    if domain_name == 0:
        #print("Reaching Base point 1 for domain_name check for default")
        # Return all search result, irrespective of domain name
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
        # print(result[0])
        if result[0].find(domain_name) != -1:
            # Check if result contains url with filtered website
            result_links.append(result[0].split('&')[0])

    if len(result_links) == 0:
        # No result found for filtered website with requested query
        return [-1]
    else:
        return result_links


# ---------------------- Method to scrap the stack overflow page ------------------------
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
    try:
        # Title of the page
        stackoverflow_page_title = ' '.join(
            page.find("title").get_text(strip=True).split('-')[0:-1])

        # Total number of answers on the page
        answer_count = page.find(
            "h2", {'data-answercount': True}).get_text(strip=True).split()[0]

        # No answer for current page
        if answer_count == '0':
            return [-1, stackoverflow_page_title]

        # First Vote is for the Question, rest are for answers
        # So, all_votes - 1 = answer_count
        #all_votes = [vote.get_text(strip=True) for vote in page.find_all("div", class_='js-vote-count flex--item d-flex fd-column ai-center fc-black-500 fs-title')]
        all_votes = [vote.get_text(strip=True)
                     for vote in page.select("div[class*='js-vote-count']")]

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

    except Exception as e:
        return [-1, stackoverflow_page_title + "\nUnable to extract result from the page. Kindly continue to next page\n"]


# ---------------------- Method to return result for the searched query on stack overflow ------------------------
def get_stackoverflow_result(query, limit=2, **parameters):
    """
    Method to show stack overflow results.

    Parameters:
    query [STRING]: stack overflow query to search
    limit [INT]: Number of answers to display per page (DEFAULT - 2)

    Optional keyword arguments::
    @ans_format [INT]: 
    > 0 - Display only code snippets from answer (DEFAULT)
    > 1 - Display detailed answer

    @result [INT]:
    > 0 [DEFAULT] - To print the result
    > 1 - To get search_result {DICTIONARY} as return for search result
    > 2 - Get result as key:value pair data with raw inputs and only formated answer body

    Verified [BOOL] | (Under development) : 
    <TRUE> - To display only the Verified Accepted Correct Answer on the Stack overflow page.
    <FALSE> - To display all the result within the limit. [DEFAULT]

    Return:
    search_result {DICTIONARY}:    
    > 'result_title': [STRING] <Title of the Result>
    > 'page-n': [STRING] <page_data>, Where 'n' is page number & page_data is formated page result
    > 'pages': [INT] <Number of pages in result>
    """
    # To get all the info in the dictionary as <page-n> : <page_data>, Where 'n' is page number & page_data is formated page result
    search_result = {'result_title': '',
                     'total_stackoverflow_pages_results': 0}

    default_parameters = {'ans_format': 0, 'result': 0}
    # parameter check & update
    for parameter_key in parameters.keys():
        if parameter_key not in ['ans_format', 'result']:
            raise TypeError(
                "'{}' is an invalid keyword argument for get_myString() \nFor more details for valid parameters try:\nhelp(get_myString) OR\nget_myString.__doc__", parameter_key)
        else:
            default_parameters[parameter_key] = parameters[parameter_key]

    if default_parameters["result"] == 0:
        print("Process Initiated: ", datetime.today().strftime('%Y-%m-%d %H:%M:%S'))

    # Gets all url of search result from google have the mentioned domain_name
    query_links = get_google_searchResult_Links(
        query+" stack overflow", domain_name='stackoverflow.com')

    # Check if stackoverflow url result exists
    if query_links[0] == -1 or query_links[0] == 0:
        # No results found with query
        if default_parameters["result"] == 0:
            print(
                "No Stack Overflow result for Query. :(\nPlease Try again by modifying the query!")
        else:
            return "No Stack Overflow result for Query. :(\nPlease Try again by modifying the query!"

    else:
        page_count = 0
        # Result URLs found with domian name search
        total_stackoverflow_pages_results = len(query_links)

        search_result['result_title'] = (highlight(
            char='*', n=1) + f"\nStack Overflow Results:\tTotal Pages - ({total_stackoverflow_pages_results})\n")

        search_result["total_stackoverflow_pages_results"] = total_stackoverflow_pages_results

        # LOOP to traverse over stack overflow pages
        for url in query_links:
            # print(url)
            page_count += 1
            resp = requests.get(url)
            soup = bs(resp.text, features="html.parser")

            # Getting data from the page
            page_result = scrap_stackoverflow_page(
                soup, default_parameters["ans_format"])

            # -----------------------------------------------------------------
            # --------------------  NO ANSWER PRESENT -------------------------
            # -----------------------------------------------------------------
            if page_result[0] == -1:
                # No Answer for the query in current stack overflow page
                search_result["page-"+str(page_count)] = highlight(char='*') + f"\nPage {page_count} Title - " + page_result[1] + \
                    "\n\t----> NO ANSWERS PRESENT for Current Page <-----\n" + \
                    highlight(n=2)

            # -----------------------------------------------------------------
            # -----------------  DETAILED ANSWER FORMAT -----------------------
            # -----------------------------------------------------------------
            elif page_result[0] == 1:
                # DETAILED[1] Answer Present for the query in current stack overflow page

                # String to store complete result of current page and later to get appended in answer_page
                current_detailed_page = ''
                answer_collections = []

                page_details = page_result[1]
                #{'stackoverflow_page_title': stackoverflow_page_title, 'answer_count': answer_count, 'all_votes': all_votes, 'answer_body': answer_body}

                current_detailed_page += highlight(char='*')
                current_detailed_page += f"\nPage ({page_count}) Title - " + \
                    page_details["stackoverflow_page_title"]
                current_detailed_page += f"\nPage Vote: {page_details['all_votes'][0]} | \tTotal Answers Present: {page_details['answer_count']} | \tAnswer Limit: {limit} | \tFormat: DETAILED\n"

                ans_count = 0
                for body in page_details['answer_body'][0:limit]:
                    ans_count += 1
                    current_detailed_page += highlight()
                    current_detailed_page += f"\n-->  ANSWER No. ({ans_count}) ANSWER VOTES: {page_details['all_votes'][ans_count]} <--\n"
                    current_detailed_page += body.get_text() + highlight(n=2)
                    answer_collections.append(body.get_text())

                # To update search_result if Optional parameter result==2 i.e. to ge raw search data in dictionary
                if default_parameters["result"] == 2:
                    raw_search_result = page_details
                    raw_search_result['answer_body'] = answer_collections
                    search_result["page-" +
                                  str(page_count)] = raw_search_result

                else:
                    search_result["page-" +
                                  str(page_count)] = current_detailed_page
                    search_result["page-" +
                                  str(page_count)+"-ans"] = answer_collections

            # -----------------------------------------------------------------
            # -----------------  SNIPPET ANSWER FORMAT -----------------------
            # -----------------------------------------------------------------
            elif page_result[0] == 0:
                # Summarised CODE SNIPPETS[0] Answer Present for the query in current stack overflow page
                # String to store complete result of current page and later to get appended in answer_page
                current_snippet_page = ''
                answer_collections = []

                page_details = page_result[1]
                #{'stackoverflow_page_title': stackoverflow_page_title, 'answer_count': answer_count, 'all_votes': all_votes, 'answer_body': answer_body}

                current_snippet_page += highlight(char="*")
                current_snippet_page += f"\nPage ({page_count}) TITLE - " + \
                    page_details["stackoverflow_page_title"]

                current_snippet_page += f"\nPage Vote: {page_details['all_votes'][0]} | \tTotal Answers Present: {page_details['answer_count']} | \tAnswer Limit: {limit} | \tFormat: CODE-SNIPPET\n"

                ans_count = 0  # To count the answer number and get votes based on index
                limit_breaker = 0  # To check the number of answer printed and break when reached limit

                # LOOPING over all the answer body present in the page
                for snippet_collection in page_details['answer_body']:
                    # snippet_collection is list of all snippets present in that answer
                    ans_count += 1

                    # Skip if no snippet in the answer
                    if len(snippet_collection) == 0:
                        continue

                    # Incrementing limit breaker only for printed answer
                    limit_breaker += 1
                    current_snippet_page += highlight(n=2)
                    current_snippet_page += f"--> ANSWER No. ({limit_breaker}) || VOTES: {page_details['all_votes'][ans_count]} <--\n"

                    # Traversing all snippets in snippet_collection of answer
                    for snippet in snippet_collection:
                        text_in_box_result = text_in_box(snippet)
                        current_snippet_page += text_in_box_result
                        answer_collections.append(text_in_box_result)

                    current_snippet_page += highlight(n=2)

                    # Break if limit for answer to be displayed is reached
                    if limit_breaker == limit:
                        break

                # To update search_result if Optional parameter result==2 i.e. to ge raw search data in dictionary
                if default_parameters["result"] == 2:
                    raw_search_result = page_details
                    raw_search_result['answer_body'] = answer_collections
                    search_result["page-" +
                                  str(page_count)] = raw_search_result
                else:
                    search_result["page-" +
                                  str(page_count)] = current_snippet_page
                    search_result["page-" +
                                  str(page_count)+"-ans"] = answer_collections

        # ------------- OUT of LOOP to traverse over stack overflow pages ---------------
        if default_parameters["result"] == 0:
            print_stackOverflow_result(search_result)
        elif default_parameters["result"] == 1:
            return search_result
        else:
            # Here, search_result = raw_search_result
            return search_result


# ---------------------- Main Method --------------------------
if __name__ == '__main__':
    print("Please follow the below documentation for usage:")
    print("\n", help(get_stackoverflow_result))

    #query = "functions in python"
    #query_to_check_noSnippetAnswers = "git-for-beginners-the-definitive-practical-guide"
    #query_with_noAnswers = "Hybris navigation component anatomy"
    # query="sa5d64sa6"
    # print(*get_google_searchResult_Links(query,website),sep="\n")

    #get_data = get_stackoverflow_result(query)
    #data = get_stackoverflow_result(query, ans_format=0, result=0)

    #get_stackoverflow_result(query_with_noAnswers, ans_format=0)
    # get_stackoverflow_result(query_to_check_noSnippetAnswers, ans_format=0)
