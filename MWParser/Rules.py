class RuleList:
    def __init__(self, rule_list=[]):
        self.rule_list = [Rule(rule) for rule in rule_list]

    def add_rule(self, rule):
        self.rule_list.append(rule)

    def remove_rule(self, rule):
        self.rule_list.remove(rule)

    def test(self, element):
        for rule in self.rule_list:
            if rule.test(element):
                return True

        return False


class Rule:
    def __init__(self, rule):
        self.rule = rule

    def __logic(self, element, rule, operator):
        result = None
        if operator == "$not":
            return not self.__test(element, rule)

        if operator == "$or":
            result = False
            for sub_rule in rule:
                result = result or self.__test(element, sub_rule)

        if operator == "$and":
            result = True
            for sub_rule in rule:
                result = result and self.__test(element, sub_rule)

        return result

    def __test(self, element, rule):
        match = True
        for key in rule:
            if key in ["$not", "$and", "$or"]:
                match = match and self.__logic(element, rule[key], key)
            elif key == "name":
                match = match and (element.name == rule[key])
            else:
                if not (key in element.attrs):
                    return False
                if type(element[key]) is list:
                    match = match and (rule[key] in element[key])
                else:
                    match = match and rule[key] == element[key]

        return match

    def __eq__(self, other):
        return self.rule == other.rule

    def test(self, element):
        return self.__test(element, self.rule)
