from platform_http import Client


def load(client: Client, path: str) -> dict:
    response = client.fetch(path, 30)
    return response.json
