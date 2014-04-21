#!/usr/bin/env python2.7
import automerger
import releases
import config

if config.automerger:
  automerger.run()

if config.releases:
  releases.run()
