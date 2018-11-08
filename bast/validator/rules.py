from .validator import Rule
import re


class matches(Rule):
    """
    Rule to check if a value matches another value.

    Arguments:
        match str         ----  Value to compare against associated value
        error str         ----  User defined error message (Optional)
        pass_ bool        ----  Pass through as success if value passed is blank (Optional)
    """
    def __init__(self, match, error=None, pass_=False):
        if not error:
            error = "Values `{}` and `{}` do not match."

        super(matches, self).__init__(error, pass_)
        self.match = match

    def run(self, value):
        if self.pass_ and not value.strip():
            return True

        if self.match != value:
            self.error = self.error.format(value, self.match)
            return False
        return True


class regex(Rule):
    """
    Applies Regular Expression to a given field value
    Arguments:
        expression str      --- The Regular expression to apply
        error str         ----  User defined error message (Optional)
        pass_ bool        ----  Pass through as success if value passed is blank (Optional)
    """
    def __init__(self, expression, error=None, pass_=False):
        if not error:
            error = "Values `{}` and `{}` do not match"

        super(regex, self).__init__(error, pass_)
        self.exp = expression

    def run(self, value):
        if self.pass_ and not value.strip():
            return True

        if not self.exp:
            raise ValueError('Rule requires a Regular Expression')

        try:
            regex_ = re.compile(self.exp)
            if not regex_.match(value):
                self.error = self.error.format(value, self.exp)
                return False
        except Exception as e:
            raise ValueError("Expression `{}` failed with the following error: {}".format(self.exp, e))
        return True


class is_email(regex):
    """
    Applies Regular expression to determine if given value is a valid email address. Inherits from the Base **regex**
    class
    Arguments:
        error str         ----  User defined error message (Optional)
        pass_ bool        ----  Pass through as success if value passed is blank (Optional)
    """
    def __init__(self, error=None, pass_=False):
        if not error:
            error = 'This is not a valid email address.'

        super(is_email, self).__init__(r'^[a-zA-Z0-9._%-+]+@[a-zA-Z0-9._%-]+.[a-zA-Z]{2,6}$', error, pass_)


class is_numeric(regex):
    """
    Applies Regular Expression to determine if given field value is numeric-only. Inherits from the **regex** class
    Arguments:
        error str         ----  User defined error message (Optional)
        pass_ bool        ----  Pass through as success if value passed is blank (Optional)
     """

    def __init__(self, error=None, pass_=False):
        if not error:
            error = 'This is not a number.'
        super(is_numeric, self).__init__(r'^[0-9]*$', error, pass_)


class is_alphabet(regex):
    """
    Applies Regular Expression to determine if given field value is alpha-only. Inherits from the **regex** class
    Arguments:
        error str         ----  User defined error message (Optional)
        pass_ bool        ----  Pass through as success if value passed is blank (Optional)
    """

    def __init__(self, error=None, pass_=False):
        if not error:
            error = 'This is not an alpha-only string.'
        super(is_alphabet, self).__init__('^[a-zA-Z]*$', error, pass_)


class is_alpha_numeric(regex):
    """
    Applies Regular Expression to determine if given field value is alpha-numeric. Inherits from the **regex** class
    Arguments:
        error str         ----  User defined error message (Optional)
        pass_ bool        ----  Pass through as success if value passed is blank (Optional)
    """

    def __init__(self, error=None, pass_=False):
        if not error:
            error = 'This is not an alpha-numeric string.'
        super(is_alpha_numeric, self).__init__(r'^[a-zA-Z0-9]*$', error, pass_)


class is_required(Rule):
    """ Used to determine if given field is empty. """

    def __init__(self, error=None, pass_=False):
        if not error:
            error = 'This field requires a value.'
        super(is_required, self).__init__(error, pass_)

    def run(self, value):
        """ Determines if value value is empty.
        Keyword arguments:
        value str -- the value of the associated field to compare
        """
        if self.pass_ and not value.strip():
            return True

        if not value:
            return False
        return True


class required_length(Rule):
    """ Used to determine whether the given associated field value's character length equals
    the given maximum amount. """

    def __init__(self, length, strip=False, error=None, pass_=False):
        """ Constructor that instantiates a class instance and properties.
        Keyword arguments:
        length int         -- Absolute maximum character length.
        strip bool         -- Used to strip whitespace from the given field value. (optional)
        error str          -- A user-defined error messaged for a failed  (optional)
        pass_ bool -- Pass through as success if field value is blank. (optional)
        """
        if not error:
            error = "String `{}` length does not equal `{}`"
        super(required_length, self).__init__(error, pass_)
        self.length = int(length)
        self.strip = bool(strip)

    def run(self, value):
        """ Determines if value character length equal self.length.
        Keyword arguments:
        value str -- the value of the associated field to compare
        """
        if self.pass_ and not value.strip():
            return True

        if len((value.strip() if self.strip else value)) != self.length:
            self.error = self.error.format(value, self.length)
            return False
        return True


class length_between(Rule):
    """ Used to determine whether the given associated field value's character length is
    within the given range. """

    def __init__(self, minimum, maximum, **kwargs):
        """ Constructor that instantiates a class instance and properties.
        Keyword arguments:
        minimum int        -- Absolute minimum character length.
        max int            -- Absolute maximum character length.
        strip bool         -- Used to strip whitespace from the given field value. (optional)
        error str          -- A user-defined error messaged for a failed  (optional)
        pass_ bool -- Pass through as success if field value is blank. (optional)
        """
        if not kwargs.get('error', None):
            kwargs['error'] = "String `{}` length is not within `{}` and `{}`"
        super(length_between, self).__init__(kwargs.get('error', None), kwargs.get('pass_', False))
        self.minimum = int(minimum)
        self.maximum = int(maximum)
        self.strip = kwargs.get('strip', False)

    def run(self, value):
        """ Determines if value character length is between self.minimum and self.maximum.
        Keyword arguments:
        value str -- the value of the associated field to compare
        """
        if self.pass_ and not value.strip():
            return True

        if self.minimum <= len((value.strip() if self.strip else value)) <= self.maximum:
            return True

        self.error = self.error.format(value, self.minimum, self.maximum)
        return False


class in_list(Rule):
    """ Used to determine if the associated field's value exists within the specified list. """

    def __init__(self, given_list, strip=False, error=None, pass_=False):
        """ Constructor that instantiates a class instance and properties.
        Keyword arguments:
        given_list list          -- List containing values to evaluate.
        strip bool         -- Used to strip whitespace from the given field value. (optional)
        error str          -- A user-defined error messaged for a failed  (optional)
        pass_ bool -- Pass through as success if field value is blank. (optional)
        """
        if not error:
            error = "Value of `{}` is not within the list"
        super(in_list, self).__init__(error, pass_)
        self.given_list = given_list
        self.strip = strip

    def run(self, value):
        """ Checks if value is included within self.given_list.
        Keyword arguments:
        value str -- the value of the associated field to compare
        """
        if self.pass_ and not value.strip():
            return True

        if (value.strip() if self.strip else value) not in self.given_list:
            self.error = self.error.format(value)
            return False
        return True


class is_type(Rule):
    """ Rule that compares the associated field's value against a specified data type. """

    def __init__(self, asserted_type, error=None, pass_=False):
        """ Constructor that instantiates a class instance and properties.
        Keyword arguments:
        asserted_type mixed -- The type to compare the field value against.
        error str           -- A user-defined error messaged for a failed  (optional)
        pass_ bool  -- Pass through as success if field value is blank. (optional)
        """
        if not error:
            error = "Type of `{}` is not of type `{}`"
        super(is_type, self).__init__(error, pass_)
        self.asserted_type = asserted_type

    def run(self, value):
        """ Compares value against self.asserted_type.
        Keyword arguments:
        value str -- the value of the associated field to compare
        """
        if self.pass_ and not value.strip():
            return True

        if not isinstance(value, type(self.asserted_type)):
            self.error = self.error.format(type(value), self.asserted_type)
            return False
        return True
