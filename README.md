# TestSiteBuilder

Sometimes (like when you're doing lots of memory profiling), it's nice to have a site hosted locally so that you can avoid all of the waiting around the Vincent does to be polite.

## Setup
To get this up and running, install jekyll and bundler:
```
    sudo apt-get install ruby2.0 ruby2.0-dev
    sudo gem2.0 install jekyll bundler
```

Then go to the site directory and let bundle install the dependencies listed in the Gemfile:
```
    cd TestSiteBuilder/site
    bundle install
```

### Vincent Setup
First, you'll need to go to `/etc/hosts` and add a line for your test site, since Vincent won't accept `localhost` or an IP address for a project URL. Something like:
```
127.0.0.1   test.dev
```
Remeber that jekyll will serve the page on port 4000 unless told otherwise, so the URL that you would give your Vincent project would be `http://test.dev:4000`.

## Running
Now you're ready to build some pages (provide the number of pages as an argument to `build.py`) and serve the website:
```
    python build.py 100
    cd site
    jekyll serve
```

You'll need to set the `VINCENT_DEBUG_LOCALHOST_SITE` environment variable in order for Vincent to know to shortcircuit proxies, etc. You can do this one of two ways. Either set the variable to true for your entire session with `export VINCENT_TEST_LOCALHOST_SITE=1`, or simply prepend the commands you want to run:
```VINCENT_DEBUG_LOCALHOST_SITE=1 mprof run_local.py```

In PyCharm, you can edit your local debug configuration to set the environment variable for the debug session.

