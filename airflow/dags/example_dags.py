from datetime import datetime, timedelta
from textwrap import dedent

# DAG 객체를 인스턴스로 만들어주기 위해 모듈 불러오기
from airflow import DAG

# Operators / Taks 정의
# 다양한 Operator가 있고 하는 일이 다 다름 
from airflow.operators.bash import BashOperator

# DAG를 구성할 때 필요한 default args 셋팅 
default_args = {
    'owner': 'owner-name',
    'depends_on_past': False,
    'email': ['your-email@g.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=15),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

# 객체 인스턴스 생성(구체화)
with DAG(
    'tutorial',  # DAG 이름 
    default_args=default_args, 
    description='A simple tutorial DAG',   
    schedule_interval=timedelta(days=1), # DAG 실행 간격
    start_date=datetime(2022, 2, 1),     # DAG 처음 실행 날짜
    catchup=False,
    tags=['example-sj'],                
) as dag:

    # Task 만들기
    t1 = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    t2 = BashOperator(
        task_id='sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
    )
    t1.doc_md = dedent(
        """\
    #### Task Documentation
    You can document your task using the attributes `doc_md` (markdown),
    `doc` (plain text), `doc_rst`, `doc_json`, `doc_yaml` which gets
    rendered in the UI's Task Instance Details page.
    ![img](http://montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)
    """
    )

    dag.doc_md = __doc__  # providing that you have a docstring at the beginning of the DAG
    dag.doc_md = """
    This is a documentation placed anywhere
    """  # otherwise, type it like this
    templated_command = dedent(
        """
    {% for i in range(5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7)}}"
        echo "{{ params.my_param }}"
    {% endfor %}
    """
    )

    t3 = BashOperator(
        task_id='templated',
        depends_on_past=False,
        bash_command=templated_command,
        params={'my_param': 'Parameter I passed in'},
    )
    # Task 연결 
    # ">>", "<<" , "[]"를 이용하여 DAG 그래프 그리기 가능 
    t1 >> [t2, t3]