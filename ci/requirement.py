"""Print the one requirement of this package, as pyproject.toml states it."""

import tomllib

with open("pyproject.toml", "rb") as manifest:
    print(tomllib.load(manifest)["project"]["dependencies"][0])
