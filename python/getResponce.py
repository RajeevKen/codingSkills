import requests
import json



def get_ids():
    '''
    '''

    responce_data = requests.get('https://reqres.in/api/users?page=2')
    # print(responce_data.json())


    data = responce_data.json()["data"]
    print(data)
    for item in data:
        for k,v in item.items():
            if k == "id":
                print(f'Values if {k} is {v}')

    # for k, v in responce_data.json():
    #     if k == 'data':
    #         for val in v:
    #             print(f'Different ids are {val["id"]}')


get_ids()