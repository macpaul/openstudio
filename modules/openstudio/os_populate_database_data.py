
from tests.controllers.populate_os_tables import  *
from gluon import *

class PopulateDatabaseData:

    def get_buttons(self):
        buttons = A(os_gui.get_fa_icon('fa-wheel'),
                                       href= self.populate_all(),
                                       title='Populate all')
        return buttons
    def populate_all(self):
        populate_subscriptions(self)

    def populate_subscriptions(self):
        populate_school_subscriptions()

