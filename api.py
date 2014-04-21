import config
import requests
import json

base="https://api.github.com/repos/"

def merge_pr(repo, pr_id):
  r = requests.put(base + "%s/%s/pulls/%d/merge"%(config.username, repo, pr_id,),
    data=json.dumps({"commit_message": "Auto_Merge"}),
    auth=('token', config.oauth_key))
  return r.json()

def get_prs(repo):
  r = requests.get(base + '%s/%s/pulls'%(config.username, repo), auth=('token', config.oauth_key))
  return r.json()

def get_releases(repo):
  r = requests.get(base + '%s/%s/releases'%(config.username, repo), auth=('token', config.oauth_key))
  return r.json()
