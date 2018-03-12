# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from session.handlers import SessionHandler

from cashbook.actions import Action
from savings.handlers import AgentHandler, ParentHandler

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
            return Response(Action.release('You are unauthorized to use this service.'))

    """ session = SessionHandler(request.data['SessionId'])
    session.get_or_create(
        phone_number='0' + request.data['Mobile'][3:],
        service_code=request.data['ServiceCode'],
        operator=request.data['Operator']
    )

    # Create session
    session_id = data['SessionId']
    session = SessionHandler(session_id)

    session_args = {
        'phone_number': data['Mobile'],
        'service_code': data['ServiceCode'],
        'operator': data['Operator']
    }

    session.get_or_create(**session_args) """