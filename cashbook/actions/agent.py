from . import Action
from savings.handlers import ParentHandler, SavingPlanHandler, SavingHandler

import sys

class CollectContribution(Action):
    def __init__(self, session, message):
        super(CollectContribution, self).__init__(session, message)
        self.saving_handler = SavingHandler(session)

    # Action methods
    def request_phone_number(self):
        # Set method and action in session
        self.session.set_method_and_action(sys._getframe().f_code.co_name, action=self.__class__.__name__)
        return Action.response("Please provide parent's phone number:")

    def request_confirmation(self):
        # Set method in session
        self.session.set_method_and_action(sys._getframe().f_code.co_name)

        # Check whether parent exists
        phone_number = self.message.strip()
        parent = ParentHandler.get(phone_number)
        if not parent:
            self.session.set_success()
            return Action.release('This parent does not exist.')

        # Get saving plan
        sp = SavingPlanHandler.get(parent)

        # Create saving record
        self.saving_handler.create(sp)

        # Request whether agent collected contribution amount in cash
        return Action.response('Confirm that you have collected {} Naira from parent.\n1. Yes\n2. No'.format(
            sp.contribution
        ))

    def confirm_contribution_collected(self):
        # Set method in session
        self.session.set_method_and_action(sys._getframe().f_code.co_name)

        # Record cash collected
        confirmation = self.message.strip()

        if confirmation == '2':
            # Delete saving record
            self.saving_handler.delete()

            # Set session success
            self.session.set_success()

            return Action.release('You cancelled this transaction.')

        if confirmation == '1':
            # Set session success
            self.session.set_success()

            # Send SMS notification to parent
            return Action.release("Success! You've collected contribution.")

class CheckCollectionSummary(Action):
    pass