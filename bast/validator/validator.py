class Rule(object):
    def __init__(self, error=None, pass_=False):
        self.error = error
        self.pass_ = pass_

    def run(self, value):
        raise NotImplementedError("Method cannot be accessed directly")


class Field(object):
    rules = []
    name = ""
    value = ""
    stop_on_error = False

    def __init__(self, name, value, stop_on_error=True):
        self.name = name
        self.value = value
        self.stop_on_error = stop_on_error

    def __iter__(self):
        return len(self.rules)

    def __getitem__(self, item):
        return self.rules[item]

    def add_rule(self, rule_):
        if isinstance(rule_, list):
            for rule in rule_:
                if not isinstance(rule, Rule):
                    raise TypeError('Ensure that the rules is of the Rule instance')
                self.rules.append(rule)
            return self
        elif not isinstance(rule_, Rule):
            raise TypeError('Ensure that the rule is of the Rule instance')
        self.rules.append(rule_)
        return self

    def run(self):
        errors = []
        for rule in self.rules:
            if not rule.run(self.value):
                errors.append(rule.error)
                if self.stop_on_error:
                    break
        return False if errors else True, errors


class validator(object):
    fields = []
    result = []

    @classmethod
    def add(cls, field_):
        if isinstance(field_, list):
            for f in field_:
                if not isinstance(f, Field):
                    raise TypeError('parameter :field must be list of class Field instances')
                cls.fields.append(f)
            return cls
        if not isinstance(field_, Field):
            raise TypeError('parameter :field must be instance of class Field')
        cls.fields.append(field_)
        return cls

    def __iter__(self):
        """ Returns generator to iterate through assigned fields. """
        for rule in self.fields:
            yield rule

    def __len__(self):
        """ Implements built-in len() to return number of assigned fields. """
        return len(self.fields)

    def __getitem__(self, i):
        """ Allows for self[key] access. Will raise IndexError if out of range. """
        return self.fields[i]

    def results(self):
        """ Returns the collated results for the current collection instance. """
        return self.result

    def form(self):
        """ Returns a dict representing the current form in field:value pairs. """
        return {
            field.title: field.value
            for field in self.fields
        }

    def errors(self):
        """ Returns a dict containing only a map of fields with any
        corresponding errors or None if all rules passed.
        """
        return {
                   f['field']: f['errors']
                   for f in self.result
                   if f['errors']
               } or None

    @classmethod
    def run(cls, return_results=False):
        """ Iterates through all associated Fields and applies all attached Rules. Depending on 'return_collated_results',
        this method will either return True (all rules successful), False (all, or some, rules failed)
        or a dictionary list
        containing the collated results of all Field Rules.
        Keyword arguments:
        return_collated_results bool -- Returns dictionary list of Field Rule collated results instead of True or False.
        """
        cls.result = []

        passed = True

        for field in cls.fields:
            result, errors = field.run()

            results = {
                'field': field.name,
                'value': field.value,
                'passed': result,
                'errors': None
            }

            if errors:
                passed = False
                results['errors'] = errors

            cls.result.append(results)

        if return_results:
            return cls.result

        return passed
