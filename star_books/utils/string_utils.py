from typing import Dict


def get_class_representation(names_dict: Dict) -> str:
    keys = names_dict.keys()
    res = []
    for key in keys:
        text = f"{key}:{names_dict.get(key)}"
        res.append(text)

    return " ".join(res)
