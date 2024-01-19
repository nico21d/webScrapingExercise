from bs4 import BeautifulSoup
import requests
import re

class Entry:
    def __init__(self, text, points, comments):
        self.text = text
        self.points = points
        self.comments = comments

    def __str__(self):
        return self.text + "   Points: " + str(self.points) + "   Comments: " + str(self.comments)


scraped_page = requests.get("https://news.ycombinator.com/")
parsed_page = BeautifulSoup(scraped_page.text, "html.parser")

table = parsed_page.find('table')
content_table = table.find_all('tr')[3]

content_rows = content_table.find_all('tr', limit = 90)
del content_rows[2:90:3]


element_list = []

for i in range(0, len(content_rows), 2):
    title = content_rows[i].find('span', attrs={"class":"titleline"}).a.text

    score_tag = content_rows[i+1].find('span', attrs={"class":"score"})
    if score_tag is not None:
        score = int(re.findall(r'\d+', score_tag.text)[0])
    else:
        score = 0

    comment_tag = content_rows[i+1].find('a', string=lambda s: s and "comments" in s)
    if comment_tag is not None:
        comments = int(re.findall(r'\d', comment_tag.text)[0])
    else:
        comments = 0
    
    element_list.append(Entry(title, score, comments))


print("\nFirst 3 entries, their points and their comments: \n")
for elem in element_list:
    print(elem)

print("\nEntries with more than five words in the title ordered by number of comments in descending order: \n")
gt_five_words = [elem for elem in element_list if len(elem.text.split())>5]

sorted_by_comments_descending = sorted(gt_five_words, key=lambda x:x.comments, reverse=True)

for elem in sorted_by_comments_descending:
    print(elem)

print("\nEntries with less or equal than five words in the title ordered by points in descending order: \n")
le_five_words = [elem for elem in element_list if len(elem.text.split())<=5]

sorted_by_scores_descending = sorted(le_five_words, key=lambda x:x.points, reverse=True)

for elem in sorted_by_scores_descending:
    print(elem)