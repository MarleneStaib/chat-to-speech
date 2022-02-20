import requests


def get_token(subscription_key):
    """
    Get authorization token for Azue API.
    """
    fetch_token_url = "https://westeurope.api.cognitive.microsoft.com/sts/v1.0/issuetoken"
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    response = requests.post(fetch_token_url, headers=headers)
    access_token = str(response.text)
    return access_token
