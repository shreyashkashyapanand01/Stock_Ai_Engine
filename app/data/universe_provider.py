import json
import os


def load_universe():

    file_path = os.path.join(
        os.path.dirname(__file__),
        "universe_cache.json"
    )

    with open(file_path, "r") as f:
        data = json.load(f)

    return data["symbols"]