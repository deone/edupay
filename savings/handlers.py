from models import Agent, Parent

class AgentHandler:
    @staticmethod
    def get(phone_number):
        try:
            agent = Agent.objects.get(user__username=phone_number)
        except Agent.DoesNotExist:
            return None
        return agent

class ParentHandler:
    @staticmethod
    def get(phone_number):
        try:
            parent = Parent.objects.get(user__username=phone_number)
        except Parent.DoesNotExist:
            return None
        return parent