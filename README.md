# git_anomaly_detector
# The Legit Home Assignment

this guide will help you to detect and notify suspicious behavior in your integrated
GitHub organization.

The reason I created this project is because I got this project as a home assignment.

In order to run the service please make sure to create a virtualenv.
once you activate the virtual env, make sure to change dir to the project directory and use pip install -r requirements.txt in order to install all relevant packages.

The server will run different anomalies to check whether there is a suspicious behavior inside your github repository.
In order to run the server run the following command : uvicorn main:app --host <host_ip> --port <port_number>, for example:
uvicorn main:app --host 0.0.0.0 --port 9999.

If you want to add additional anomalies, what you need to do is:

- go to event_handlers and add a new class that is inheriting from BaseEventHandler.
- Inside your class constructor make sure to write the event type you are interested in. if the event_type does not exist inside EventTypes enum please add it.
- If the action type you want to subscribe to is not listed inside ActionTypes enum, please add it there.
