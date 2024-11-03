from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

# Definindo argumentos padrão do DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1)
    }

# Definindo a DAG
with DAG(
    'DAG_HELLO',
    default_args=default_args,
    description='DAG simples que imprime "Olá, mundo!" usando o BashOperator',
    schedule_interval=None,
) as dag:

    # BashOperator para imprimir "Olá, mundo!" no console
    task_hello = BashOperator(
        task_id='task_hello',
        bash_command='echo "Olá, mundo!"',
    )

    # Definindo a ordem de execução das tarefas
    task_hello