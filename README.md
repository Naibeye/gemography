<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
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
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">backend-coding-challenge</h3>

  <p align="center">
    API REST microservice that list the languages used by the 100 trending public repos on GitHub.
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#project-description">Project description</a>
     </li>
    <li><a href="#getting-started">Getting Started</a></li>
     <li><a href="#built-with">Built With</a></li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- PROJECT DESCRIPTION -->
## Project description
Using the endpoint 
``` sh
 https://api.github.com/search/repositories?q=created:>{date}&sort=stars&order=desc
```
Fetching trending repositories simply translates to fetching the most starred repos created in the last 30 days ( from now ).

Develop a REST microservice that list the languages used by the 100 trending public repos on GitHub. For every language, you need to calculate the attributes below 👇:the number of repos using this language and the list of repos using the language



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.
<!-- BUILT WITH-->
## Built With
* [flask](https://flask.palletsprojects.com/en/2.0.x/)
* [requests](https://pypi.org/project/requests/)
<!-- PREREQUISITES -->
## Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* certifi==2021.5.30
*  chardet==4.0.0
*  click==8.0.1
*  colorama==0.4.4
*  Flask==2.0.1
* idna==2.10
* itsdangerous==2.0.1
* Jinja2==3.0.1
* MarkupSafe==2.0.1
* python-dotenv==0.17.1
* requests==2.25.1
* urllib3==1.26.5
* Werkzeug==2.0.1
  ```sh
  $pip install -r requirements.txt
  ```

## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Naibeye/gemography.git
   ```
2. Run it
   ```sh
   $ flask run
   ```
3. use url 
 ```sh
   http://localhost:5000/getlangue
   ```
  
<!-- CONTACT -->
## Contact

DJIMNAIBEYE- [@djimnaibeye-sidoine-6a332a36](https://www.linkedin.com/in/djimnaibeye-sidoine-6a332a36/) - dthekplus@gmail.com

Project Link: [https://github.com/Naibeye/gemography](https://github.com/Naibeye/gemography)




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/Naibeye/gemography/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/Naibeye/gemography?style=plastic
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/djimnaibeye-sidoine-6a332a36/
[product-screenshot]: images/screenshot.png
