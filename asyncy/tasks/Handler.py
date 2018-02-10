# -*- coding: utf-8 -*-
from ..Containers import Containers
from ..Lexicon import Lexicon
from ..models import Mongo, db


class Handler:
    """
    Handles various task-related things.
    """

    @staticmethod
    def init_db(database_url):
        db.from_url(database_url)

    @staticmethod
    def init_mongo(mongo_url):
        return Mongo(mongo_url)

    @staticmethod
    def build_story(app_identifier, pem_path, installation_id, story):
        """
        Build a storytree, given a story
        """
        story.backend(app_identifier, pem_path, installation_id)
        story.build_tree()

    @staticmethod
    def make_environment(story, application):
        """
        Makes the environment from story and application.
        """
        environment = story.environment()
        application_environment = application.environment()
        for key, value in environment.items():
            if key in application_environment:
                environment[key] = application_environment[key]
        return environment

    @staticmethod
    def run(logger, line_number, story, context):
        """
        Run the story
        """
        line = story.line(line_number)
        command = story.resolve(logger, line_number)

        if line['method'] == 'if':
            return Lexicon.if_condition(line, command)

        container = Containers(line['container'])
        container.make_volume(story.filename)
        container.run(logger, command, context['environment'])
        context['results'][line_number] = {'output': container.result(),
                                           'start': 0, 'end': 0}