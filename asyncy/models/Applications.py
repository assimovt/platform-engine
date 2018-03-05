# -*- coding: utf-8 -*-
from peewee import CharField, ForeignKeyField

from playhouse.postgres_ext import HStoreField

from .Base import BaseModel
from .Stories import Stories
from .Users import Users


class Applications(BaseModel):

    name = CharField()
    user = ForeignKeyField(Users)
    initial_data = HStoreField(null=True)

    def get_story(self, story_name):
        appstory = self.stories.join(Stories)\
                               .where(Stories.filename == story_name).get()
        return appstory.story

    def environment(self, scope):
        """
        Gets the environment from the initial data
        """
        environment = {}
        if self.initial_data:
            if 'environment' in self.initial_data:
                initial_environment = self.initial_data['environment']
                if scope in initial_environment:
                    environment[scope] = initial_environment[scope]
        return environment

    def installation_id(self):
        return self.user.installation_id
