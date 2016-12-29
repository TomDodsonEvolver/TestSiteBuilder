import os
import shutil
import datetime
from random import randint

CONTENT_DIR = 'site/_posts/'
CONTENT_BODY_TEMPLATE = '_lorem_ipsum.html'
NUM_POSTS = 50

def create_clean_content_dir():
    d = os.path.dirname(CONTENT_DIR)
    if os.path.exists(d):
        shutil.rmtree(CONTENT_DIR)

    os.makedirs(d)


def create_post_file(post_title, body_text):
    with open(os.path.join(CONTENT_DIR, post_title), 'w') as outfile:
        outfile.write('{% include header.html %}')
        outfile.write('<body>')
        outfile.write('<h1>{}</h1>'.format(post_title))
        outfile.write(body_text)
        outfile.write('</body>')
        outfile.write('{% include footer.html %}')


def main():
    create_clean_content_dir()

    body_text = '<p>BODY TEXT!</p>'
    with open(CONTENT_BODY_TEMPLATE, 'r') as infile:
        body_text = infile.read()

    for i in range(NUM_POSTS):
        date = datetime.datetime.utcnow() - datetime.timedelta(days=i)
        post_title = '{}-page{}.html'.format(date.strftime('%Y-%m-%d'), NUM_POSTS-i)

        create_post_file(post_title, body_text)

if __name__ == '__main__':
    main()
