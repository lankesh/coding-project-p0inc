# Schedule Assistant

### Assumptions
1. Mocked a dummy calendar service
2. Find overlap gives overlapping available slots

### Trade Offs
1. Ignored concurrency in db to reduce the scope of the application

### Available features
1. Set own availability
2. Show own availability
3. Find overlap in schedule between two users
4. Calendar integration

### Upcoming features
1. Set interval between two consecutive slots
    a. This can be good to avoid situations where meeting is extended or to take a break between two consequtive schedules
2. Set reminders
    a. 5 minute before/10 min before/etc...
3. Book slot
4. Cancel bookings
5. Background sync with calendar


## How to run application

### Recomendation
- Use `Python 3.11` to run the application
- Use `python3-venv` to sandbox the dependencies

### Run locally
```bash
# This guide assumes you are using Mac OS or Linux.
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# Change the port number if it is already in use
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

### Run locally using docker compose
```bash
chmod +x run.sh
./run.sh
```


## How to run test cases

### Run tests locally
```bash
# This guide assumes you are using Mac OS or Linux.
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
chmod +x run_tests.sh
./run_tests.sh
```

## How to execute APIs
- Run the application by refering to the [Run Locally](#run-locally) section
- Open <a href="http://0.0.0.0:8000/docs" target="_blank">Open API docs [http://0.0.0.0:8000/docs]</a>
    - Expand the API and click on `Try it out` button
    - Fill in the required details and click on `Execute` button
- Alternatively you may import `openapi.json` into Postman as OpenAPI collection to run the APIs
