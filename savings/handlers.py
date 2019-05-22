from .models import Agent, Parent, SavingPlan, Saving

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

class SavingPlanHandler:
    @staticmethod
    def get(parent):
        try:
            sp = SavingPlan.objects.get(parent=parent, is_active=True)
        except SavingPlan.DoesNotExist:
            return None
        return sp

class SavingHandler:
    def __init__(self, session):
        self.session = session.get_or_create()[0]

    def create(self, saving_plan):
        return Saving.objects.create(session=self.session, saving_plan=saving_plan)

    def delete(self):
        saving = Saving.objects.get(session=self.session)
        saving.delete()
