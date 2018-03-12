from . import Action

import sys

class CollectContribution(Action):
    # Action methods
    def request_phone_number(self):
        # Set method and action in session
        self.session.set_method_and_action(sys._getframe().f_code.co_name, action=self.__class__.__name__)
        return Action.response("Please provide parent's phone number:")

class CheckCollectionSummary(Action):
    pass