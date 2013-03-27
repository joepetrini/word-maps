from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises
from wordmaps.app.words import getWords


def simple_word_group():
    """ Simple grouping test, no tricks """
    w = getWords("test test2 test")
    v = {'test': 2, 'test2': 1}
    assert_equal(w, v)

