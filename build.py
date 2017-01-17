import os
import shutil
import datetime

CONTENT_DIR = 'site/_posts/'
CONTENT_BODY_TEMPLATE = '_lorem_ipsum.in'

def create_clean_content_dir():
    d = os.path.dirname(CONTENT_DIR)
    if os.path.exists(d):
        shutil.rmtree(CONTENT_DIR)

    os.makedirs(d)


def create_post_file(file_name, body_text, date, post_num):
    with open(os.path.join(CONTENT_DIR, file_name), 'w') as outfile:
        outfile.write('---\n')
        outfile.write('layout: post\n')
        outfile.write('title:  "Lorem Ipsum Number {}"\n'.format(post_num))
        outfile.write('date:   {}\n'.format(date.strftime('%Y-%m-%d %H:%M:%S')))
        outfile.write('---\n\n')
        outfile.write(body_text)


def make_content(num_posts=10):
    create_clean_content_dir()

    body_text = 'BODY TEXT!'
    with open(CONTENT_BODY_TEMPLATE, 'r') as infile:
        body_text = infile.read()

    for i in range(num_posts):
	post_num = num_posts - i
        date = datetime.datetime.utcnow() - datetime.timedelta(days=i)
        file_name = '{}-page{}.md'.format(date.strftime('%Y-%m-%d'), post_num)

        create_post_file(file_name, body_text, date, post_num)


if __name__ == '__main__':
    import argparse
    
    parser = argparse.ArgumentParser(description="Create content for a jekyll-served webpage. The total number of pages will be num_pages+2 including the static index and PDF test page.")
    parser.add_argument('num_pages', metavar='num_pages', type=int,
                        help='number of post pages to produce')
    args = parser.parse_args()   
 
    make_content(args.num_pages)

