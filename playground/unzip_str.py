import re


def unzip_str(target: str) -> str:
    result = re.findall(r"(\D)(\d+)", target)

    if not result:
        raise TypeError
    result_str = ""

    for t in result:
        s, i = t
        for _ in range(int(i)):
            result_str += s
    return result_str
