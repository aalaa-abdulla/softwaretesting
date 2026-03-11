# Let's write 4 test cases to test all the above:
import pytest
from myenv.day3.database import *
import os
 
# use fixure to initialize the database before each test
@pytest.fixture(autouse=True)
def setup_database():
    if os.path.exists("example.db"):
        os.remove("example.db")
    init_db()
    add_user("Ameen")
    add_user("Alaa")
    add_user("Eve")
    yield
    if os.path.exists("example.db"):
        os.remove("example.db")
    
 
def test_database_initialization():
    init_db()
    users = get_all_users()
    assert len(users) == 3
 
 
def test_add_user():
    add_user("Test")
    users = get_all_users()
    assert users[3][1] == "Test"
 
def test_delete_user():
    delete_user(2)
    users = get_all_users()
    assert len(users) == 2
 
def test_get_all_users():
    users = get_all_users()
    assert len(users) == 3
# add_user
# delete_user
# get_all_users