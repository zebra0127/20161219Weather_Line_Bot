# Weaher Line Bot

[Line Message API](https://devdocs.line.me/en/#messaging-api) using [line-bot-sdk-python](https://github.com/line/line-bot-sdk-python).

## Setup

### Register
Go to Line [Business Center](https://business.line.me/zh-hant/).


### HTTPS Server
I use [Heroku](https://www.heroku.com) as a server .
Get an account and create a project.

Then open terminal
$ heroku login
$ heroku git:clone -a "your heroku project name"
$ cd "your heroku project name"

Then put all these file into the directory.

Then, after putting all these file into the directory.
$ git add .
$ git commit -am "make it better"
$ git push heroku master

### Set Webhook URL
Set webhook url on your `LINE Developers` page to `https://"your domain name"/echobot/callback/`

### Remember
Set these three variables. 1. SECRET_KEY 2. LINE_CHANNEL_ACCESS_TOKEN 3. LINE_CHANNEL_SECRET

You can do it by: 1. Set in your Heroku project's setting page. 2. Set in weather_bot/settings_secret.py.

