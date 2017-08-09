#! /Library/Frameworks/Python.framework/Versions/3.4/bin/python3.4

from __future__ import print_function
import httplib2
import os
import requests, sys

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from datetime import datetime, timedelta

import datetime

SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'

profile_in_office = "%7B%22status_text%22%3A%22In%20the%20office%22%2C%22status_emoji%22%3A%22%3Aoffice%3A%22%7D"
profile_wfh = "%7B%22status_text%22%3A%22Working%20remotely%22%2C%22status_emoji%22%3A%22%3Ahouse_with_garden%3A%22%7D"
profile_vacation = "%7B%22status_text%22%3A%22On%20holiday%22%2C%22status_emoji%22%3A%22%3Apalm_tree%3A%22%7D"
token = "Slack token goes here"

endpoint = "https://slack.com/api/users.profile.set?token=" + token

def set_status(location):
    if location == 'wfh':
        profile = profile_wfh
    elif location == 'holiday':
        profile = profile_vacation
    else:
        profile = profile_in_office

    post_url = endpoint + "&profile=" + str(profile)

    requests.put(post_url)
    


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Creates a Google Calendar API service object and checks today's All day events.

    There's no way of retrieving just All day events, but they have a 'date' property, whilst normal events have a 'dateTime' property, so use that as the indicator.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    
    # Getting events for today only
    startdate = datetime.date.today().strftime("%Y-%m-%d") + 'T00:00:00Z' # 'Z' indicates UTC time
    enddate = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%Y-%m-%d") + 'T00:00:00Z' # 'Z' indicates UTC time
    print('Checking events for today')
    eventsResult = service.events().list(
        calendarId='primary'
        ,timeMin=startdate
        ,timeMax = enddate
        ,singleEvents = 'true'
        ,orderBy='startTime'
        ).execute()
    events = eventsResult.get('items', [])
    
    if not events:
        print('No upcoming events found. Setting status as \"In the office\"')
        set_status('in_office')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        if 'date' in event['start']: 
            if event['summary'] == 'Stuart WFH':
                set_status('wfh')
                print('Status set to wfh')
                break
            elif event['summary'] in ("Stuart Hols","Stuart Holiday"):
                set_status('holiday')
                print('Status set to holiday')
                break
            else:
                set_status('in_office')
                print('Status set to in office')
        else:
            set_status('in_office')
            print('No All day events found. Status set to in office')

if __name__ == '__main__':
    main()
