from neoutils import NeoAction

class Action(NeoAction):
    def __init__(self, session, message):
        super(Action, self).__init__(session, message)