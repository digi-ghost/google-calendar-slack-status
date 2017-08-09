# google-calendar-slack-status
A Python script that checks your Google calendar for specific strings in All day events and uses those to update your Slack status. Note that this is only useful if you use All day events within Google Calendar to specify your location.

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
2. add your Slack token into line 23 of set_status.py
3. Run set_status.py
4. Update the relevant parts of the script (namely the for loop in lines 91 - 100) to reflect how you describe your location for the day..

Now that this has been done, and you've tested that the script works as expected (an update to an All day event in your calendar is reflected in your Slack status) then you just need to arrange for this to be run regularly.

On a Linux based machine this can be done using launchd, or a cron job. As OSX based application that allows simple creation of launchd agents is LaunchControl, found here: http://www.soma-zone.com/LaunchControl/


