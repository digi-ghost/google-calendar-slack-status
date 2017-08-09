# google-calendar-slack-status
A Python script that checks your Google calendar for specific strings and uses those to update your Slack status.

Prerequisites
In order for this script to work you'll need to set up two things:
1. A token that allows you to set your Slack status
2. A json file that contains the Google client secrets (client_secret.json) that allows you to check your calendar. 

1. Slack token
This script uses the Legacy tokens for Slack, information on which can be found here: https://api.slack.com/custom-integrations/legacy-tokens
Generate a token that allows you to update your status, and make a note of it.

2. Google client_secret.json
This is simply a case of following sections 1 and 2 on this page: https://developers.google.com/google-apps/calendar/quickstart/python


Configuration

Config is simple:
1. place the client_secret.json file in your working directory
2. add you 
