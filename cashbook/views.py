# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.response import Response
from rest_framework.decorators import api_view

import neoutils

from . import step
from .responses import ACTIONS
from savings.handlers import AgentHandler, ParentHandler

from session.handlers import SessionHandler

STEP_FUNCTIONS = {
    '1': step.one,
    '2': step.two,
    '3': step.three,
}

WELCOME = 'Welcome to EduPay\n\n'
INIT_MENU = {
    'agent':  WELCOME + "1. Collect Contribution\n2. Check Collection Summary",
    'parent': WELCOME + "1. Check Savings Summary"
}

@api_view(['POST'])
def index(request):
    # {u'Sequence': 1, u'Mobile': u'233542751610',
    # u'SessionId': u'7ea9dd78239549688a10cecd9837e6ed',
    # u'ServiceCode': u'711*79', u'Operator': u'mtn',
    # u'Message': u'*711*79#', u'ClientState': None, u'Type': u'Initiation'}
    data = request.data
    phone_number = '0' + data['Mobile'][3:]

    # Get agent/parent
    agent = AgentHandler.get(phone_number)
    if not agent:
        parent = ParentHandler.get(phone_number)
        if not parent:
            return Response(neoutils.NeoAction.release('You are unauthorized to use this service.'))
    else:
        first_name = agent.first_name
        last_name = agent.last_name
        data.update({'is_agent': True, 'first_name': first_name, 'last_name': last_name})

    r = {}
    initiator, is_agent, session_args = neoutils.build_session_args(data, 'parent')

    session_id = data['SessionId']
    session = SessionHandler(session_id)
    session.get_or_create(**session_args)

    # Set initiation message (code dialled - e.g. *711*78# or *711*78*1#) at first sequence
    seq = request.data.get('Sequence', None)
    message = request.data.get('Message', None)
    if int(seq) == 1:
        session.set_init_message(message)

    response_type = request.data.get('Type', None)
    if response_type == 'Initiation':
        r = neoutils.perform_init_action(
            ACTIONS, STEP_FUNCTIONS, session, seq, message, initiator, first_name, is_agent, menu=INIT_MENU)
    else:
        step = neoutils.get_step(session, int(seq))
        r = neoutils.perform_action(ACTIONS, STEP_FUNCTIONS, step, session, message, initiator)

    return Response(r)
