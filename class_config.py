"""
CMP
"""
# Imports
from abc import abstractmethod, ABC


class GUI(ABC):
    icon = 'icon.ico'
    sticky = 'NSEW'
    style = ''
    padding = 5
    app_size = "520x550"
    title = 'Application'
    theme = 'proxttk-dark'

    @abstractmethod
    def app(self):
        pass
