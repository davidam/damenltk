
# Table of Contents

1.  [Installing from git](#orgd603379)
2.  [Check Test](#orgf4e38db)
3.  [Installing from pypi](#org4ae5bdb)
4.  [Updating the source](#org3ef8d49)
    1.  [To create new tar.gz in dist directory:](#orgc40c83f)
    2.  [To upload to pypi:](#org5b8963e)

Learning about Natural Language Tool Kit (NLTK) from tests

A first version can be found in: <https://github.com/Lingwars/GAPLEN> 

Thanks to GAPLEN by the shared time.

Learning NLTK book (<https://www.nltk.org/book>) from Tests by David Arroyo Menéndez


<a id="orgd603379"></a>

# Installing from git

    $ git clone https://github.com/davidam/damenltk
    $ pip3 install nltk scikit-learn
    $ cd damenltk
    $ python3 damenltk/installing-nltk-modules.py


<a id="orgf4e38db"></a>

# Check Test

-   Execute all tests:

    $ ./runtests.sh

-   Execute one file:

    $ pytest test/test_bernoulli.py 

-   Execute one test:

    $ pytest test/test_wordnet.py::TddInPythonExample::test_lemmatizer


<a id="org4ae5bdb"></a>

# Installing from pypi

You can install from Internet in a python virtual environment to check: 

    $ python3 -m venv ~/venv_damenltk
    $ cd ~/venv_damenltk
    $ source bin/activate
    $ pip3 install damenltk
    $ cd ~/venv_damenltk/lib/python3.14/site-packages/damenltk
    $ pytest test/test_bernoulli.py 


<a id="org3ef8d49"></a>

# Updating the source


<a id="orgc40c83f"></a>

## To create new tar.gz in dist directory:

    $ python3 -m build


<a id="org5b8963e"></a>

## To upload to pypi:

    $ twine upload dist/damenltk-0.1.tar.gz

