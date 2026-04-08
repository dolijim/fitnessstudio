from ._anvil_designer import StartseiteTemplate
from anvil import *
import anvil.server


class Startseite(StartseiteTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("button_kursuebersicht", "click")
  def button_kursuebersicht_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
