class NavigateTo:
    def __init__(self, url):
        self.url = url

    def perform_as(self, actor):
        actor.driver.get(self.url)