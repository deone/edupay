from cashbook.actions import agent

ACTIONS = {
    'agent': {
        1: agent.CollectContribution,
        2: agent.CheckCollectionSummary,
    }
}

STEPS = {
    'one': {
        'agent': {
            1: 'request_phone_number',
        }
    },
    'two': {
        'agent': {
            1: 'request_confirmation',
        }
    },
    'three': {
        'agent': {
            1: 'confirm_contribution_collected',
        }
    }
}