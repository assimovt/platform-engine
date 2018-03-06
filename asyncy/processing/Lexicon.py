# -*- coding: utf-8 -*-
from ..Containers import Containers


class Lexicon:
    """
    Lexicon of possible line actions and their implementation
    """

    @staticmethod
    def run(logger, story, line, environment):
        """
        Runs a container with the resolution values as commands
        """
        command = story.resolve(logger, line['ln'])
        container = Containers(line['container'], logger)
        container.make_volume(story.filename)
        container.run(command, environment)
        story.end_line(line['ln'], container.result())

    @staticmethod
    def if_condition(logger, story, line):
        """
        Evaluates the resolution value to decide wheter to enter
        inside an if-block.
        """
        result = story.resolve(logger, line['ln'])
        if result[0]:
            return line['enter']
        return line['exit']

    @staticmethod
    def unless_condition(logger, story, line):
        result = story.resolve(logger, line['ln'])
        if result[0]:
            return line['exit']
        return line['enter']

    @staticmethod
    def next(logger, story, line):
        result = story.resolve(logger, line['ln'])
        if result.endswith('.story'):
            return result
        return '{}.story'.format(result)
