# -*- coding: utf-8 -*-
from .Handler import Handler
from .models import Applications, Stories


class Tasks:

    @staticmethod
    def process_story(app_id, story_name, *, story_id=None):
        Handler.init_db()
        app = Applications.get(Applications.id == app_id)
        story = app.get_story(story_name)
        story.data(app.initial_data)
        Handler.build_story(app.user.installation_id, story)

        line_number = '1'
        context = {'application': app, 'story': story_name}
        while line_number:
            line_number = Handler.run(line_number, story, context)