# Slack API
1. Create a [Slack App](https://api.slack.com/apps).
2. Install Slack App to Team
3. Copy `Bot User OAuth Access Token` from `OAuth & Permissions` page and create `environment varible` - `export SLACK_API_TOKEN = <Bot User OAuth Access Token>`
4. On the `Events Subscriptions` page enter link of your website + `/events/`, pick next events:
`im_created`, `im_history_changed`, `message.channels`, `message.groups`, `message.im` to `Workspace Events` and `im_created`, `message.channels`, `message.im` to `Bot Events`.
5. On the `OAuth & Permissions` page to a `Scopes` add `files.read`

# Run application

`docker-compose up`

## Run tests

```bash
./manage.py tests
```
