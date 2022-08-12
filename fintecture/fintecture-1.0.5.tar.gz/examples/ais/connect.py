from __future__ import absolute_import, division, print_function

import os

import fintecture


fintecture.app_id = os.environ.get("FINTECTURE_APP_ID")
fintecture.app_secret = os.environ.get("FINTECTURE_APP_SECRET")


print("Searching URL to connect with AIS...")

resp = fintecture.AIS.connect(redirect_uri="https://domain.com", state="1234")

print("Redirecting user to {} ...".format(
    resp['meta']['url']
))
print("Success: %r" % (resp))
