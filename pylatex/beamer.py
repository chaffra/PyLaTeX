
from .base_classes import Command, Container, Environment, LatexObject, Options
from .package import Package

class Frame(Environment):
    """Beamer frame container class."""
    _latex_name = "frame"
    escape = False
    content_separator = "\n"

    def __init__(self, title=None, options=None, start_arguements=None, ):
        super().__init__(arguments=title, options=options, start_arguments=start_arguements)

class Columns(Environment):
    """Beamer columns container class."""
    _latex_name = "columns"
    escape = False
    content_separator = "\n"

    def __init__(self, arguments=None, options=None, start_arguements=None, ):
        super().__init__(arguments=arguments, options=options, start_arguments=start_arguements)


class Column(Environment):
    """Beamer column container class."""
    _latex_name = "column"
    escape = False
    content_separator = "\n"

    def __init__(self, arguments=None, options=None, start_arguements=None, ):
        super().__init__(arguments=arguments, options=options, start_arguments=start_arguements)

class Block(Environment):
    """Beamer block container class."""
    _latex_name = "block"
    escape = False
    content_separator = "\n"

    def __init__(self, arguments=None, options=None, start_arguements=None, ):
        super().__init__(arguments=arguments, options=options, start_arguments=start_arguements)