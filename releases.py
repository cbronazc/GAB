import datetime
import config
import api
import shelve
import emailer

def run():
  # import pdb; pdb.set_trace()
  print "Running release email updates at: " + str(datetime.datetime.now())
  __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
  d = shelve.open(os.path.join(__location__, 'releases_db')
  for repo in config.release_repos:
    data = api.get_releases(repo)
    for i in data:
      name=i["tag_name"].encode('ascii','ignore')
      notes=i["body"].encode('ascii','ignore')
      if name not in d.keys():
        d[repo + "-" + name] = notes
        if '-noemail-' not in notes:
          print "emailing a new release in %s"%repo
          email_updates(repo, name, notes)
      else:
        print "no new releases"
  d.close()

def email_updates(repo, name, notes):
  subject = "%s version %s has been released"%(repo, name)
  body = "<h2>%s version %s has been released </h2>"%(repo, name)
  body += "\r\n" + notes
  emailer.send_email(config.release_contacts, subject, body)