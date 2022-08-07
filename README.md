# Git Anomaly Detector - The Legit Security Home Assignment

this guide will help you to detect and notify suspicious behavior in your integrated
GitHub organization.
The server will run different anomalies to check whether there is a suspicious behavior inside your github repository and will print the event once one of the anomalies were triggered.


## Quick Installation
2. Make sure you have python3 installed
3. Make sure have virtual env installed (If you don't use pip install virtualenv)
4. Clone the repository to your local environment and change directory to it
5. Activate your virtual environment
6. Install all the packages inside requirements.txt using pip install -r requirements.txt

## Debugging
1. Run python main.py (this will run by default on localhost (127.0.0.1) and port 9999)
2. Install ngrok and run it using: ngrok http 9999 (or any other port you chooses, as long as the app is listening to it)
3. Once you get a url, go to the relevant git repository and add the webhook with the url received from ngrok.
4. Choose whether you want to listen to all  events or just specific type of events

## Running the server in production
1. Change directory to the project directory.
2. Run in shell : uvicorn main:app --host <host_ip> --port <port_number> for example: uvicorn main:app --host 0.0.0.0 --port 9999

## How to expand the current anomalies?
- go to event_handlers and add a new class that is inheriting from BaseEventHandler.
- Inside your class constructor make sure to write the event type you are interested in (push,team,repository etc). if the event_type does not exist inside EventTypes enum please add it.
- If the action type you want to subscribe (create,delete, etc..) to is not listed inside ActionTypes enum, please add it there.
- Override notify method, in case you don't want to just the print the event to the screen, but do something else.
