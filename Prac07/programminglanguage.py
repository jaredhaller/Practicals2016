"""
Intermediate Exercise
"""


class ProgrammingLanguage:

    def __init__(self, language, typing, reflection, year):
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return True if self.typing is 'Dynamic' else False

    def __str__(self):
        # return "{}, {} Typing, Reflection={}, First appear in {}"\
        #     .format(self.language, self.typing, self.is_dynamic(), self.year)
        return "{}".format(self.language)
