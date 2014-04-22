#Github Api Bot 

### Setup

Edit config_example.py to be config.py, then edit the variables in the config to do the following things

* Automerge pull requests for certain repositories
* Send emails to people everytime a release is created in github, with the body made up of the release notes.

### Github Auth

Make a token on Github and paste it into token.txt in the project root

### Run

Run every 5 minutes:

`*/5 * * * * /usr/local/bin/python2.7 /path/to/gab/gab.py > /path/to/gab/logfile.log 2>&1`



### Todo

* Nothing ?