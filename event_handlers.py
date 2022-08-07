import datetime
from enum import Enum

from dateutil import parser


class EventTypes(Enum):
    PUSH = 'push'
    TEAM = 'team'
    REPOSITORY = 'repository'


class ActionTypes(Enum):
    CREATED = 'created'
    DELETED = 'deleted'
# Base class


class BaseEventHandler(object):
    def __init__(self, event_type=None):
        self.event_type = event_type

    async def run(self, event: dict):
        raise NotImplementedError('subclasses must override run()!')

    async def notify(self, event: dict):
        print(event)


class PushBetweenTwoToFour(BaseEventHandler):

    def __init__(self):
        super(PushBetweenTwoToFour, self).__init__(EventTypes.PUSH.value)

    async def run(self, event: dict):
        now = datetime.datetime.now()
        current_hour = now.hour
        # utc time?
        if current_hour > 14 and current_hour < 16:
            await self.notify(event)

    async def notify(self, event: dict):
        username = event['pusher']['name']
        print(f'User {username} pushed between 14 to 16')
        await super().notify(event)


class NewTeamStartsWithHackerEventHandler(BaseEventHandler):

    def __init__(self):
        super(NewTeamStartsWithHackerEventHandler, self).__init__(EventTypes.TEAM.value)

    async def run(self, event: dict):
        action_name = event['action']
        if action_name == ActionTypes.CREATED.value:
            team_name = event['team']['name']
            if team_name.startswith('hacker'):
                await self.notify(event)

    async def notify(self, event: dict):
        team_name = event['team']['name']
        print(f'Team {team_name} has hacker prefix')
        await super().notify(event)


class RepositoryDeletedLessThenTenMinutesBeforeCreationEventHandler(BaseEventHandler):

    def __init__(self):
        super(RepositoryDeletedLessThenTenMinutesBeforeCreationEventHandler, self).__init__(EventTypes.REPOSITORY.value)

    async def run(self, event: dict):
        action_name = event['action']
        if action_name == ActionTypes.DELETED.value:
            creation_date = parser.parse(event['repository']['created_at'])
            deletion_date = parser.parse(event['repository']['updated_at'])
            delta = deletion_date - creation_date
            minutes = delta.total_seconds() / 60
            if minutes <= 10:
                await self.notify(event)

    async def notify(self, event: dict):
        repository_name = event['repository']['name']
        print(f'Repository {repository_name} was deleted in less than 10 minutes.')
        await super().notify(event)
