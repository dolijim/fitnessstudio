from ._anvil_designer import KursuebersichtTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Kursuebersicht(KursuebersichtTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  @handle("button_startseite_kursuebersicht", "click")
  def button_startseite_kursuebersicht_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("Startseite", row_dict=self.item)
