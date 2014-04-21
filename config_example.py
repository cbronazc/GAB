# Change this file to "config.py"

# The name of the user or organization to run these calls on
username = 'my_github_username'

# The domain you send emails from
domain = 'mydomain.com'

# Auto merges pull requests in github
automerger = False
am_repos = ['repo_name'] # Add all repo's you want to automerged here, case sensitive
am_ignore_branches = ['master', 'release'] # Add 'master' here if you don't want to automerge into master


# Send release emails for tags/releases
# if you don't want to send a release out just add -noemail- to the notes
releases = False
release_repos = ['repo_name']
release_contacts = {'repo_name': ['email@me.com', 'email_another@me.com']}

# Github access token - add it to token.txt in the same dir as the file
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

token_file = open(os.path.join(__location__, 'token.txt'));
oauth_key = token_file.read().rstrip('\n')
token_file.close()