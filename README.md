# TestSiteBuilder
To get this up and running, install jekyll and bundler:
    sudo apt-get install ruby2.0 ruby2.0-dev
    sudo gem2.0 install jekyll bundler

Then go to the site directory and install the dependencies:
    cd TestSiteBuilder/site
    bundle install

Now you're ready to build some pages (adjust the number of pages near the top
of build.py) and serve the website:
    python build.py
    cd site
    jekyll serve

Note that jekyll is set to run in the background, so you'll have to kill it when
you're done:
    pkill -f jekyll
