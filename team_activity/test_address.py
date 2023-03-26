from address import extract_city, \
    extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_city("50 N W Temple St, Salt Lake City, UT 84150") == "Salt Lake City"
    assert extract_city("77 Massachusetts Ave, Cambridge, MA 02139") == "Cambridge"

def test_extract_state():
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_state("50 N W Temple St, Salt Lake City, UT 84150") == "UT"
    assert extract_state("77 Massachusetts Ave, Cambridge, MA 02139") == "MA"
    

def test_extract_zipcode():
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"
    assert extract_zipcode("50 N W Temple St, Salt Lake City, UT 84150") == "84150"
    assert extract_zipcode("77 Massachusetts Ave, Cambridge, MA 02139") == "02139"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
