from platform_http import Client


def load(client: Client, path: str) -> dict:
    response = client.get(path, timeout=30)
    return response.json()
