def palindrome(target: str) -> bool:
    if isinstance(target, str) is False:
        return False
    duplicated_target = target[:]
    reversed_list = list(reversed(duplicated_target))
    for x, y in zip(target, "".join(reversed_list)):
        if x != y:
            return False
    return True
