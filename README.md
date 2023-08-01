# Data_Generator



docker-compose up --build web

docker-compose up

---
### conecting to Django-Admin
sudo docker exec -it generator_web_1 bash

##### after_connecting:

- python3 manage.py migrate
- python3 manage.py createsuperuser --username root --email root@email.com
- python3 manage.py create_base_dataset

---
### conecting to Postgres
sudo docker exec -it generator_db_1 bash

psql -U postgres

##### see details:
- *for chunks:*  
  - SELECT hypertable_schema, hypertable_name, chunk_name, primary_dimension, range_start, range_end 
    FROM timescaledb_information.chunks;

 
- *for retention_policy:*
  - SELECT config schedule_interval, job_status, last_run_status, last_run_started_at, js.next_start, total_runs, total_successes, total_failures 
    FROM timescaledb_information.jobs j JOIN timescaledb_information.job_stats js
    ON j.job_id = js.job_id
  WHERE j.proc_name = 'policy_retention';


- *for hypertable:*
  - SELECT * FROM timescaledb_information.hypertables;


---
### conecting to Metabase
localhost:3000


