# The Legit Home Assignment
# git_anomaly_detector

this guide will help you to detect and notify suspicious behavior in your integrated
GitHub organization.

In order to run the service please make sure to have python3 installed and virtualenv (pip install virtualenv).
once you activate the virtual env, make sure to change dir to the project directory and use pip install -r requirements.txt in order to install all relevant packages.

The server will run different anomalies to check whether there is a suspicious behavior inside your github repository and will print the event once one of the anomalies were triggered.
Once you installed all the packages from the requirements.txt file, please run the following command to run the server:
uvicorn main:app --host <host_ip> --port <port_number>
for example: uvicorn main:app --host 0.0.0.0 --port 9999.

If you want to add additional anomalies, what you need to do is:

- go to event_handlers and add a new class that is inheriting from BaseEventHandler.
- Inside your class constructor make sure to write the event type you are interested in (push,team,repository etc). if the event_type does not exist inside EventTypes enum please add it.
- If the action type you want to subscribe (create,delete, etc..) to is not listed inside ActionTypes enum, please add it there.
- Override notify method, in case you don't want to just the print the event to the screen, but do something else.
