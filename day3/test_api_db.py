from myenv.day3.database import *
import pytest
import os
from myenv.day3.api_service import app
 
 
 
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
 
 
 
 
def test_get_all_users(client):
   
   
   
def test_add_user(client):
 
 
 
def test_delete_user(client):
   