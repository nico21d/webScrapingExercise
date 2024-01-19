Simple web scraper that gets the first 30 entries from https://news.ycombinator.com/.

The current code gets the 30 entries and then prints them on console. It will also print
the elements filtered by titles with more than 5 words ordered by number of coments
and by titles with less or equal than 5 words ordered by points.

Each entry is stored in an object Entry that will contain its title, points and number of comments.
The code could be changed to store the entries to a file.

To run the code, you will need to have a recent version of Python and have installed 
the package bs4. Once that is done, running py ./scrapper.py will run the code.
