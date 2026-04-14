
# Table of Contents

1.  [Installing](#org400d147)
2.  [Check Test](#org4e85ed4)
3.  [Pypi](#org2fc3008)

Learning about Natural Language Tool Kit (NLTK) from tests

A first version can be found in: <https://github.com/Lingwars/GAPLEN>

Thanks to GAPLEN by the shared time.

Learning NLTK from Tests by David Arroyo Menéndez


<a id="org400d147"></a>

# Installing

    $ pip3 intall damenltk
    $ python3 damenltk/installing-nltk-modules.py


<a id="org4e85ed4"></a>

# Check Test

-   Execute all tests:

    $ nosetests3 tests

-   Execute one file:

    $ nosetests3 tests/test_basics.py

-   Execute one test:

    nosetests3 test/test_syn.py:TddInPythonExample.test_syn_returns_correct_result


<a id="org2fc3008"></a>

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

