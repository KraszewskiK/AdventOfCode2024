def solve_part1(input_data: str) -> int:
    rules, updates = get_rules_and_updates(input_data)

    result = 0
    for update in updates:
        if is_update_in_correct_order(update, rules):
            result += int(update[(len(update)) // 2])
    return result


def solve_part2(input_data: str) -> int:
    rules, updates = get_rules_and_updates(input_data)
    updates = [update for update in updates if not is_update_in_correct_order(update, rules)]

    for update in updates:
        for i, page in enumerate(update):
            for j, preceding_page in enumerate(update[:i]):
                if page in rules.get(preceding_page, []):
                    update.insert(j, update.pop(i))
                    break

    return sum(int(update[(len(update)) // 2]) for update in updates)


def get_rules_and_updates(input_data: str) -> tuple[dict[str, list[str]], list[list[str]]]:
    rules, updates = input_data.strip().split("\n\n")
    rules = [rule.split("|") for rule in rules.splitlines()]
    rules = {rule[0]: [_rule[1] for _rule in rules if _rule[0] == rule[0]] for rule in rules}
    updates = [update.split(",") for update in updates.splitlines()]
    return rules, updates


def is_update_in_correct_order(update: list[str], rules: dict[str, list[str]]) -> bool:
    for i, page in enumerate(update):
        for following_page in rules.get(page, []):
            if following_page in update and update.index(following_page) < i:
                return False
    return True
