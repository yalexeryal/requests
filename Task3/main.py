import requests
from datetime import datetime
from pprint import pprint


def get_questions(days, tag):
    end_date = int(datetime.timestamp(datetime.now()))
    start_date = end_date - days * 86400

    PARAMS = {
        'fromdate': start_date,
        'todate': end_date,
        'tagged': tag,
        'site': 'stackoverflow'
    }

    resp = requests.get('https://api.stackexchange.com/2.2/questions', params=PARAMS)
    pprint(resp)
    for question in resp.json().get('items'):
        print(('Question: ' + question['title']).upper())

get_questions(2, 'python')
