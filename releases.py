import datetime
import config
import api
import shelve
import emailer
import os

def run():
  # import pdb; pdb.set_trace()
  print "Running release email updates at: " + str(datetime.datetime.now())
  __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
  d = shelve.open(os.path.join(__location__, 'releases_db'))
  for repo in config.release_repos:
    data = api.get_releases(repo)
    for i in data:
      tag_name=i["tag_name"].encode('ascii','ignore')
      name=i["name"].encode('ascii','ignore')
      notes=i["body"].encode('ascii','ignore')
      release_name = repo + "-" + name
      if release_name not in d.keys():
        d[release_name] = notes
        if '-noemail-' not in notes:
          print "emailing a new release in %s"%repo
          email_updates(repo, tag_name, name, notes)
  d.close()

def email_updates(repo, tag_name, name, notes):
  subject = "%s version %s has been released"%(repo, name)
  body = "<h2>%s version %s has been released </h2>"%(repo, name)
  body += "\r\n<b>%s</b>"%
  body += "\r\n" + notes
  emailer.send_email(config.release_contacts, subject, body)