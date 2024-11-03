import sys
from pprint import pprint
import pendulum
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
import random
import string
import os

with DAG(
    dag_id="DAG_PYTHON_OPERATOR_2",
    schedule=None,
    start_date=pendulum.datetime(2024, 4, 20, tz="UTC"),
    catchup=False,
):

    def generate_random_numbers():
        # Gerar 20 números inteiros aleatórios no intervalo de 1 a 100
        random_numbers = [random.randint(1, 100) for _ in range(20)]
        # Caminho para salvar o arquivo
        file_path = "./dags/random_numbers.txt"
        # Escrever os números aleatórios no arquivo
        with open(file_path, 'w') as f:
            for num in random_numbers:
                f.write(str(num) + '\n')
        print("Arquivo de números aleatórios criado em:", file_path)
        return 0

    start = EmptyOperator(task_id="start")
    task_python = PythonOperator(task_id="task_python", python_callable=generate_random_numbers)
    end = EmptyOperator(task_id="end")


start >> task_python >> end
