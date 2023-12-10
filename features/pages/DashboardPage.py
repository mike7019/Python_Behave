import hamcrest


class DashboardPage:

    def __init__(self, driver):
        self.driver = driver

    lbl_dashboard = "//h2[contains(text(),'Dashboard')]"

    def validate_the_title(self):
        return self.lbl_dashboard.__contains__("Dashboard")