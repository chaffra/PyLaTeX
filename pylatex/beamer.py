
from .base_classes import Command, Container, Environment, LatexObject, Options
from .package import Package

class Frame(Environment):
    """Beamer frame container class."""
    _latex_name = "frame"
    escape = False
    content_separator = "\n"

    def __init__(self, title=None, options=None, start_arguements=None, ):
        super().__init__(arguments=title, options=options, start_arguments=start_arguements)