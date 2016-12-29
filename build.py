import os
import shutil
import datetime
from random import randint

CONTENT_DIR = 'site/_posts/'
CONTENT_BODY_TEMPLATE = '_lorem_ipsum.in'
NUM_POSTS = 50

def create_clean_content_dir():
    d = os.path.dirname(CONTENT_DIR)
    if os.path.exists(d):
        shutil.rmtree(CONTENT_DIR)

    os.makedirs(d)


def create_post_file(post_title, body_text, date, post_num):
    with open(os.path.join(CONTENT_DIR, post_title), 'w') as outfile:
        outfile.write('---')
        outfile.write('layout: post')
        outfile.write('title:  "Lorem Ipsum {}"'.format(index))
        outfile.write('date:   {}'.format('%Y-%m-%d %H:%M:%S')
        outfile.write('---')
        outfile.write()
        outfile.write(body_text)


def main():
    create_clean_content_dir()

    body_text = 'BODY TEXT!'
    with open(CONTENT_BODY_TEMPLATE, 'r') as infile:
        body_text = infile.read()

    for i in range(NUM_POSTS):
	post_num = NUM_POSTS-i
        date = datetime.datetime.utcnow() - datetime.timedelta(days=i)
        post_title = '{}-page{}.html'.format(date.strftime('%Y-%m-%d'), post_num)

        create_post_file(post_title, body_text, date, post_num)

if __name__ == '__main__':
    main()
