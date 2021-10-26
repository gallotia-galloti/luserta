"""Util to update package version."""
import re

import requests

latest_version = re.search(
    r"([\d+].[\d+].[\d+]).",
    list(
        requests.get("https://test.pypi.org/pypi/luserta/json").json().get("releases")
    )[-1],
).group(1)

patch_number = latest_version.split(".")[-1]
new_patch_number = int(patch_number) + 1
new_version = latest_version.split(".")[:-1]
new_version.append(str(new_patch_number))  # + ".dev")
print(".".join(new_version))
