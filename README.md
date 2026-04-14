
# Table of Contents

1.  [Installing](#orgd697461)
2.  [Check Test](#orgdfa0beb)
3.  [Pypi](#org43a0292)

Learning about Natural Language Tool Kit (NLTK) from tests

A first version can be found in: <https://github.com/Lingwars/GAPLEN>

Thanks to GAPLEN by the shared time.

Learning NLTK from Tests by David Arroyo Menéndez


<a id="orgd697461"></a>

# Installing

    $ pip3 install damenltk
    $ python3 damenltk/installing-nltk-modules.py


<a id="orgdfa0beb"></a>

# Check Test

-   Execute all tests:

    $ ./runtests.sh

-   Execute one file:

    $ pytest test/test_bernoulli.py 


<a id="org43a0292"></a>

# Pypi

-   To install from local:

    $ pip install -e .

-   To install create tar.gz in dist directory:

    $ python3 -m build

-   To upload to pypi:

    $ twine upload dist/damenltk-0.1.tar.gz

-   You can install from Internet in a python virtual environment to check:

    $ python3 -m venv /tmp/dn
    $ cd /tmp/dn
    $ source bin/activate
    $ pip3 install damenltk

