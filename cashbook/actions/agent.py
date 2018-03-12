from . import Action
from savings.handlers import ParentHandler

import sys

class CollectContribution(Action):
    # Action methods
    def request_phone_number(self):
        # Set method and action in session
        self.session.set_method_and_action(sys._getframe().f_code.co_name, action=self.__class__.__name__)
        return Action.response("Please provide parent's phone number:")

    def confirm_contribution_collected(self):
        # Set method in session
        self.session.set_method_and_action(sys._getframe().f_code.co_name)

        # Check whether parent exists
        phone_number = self.message.strip()
        parent = ParentHandler.get(phone_number)
        if not parent:
            return Action.release('This parent does not exist.')

        # Get contribution amount
        # Request whether agent collected contribution amount in cash

class CheckCollectionSummary(Action):
    pass