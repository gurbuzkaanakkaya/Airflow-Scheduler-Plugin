    from datetime import datetime, timedelta
    from airflow import DAG
    from airflow.operators.bash import BashOperator
    from dag_management_plugin.timetables import CronTriggerTimetable, MultipleCronTriggerTimetable, get_schedule_from_variable
    import pendulum

    dag1 = DAG(
        'example_multiple_cron',
        default_args={
            'owner': 'kaanakkaya',
            'depends_on_past': False,
            'email_on_failure': False,
            'email_on_retry': False,
            'retries': 1,
            'retry_delay': timedelta(minutes=5),
        },
        schedule=get_schedule_from_variable('example_multiple_cron', None),
        start_date=datetime(2024, 1, 1),
        catchup=False,
        tags=['multiple-cron'],
    )

    task1 = BashOperator(
        task_id='test',
        bash_command='echo "TEST1"',
        dag=dag1,
    )

    dag2 = DAG(
        'example_single_cron',
        default_args={
            'owner': 'kaanakkaya',
            'depends_on_past': False,
            'email_on_failure': False,
            'email_on_retry': False,
            'retries': 1,
            'retry_delay': timedelta(minutes=5),
        },
        schedule=get_schedule_from_variable('example_single_cron', None),
        start_date=datetime(2024, 1, 1),
        catchup=False,
        tags=['single-cron'],
    )

    task2 = BashOperator(
        task_id='test',
        bash_command='echo "TEST2"',
        dag=dag2,
    )


