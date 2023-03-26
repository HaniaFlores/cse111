from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("Benedict", "Cumberbatch") == "Cumberbatch; Benedict"
    assert make_full_name("Sue", "Rose") == "Rose; Sue"
    assert make_full_name("Shaquille", "O'Neal") == "O'Neal; Shaquille"
    assert make_full_name("Lily-Ann", "Williams") == "Williams; Lily-Ann"

def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Cumberbatch; Benedict") == "Cumberbatch"
    assert extract_family_name("Rose; Sue") == "Rose"
    assert extract_family_name("O'Neal; Shaquille") == "O'Neal"
    assert extract_family_name("Williams; Lily-Ann") == "Williams"

def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == " Sally"
    assert extract_given_name("Cumberbatch; Benedict") == " Benedict"
    assert extract_given_name("Rose; Sue") == " Sue"
    assert extract_given_name("O'Neal; Shaquille") == " Shaquille"
    assert extract_given_name("Williams; Lily-Ann") == " Lily-Ann"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
