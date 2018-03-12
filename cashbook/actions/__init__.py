class Action(object):
    RELEASE = {'Type': 'Release'}

    @staticmethod
    def error(message):
        r = Action.RELEASE
        r.update({'Message': 'Error - ' + message})
        return r

    @staticmethod
    def response(message):
        r = {'Type': 'Response'}
        r.update({'Message': message})
        return r
    
    @staticmethod
    def release(message):
        r = Action.RELEASE
        r.update({'Message': message})
        return r