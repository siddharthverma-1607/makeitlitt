<a name="readme-top"></a>

<!--
*** Thanks for checking out the README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/siddharthverma-1607/makeitlitt">
    <img src="images/littUp.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">MAKEITLITT</h3>

  <p align="center">
    An awesome opensource project for adding custom dynamic methods and functionality for Built-in Data Types!<br />Creating general modules for repetative tasks.  (Which have a potential of being an project in itself 😉)
    <br /><br />    
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>    
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

There are many great opensource projects available on GitHub; however, I didn't find one that really suited my needs so I created this enhanced one. I want to create a python package which can add dynamic functionaities to built in types. Also to club general repetative task as a form of automation or method.

Here's why:

- We Pythoner's daily write awesome code and sometime surprice ourself with a method or script created by ourself realizing this can be used again or is just to awesome!
- These can be your implmentation for slicing, scraping, printing, etc.. But all the ideas can be categorized into some umbrella like slicing will be for list/strings; scrapping; Extracting keywords from string...
- This repository is that umbrella

Of course, no one package will serve all projects since your needs may be different. So I'll be adding more modules in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people in advance planning to contribute or to expand this repo!

Use the `Documentation` to get started.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

- [![python][python-shield]][python-url]
- [![selenium][selenium-shield]][selenium-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

Most of the modeules are standalone but for few make require some additional packages which will taken care up by PIP.

### Prerequisites

You need python 3 and any IDE installed. To install python:

```sh
Go to https://www.python.org/downloads/ and download any 3.x version for python
```

### Installation

_Install the package using PYPI (pip)_

```sh
pip install makeitlitt
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

1. For Stackoverflow module:
   To get the stack overflow results for the query we search daily for confirmation 😁
   module name: stackoverflow
   Import:

```sh
from makeitlitt import stackoverflow
```

Method name: get_stackoverflow_result(query, limit=2, \*\*parameters)
Method Documentation:

> Method to show stack overflow results.

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

Examples:

- To print results of code snippets from stack overflow for mention query

```sh
from makeitlitt import stackoverflow as sf
sf.get_stackoverflow_result("list slicing in python")
```

- To get all the raw scrapped data as a dictionary

```sh
from makeitlitt import stackoverflow as sf
search_results_snippets = sf.get_stackoverflow_result("list slicing in python",result=2) #Gets only code snippets from the answer
search_results_detailed = sf.get_stackoverflow_result("list slicing in python",ans_format=1,result=2) #Gets detailed long answer
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

1. For fetching all the search result URLs on Google search engine for a search query:
   To get the URL search results for the query to perform scrapping, SEO analysis or any other user case.
   module name: stackoverflow
   Import:

```sh
from makeitlitt import stackoverflow
```

Method name: get_google_searchResult_Links(query, domain_name=0)
Method Documentation:

> Method to get URL results from google search engine

    Parameters:
    query [STRING]: Query to search.
    domain [STRING]: To filter the result based on a particular website.
                    [Default]: 0 --> Get All results irrespective of domain name

    Return:
    result_links [List]:
        [...,] - Result Urls scraped for the search page
        [-1] - If no result found for filtered website with requested query
        [0] - If no result found on the Internet

Examples:

- To get all the URLs of searched query as result

```sh
from makeitlitt import stackoverflow as sf
sf.get_google_searchResult_Links("How to create a pancake?")
```

- To get all the URLs of searched query from a particular domain

```sh
from makeitlitt import stackoverflow as sf
sf.get_google_searchResult_Links("How to create a dictionary in python?", domain_name="stackoverflow.com")
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->

## Roadmap

- [x] Scrap data from each URL
- [x] Get question and question vote count
- [x] Check total Answers present in page
- [x] Argumrents to get detailed or summarized results [flag]
- [x] Check for exceptions and internet connection
- [x] Create snippet result for a quick view for user
- [x] ADD method to print snippet in a box.
- [x] ADD 'result' [Optional Parameter] - [INT] to get the complete output as a STRING, instead of printing result
- [x] Store complete print in a List[..,answer_pages] named 'search_result' and then later join as String to print/return just as implemented in 'text_in_box()' method.
- [ ] ADD 'verified' [Optional Parameter] as an optional parameter to only display the verified answer from the page
- [ ] Unittesting

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Linkdln - [@Siddharth Verma](https://www.linkedin.com/in/siddharth-verma-99b54a117/) - artistwhocode7@protonmail.com

Discord: [Siddharth#3469](https://discordapp.com/users/Siddharth#3469)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[forks-shield]: https://img.shields.io/github/forks/siddharthverma-1607/makeitlitt.svg?style=for-the-badge
[forks-url]: https://github.com/siddharthverma-1607/makeitlitt/network/members
[stars-shield]: https://img.shields.io/github/stars/siddharthverma-1607/makeitlitt.svg?style=for-the-badge
[stars-url]: https://github.com/siddharthverma-1607/makeitlitt/stargazers
[issues-shield]: https://img.shields.io/github/issues/siddharthverma-1607/makeitlitt.svg?style=for-the-badge
[issues-url]: https://github.com/siddharthverma-1607/makeitlitt/issues
[license-shield]: https://img.shields.io/github/license/siddharthverma-1607/makeitlitt.svg?style=for-the-badge
[license-url]: https://github.com/siddharthverma-1607/makeitlitt/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/siddharth-verma-99b54a117/
[python-shield]: https://img.shields.io/badge/python%20v3.7-000000?style=for-the-badge&logo=python&logoColor=green
[python-url]: https://www.python.org/
[selenium-shield]: https://img.shields.io/badge/Selenium-DD0031?style=for-the-badge&logo=selenium&logoColor=white
[selenium-url]: https://www.selenium.dev/
