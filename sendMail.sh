
curl -s --user 'api:key-899559bc61f3f7813c1ab8fb1ba962a2' \
    https://api.mailgun.net/v3/sandboxf68740cd47204608aa341e43c951e1ca
.mailgun.org/messages \
    -F from='Excited User <mailgun@sandboxf68740cd47204608aa341e43c951e1ca
.mailgun.org>' \
    -F to=kostyabobikov@gmail.com \
    -F to=bar@example.com \
    -F subject='Hello' \
    -F text='Testing some Mailgun awesomness!'

