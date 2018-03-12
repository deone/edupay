from responses import STEPS

# Step functions
def one(instance, initiator, option):
    method = STEPS['one'][initiator][option]
    return getattr(instance, method)()

def two(instance, initiator, option):
    method = STEPS['two'][initiator][option]
    return getattr(instance, method)()

def three(instance, initiator, option):
    method = STEPS['three'][initiator][option]
    return getattr(instance, method)()