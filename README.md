
# Table of Contents

1.  [Installing from git](#orgae0aae0)
2.  [Check Test](#orgdb5c7ae)
3.  [Pypi](#orgf7a89f3)

Learning about Natural Language Tool Kit (NLTK) from tests

A first version can be found in: <https://github.com/Lingwars/GAPLEN>

Thanks to GAPLEN by the shared time.

Learning NLTK from Tests by David Arroyo Menéndez


<a id="orgae0aae0"></a>

# Installing from git

    $ git clone https://github.com/davidam/damenltk
    $ pip3 install nltk scikit-learn
    $ cd damenltk
    $ python3 damenltk/installing-nltk-modules.py


<a id="orgdb5c7ae"></a>

# Check Test

-   Execute all tests:

    $ ./runtests.sh

-   Execute one file:

    $ pytest test/test_bernoulli.py 


<a id="orgf7a89f3"></a>

# Pypi

-   You can install from Internet in a python virtual environment to check:

    $ python3 -m venv /tmp/dn
    $ cd /tmp/dn
    $ source bin/activate
    $ pip3 install damenltk
    $ cd /tmp/dn/lib/python3.14/site-packages/damenltk
    $ pytest test/test_bernoulli.py 

-   To create new tar.gz in dist directory:

    $ python3 -m build

-   To upload to pypi:

    $ twine upload dist/damenltk-0.1.tar.gz

