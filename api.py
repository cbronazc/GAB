import config
import requests
import json

base="https://api.github.com"

def authenticate():
  r = requests.get(base, auth=('token', config.oauth_key))
  return r.status_code

def merge_pr(repo, pr_id):
  r = requests.put(base + "/repos/%s/%s/pulls/%d/merge"%(config.username, repo, pr_id,),
    data=json.dumps({"commit_message": "Auto_Merge"}),
    auth=('token', config.oauth_key))
  return r.json()

def get_prs(repo):
  r = requests.get(base + '/repos/%s/%s/pulls'%(config.username, repo,), auth=('token', config.oauth_key))
  return r.json()

def get_releases(repo):
  r = requests.get(base + '/repos/%s/%s/releases'%(config.username, repo,), auth=('token', config.oauth_key))
  return r.json()
