from bs4 import BeautifulSoup

with open("websitee.html") as file:
    data = file.read()

soup = BeautifulSoup(data, "html.parser")
# print(soup.body.string)

anchor = soup.find_all(name="a")
# print(anchor)

# for tag in anchor:
    # print(tag.get("h1", id="name"))

# heading =
url = soup.select("body a")
print(url)