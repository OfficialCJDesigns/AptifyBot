import requests

webhook_url = "https://discord.com/api/webhooks/1069383844718981251/ZNefTmuPAWzF6qQuvSHZVBWevcTpkX7vMzbgumyLHfrjkMmjjTAaUrXRSA-n5Hc47oxZ"

def send_to_webhook(variable):
    payload = {
        "content": str(variable)
    }

    requests.post(webhook_url, json=payload)
