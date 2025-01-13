class Actor:
    def __init__(self, name, driver):
        self.name = name
        self.driver = driver
        self.abilities = {}

    def attempts_to(self, task):
        task.perform_as(self)

    def can_see(self, question):
        return question.answer_as(self)