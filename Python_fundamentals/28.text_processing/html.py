# You will receive lines of input:
# On the first line, you will receive a title of an article
# On the second line, you will receive the content of that article
# On the following lines, until you receive "end of comments" you will get the comments about the article
# Print the whole information in html format:
# The title should be in "h1" tag (<h1></h1>)
# The content in article tag (<article></article>)
# Each comment should be in div tag (<div></div>)


def print_html_tag(text, tag):
    print(f"<{tag}>")
    print(text)
    print(f"</{tag}>")


title = input()
content = input()

print_html_tag(title, "h1")
print_html_tag(content, "article")

while True:
    comment = input()

    if comment == "end of comments":
        break

    print_html_tag(comment, "div")