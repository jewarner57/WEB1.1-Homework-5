import pytest

from .string_functions import *


def test_greeting_jeremy():
    """Test for greet_by_name"""
    # Step 1: Choose a scenario - here I'm choosing name='Jeremy'

    # Step 2: Decide what the expected outcome is for the scenario
    expected = 'Hello, Jeremy!'

    # Step 3: Call the function being tested to get its actual output
    actual = greet_by_name('Jeremy')

    # Step 4: Compare expected & actual outcomes. If they match, the test passes
    assert actual == expected


def test_greeting_dani():
    """Test for greet_by_name"""
    expected = 'Hello, Dani!'
    actual = greet_by_name('Dani')
    assert actual == expected


def test_reverse_long():
    """Test reversing a long string."""
    expected = 'sdflk;sfljdkksfdajlk;skdflkjfsdjllfjkdsljkfsdkjsdfajksfd'
    actual = reverse(
        "dfskjafdsjkdsfkjlsdkjflljdsfjklfdks;kljadfskkdjlfs;klfds")

    assert actual == expected


def test_reverse_empty():
    expected = ""
    actual = reverse("")
    assert actual == expected


def test_reverse_short():
    """Test reversing a short string."""
    expected = '123'
    actual = reverse("321")
    assert actual == expected


def test_reverse_words_long():
    """Test reversing words in a long string."""
    expected = "waL ylnommoc srefer ot a metsys fo selur detaerc dna decrofne hguorht laicos ro latnemnrevog"
    actual = reverse_words(
        "Law commonly refers to a system of rules created and enforced through social or governmental")
    assert actual == expected


def test_reverse_words_short():
    """Test reversing words in a short string."""
    expected = 'ym eman si eoj'
    actual = reverse_words("my name is joe")
    assert actual == expected


def test_reverse_words_empty():
    expected = ""
    actual = reverse_words("")
    assert actual == expected


def test_sarcastic_long():
    """Test sarcastic-ifying a long string."""
    expected = 'LaW cOmMoNlY rEfErS tO a SyStEm Of RuLeS cReAtEd AnD eNfOrCeD tHrOuGh SoCiAl Or GoVeRnMeNtAl InStItUtIoNs To ReGuLaTe BeHaViOr, WiTh ItS pReCiSe DeFiNiTiOn A mAtTeR oF lOnGsTaNdInG dEbAtE. iT hAs BeEn VaRiOuSlY dEsCrIbEd As A sCiEnCe AnD tHe ArT oF jUsTiCe.'
    actual = sarcastic("Law commonly refers to a system of rules created and enforced through social or governmental institutions to regulate behavior, with its precise definition a matter of longstanding debate. It has been variously described as a science and the art of justice.")
    assert actual == expected


def test_sarcastic_short():
    """Test sarcastic-ifying a short string."""
    expected = 'HeY tHeRe'
    actual = sarcastic("hey there")
    assert actual == expected


def test_sarcastic_empty():
    expected = ""
    actual = sarcastic("")
    assert actual == expected


def test_find_longest_word_empty():
    """Test find_longest_word function"""
    expected = ""
    actual = find_longest_word("")
    assert actual == expected


def test_find_longest_word_short():
    """Test find_longest_word function"""
    expected = "testing"
    actual = find_longest_word("this is some testing")
    assert actual == expected


# run the tests
if __name__ == '__main__':
    unittest.main()
