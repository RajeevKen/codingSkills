import requests
import json


# get Boxing Day out of dates

def get_boxing_date():
    '''
    '''
    responce_data = requests.get("https://www.gov.uk/bank-holidays.json")
    events_data = responce_data.json()
    # print(events_data.items())
    boxing_day_list = []
    for k, v in events_data.items(): 
        for keys, values in v.items():
            # print(k)
            # print(v)
            if keys == "events":
                # print(v)
                for event in values:
                    # print(event)
                    for ke, va in event.items():
                        if va=="Boxing Day":
                            boxing_day_list.append(event["date"])


    # return  boxing_day_list
    print(boxing_day_list)
    print(len(boxing_day_list))



# (get_boxing_date())

def do_math():
    '''
    '''
    input_st = "9+8+5+3-2-6+5"
    summ = int(input_st[0])
    # x = ""
    for x in range(len(input_st)-1):
        # if not x.isnumeric():
            if input_st[x] == "+":
                summ += int(input_st[x+1])
            if input_st[x] == "-":
                summ -= int(input_st[x+1])

    return summ
    # num_list = input_st.split("-")
    # print(num_list)

print(do_math())

