import datetime
import config
import api

def print_message(merging):
  if merging == True:
    message = "Merging: "
  else:
    message = "Not merging: "
  print message + str(pr_id) + " - " + user + " wants to merge " + head_ref + " into " + base_ref

def merge():
  data = api.merge_pr(repo, pr_id)
  if "merged" in data and data["merged"]==True:
    print "Merged: " + data['sha']
  else:
    print "Failed: " + data['message']

# Main
def run():
  print "Running auto merger at: " + str(datetime.datetime.now())

  for repo in config.am_repos:
    data = api.get_prs(repo)

    if data and data['message'] == "Not Found":
      print "Repo %s not found, make sure it exists"%repo
    else:
      for i in data:
        head_ref=i["head"]["ref"]
        base_ref=i["base"]["ref"]
        user=i["user"]["login"]
        pr_id = i["number"]
        if base_ref in config.am_ignore_branches:
          print_message(False)
        else:
          print_message(True)
          merge(repo, pr_id)
