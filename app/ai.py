import json

def fake_ai_analyze(payload: dict) -> str:
    size = payload.get("file_size", 0)
    version = payload.get("version", 1)
    name = payload.get("file_name", "file")

    if size < 50_000:
        size_desc = "relatively small"
    elif size < 1_000_000:
        size_desc = "moderate"
    else:
        size_desc = "large"

    if version <= 1:
        ver_desc = "initial upload"
    elif version <= 3:
        ver_desc = "minor update"
    else:
        ver_desc = "major iteration"

    comment = f"File '{name}' is {size_desc}, this looks like a {ver_desc}."
    if size < 20_000 and version <= 2:
        comment += " New change appears insignificant."

    return comment