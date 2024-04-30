import uuid
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'airscholar',
    'start_date': datetime(2023, 9, 3, 10, 00)
}

def get_data():
    import requests

    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]

    return res

def format_data(res):
    data = {}
    
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{res['location']['street']['number']} {res['location']['street']['name']}, {res['location']['city']}, {res['location']['state']}, {res['location']['country']}"
    data['email'] = res['email']
    data['phone'] = res['phone']
    data['cell'] = res['cell']
    data['dob'] = res['dob']['date'][:10]
    data['age'] = res['dob']['age']
    data['registered_date'] = res['registered']['date'][:10]
    data['years_registered'] = res['registered']['age']
    data['id_name'] = res['id']['name']
    data['id_value'] = res['id']['value']
    data['nationality'] = res['nat']
    data['picture'] = res['picture']['medium']
    return data

def stream_data():
    import json
    from kafka import KafkaProducer
    import time
    import logging

    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)
    curr_time = time.time()

    while True:
        if time.time() > curr_time + 60: #1 minute
            break
        try:
            res = get_data()
            res = format_data(res)

            producer.send('users_created', json.dumps(res).encode('utf-8'))
        except Exception as e:
            logging.error(f'An error occured: {e}')
            continue

with DAG('user_automation',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
    )