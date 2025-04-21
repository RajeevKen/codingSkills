import requests

import json


class   checkLogin:


    def loginToApp(self, usernme, password):
        """
        This method is to login to site
        Args:
            usernme: usernme 
            password: password
        """

        try:
            out = 1/0
            print(out)

        except ZeroDivisionError as error:
            raise error 




"""
Write a Test in API Testing in Python using Robot Framework
 
API: https://fake-json-api.mock.beeceptor.com/users
 
Get API
 
Validate the value: "Dimitri Pagac"
"""
def get_api(self, name = ""):
    
    try:

        response = requests.get("https://fake-json-api.mock.beeceptor.com/users")

        response.status_code() = 200

        data = response.json()

        for s in data:
            for k, v in s.items():
                if k is 'name':
                    assert v == name, f" Failed due to {v}"

    except Exception as error:
        raise error


get_api(name='Dimitri Pagac')