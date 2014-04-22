import datetime
import config
import api
import shelve
import emailer
import os
from datetime import datetime, timedelta

# https://developer.github.com/v3/repos/releases/

def run():
  # import pdb; pdb.set_trace()
  print "Running release email updates at: " + str(datetime.now())
  __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
  d = shelve.open(os.path.join(__location__, 'releases_db'))
  for repo in config.release_repos:
    data = api.get_releases(repo)
    for i in data:
      process_release(i, repo, d)
  d.close()

def process_release(r, repo, d):
  tag_name=r["tag_name"].encode('ascii','ignore')
  name=r["name"].encode('ascii','ignore')
  notes=r["body"].encode('ascii','ignore')
  release_name = repo + "-" + name
  if release_name not in d.keys():
    d[release_name] = notes
    one_day_ago = datetime.now() - timedelta(hours=24)
    rel_date = datetime.strptime(r['created_at'], "%Y-%m-%dT%H:%M:%SZ")
    if ('-noemail-' not in notes) and (rel_date > one_day_ago):
      print "emailing a new release in %s"%repo
      email_updates(repo, tag_name, name, notes)
    else:
      print "not emailing new release"

def email_updates(repo, tag_name, name, notes):
  subject = "%s version %s has been released"%(repo, tag_name)
  body = "<h2>%s version %s has been released </h2>"%(repo, tag_name)
  body += "<br><b>%s</b>"%name
  body += "<br>" + notes
  emailer.send_email(config.release_contacts[repo], subject, body)