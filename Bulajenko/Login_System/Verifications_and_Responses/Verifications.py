from re import search


class Verifications:
    """
    Makes verifications into
    the inputs fields.
    """
    @staticmethod
    def empty_fields(fields) -> bool:
        for field in fields:
            if field.strip() == '':
                return True

        return False

    @staticmethod
    def is_email(input_) -> bool:
        if search(r'@.*\.com|ru', input_):
            return True

        else:
            return False

    @staticmethod
    def special_characters(inputs) -> bool:
        for input_ in inputs:
            if search(r'.*!.*|.*#.*|.*\$.*|.*%.*'
                      r'|.*¨.*|.*&.*|.*\*.*|.*\+.*|.*".*|.*\'.*',
                      input_):
                return True

        return False

    @staticmethod
    def is_phone(input_) -> bool:
        if search(r"(\s*)?(\+)?([- _():=+]?\d[- _():=+]?){6,14}(\s*)?", input_):
            return True
        return False

    @staticmethod
    def is_digital (input_) -> bool:
        if input_.isdigit():
            return True
        return False
