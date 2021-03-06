import os
import logging

LOG_LEVEL = logging.WARNING
PLATFORM = "text"

# List of Admin user ids. Several actions are reserved for admin users.
# Make sure to use appropriate user ids for your platform (slack user ids vs just text - which is text)
ADMINS = ["text"]

# URL used by GZ to return a random Godzilla GIF
GZ_GIF_URL = "http://api.giphy.com/v1/gifs/search?q=godzilla&api_key=dc6zaTOxFJmzC"

# === SLACK ===
SLACK_TOKEN = "yourtoken"
# Find the bot's Slack ID. You can obtain this using Slack's API tester - https://api.slack.com/methods/users.list
# or by inspecting the tokyo debug logs (by setting LOG_LEVEL = logging.DEBUG). It should look like U023BECGF.
SLACK_USER_ID = "U12345678"

# === GOOGLE ===
# You'll need to create a google project from the Google Developer Console and enable the following APIs:
# Admin SDK, Gmail API, Calendar API
# You then need to create a service account with domain delegation authority.
# NOTE: Make sure that the service account's client
# ID has been authorized to act with domain authority on the following scopes:
# https://www.googleapis.com/auth/admin.directory.domain.readonly
# https://www.googleapis.com/auth/admin.directory.user
# https://www.googleapis.com/auth/admin.directory.group
# https://www.googleapis.com/auth/gmail.send
# https://www.googleapis.com/auth/calendar
# This should contain your Google Service Account key json file contents (downloaded when creating a google service account from the google developer console).
# Paste the contents of the file here as a python dictionary.
GOOGLE_SERVICE_ACCOUNT_JSON = {}
# Email of super admin to act on the behalf of
GOOGLE_SUPER_ADMIN = "admin@example.com"
# Google Group Mapping. These should be the left side of the google group's
# email address - i.e. dev of dev@example.com. GDES & GDEV are labels for
# designer sounding or developer sounding titles (respectively). If all parts
# of a job title make sense for this kind of label, Godzillops auto assigns groups upon user creation.
GOOGLE_GROUPS = {"GDES": ["design"], "GDEV": ["dev"], "GCRE": ["creatives"], "GFOU": ["founders"]}
GOOGLE_DEV_ROLES = ["backend", "frontend"]
# Main company calendar to add new google users to as readers
GOOGLE_CALENDAR_ID = "cal-id@group.calendar.google.com"
# Custom Welcome email text that can be configured
GOOGLE_WELCOME_TEXT = ""
GOOGLE_WELCOME_ATTACHMENTS = []

# === TRELLO ===
# Org ID or name
TRELLO_ORG = "yourorg"
# Get this key from https://trello.com/app-key
TRELLO_API_KEY = "yourkey"
# Generate a token via an API call - http://stackoverflow.com/questions/17178907/how-to-get-a-permanent-user-token-for-writes-using-the-trello-api
TRELLO_TOKEN = "yourtoken"

# === GITHUB ===
# Org ID or name
GITHUB_ORG = "yourorg"
# Generate a token - https://developer.github.com/v3/oauth_authorizations/#create-a-new-authorization
# The necessary oauth scopes are: admin:org
# Curl example: curl -u githubuser -X POST --data '{"scopes":["admin:org"], "note": "godzillops"}' https://api.github.com/authorizations
GITHUB_ACCESS_TOKEN = "yourtoken"
# Dev roles with teams to invite new members to. Get this id by running `GET /orgs/:org/teams` and
# selecting the team ids you want to use
GITHUB_DEV_ROLES = {"backend": [1234567, 8901234], "frontend": [1234567]}
# Currently, GZ supports adding abacus users by posting to a Zapier webhook that is configured to
# fire the 'Invite New User' Abacus action.
ABACUS_ZAPIER_WEBHOOK = "https://hooks.zapier.com/hooks/catch/asdf"

if os.path.exists("config_private.py"):
    # Use config_private for your own personal settings - default to be git ignored.
    # Yup, intentionally using wildcard import to shadow the default values
    from config_private import *
