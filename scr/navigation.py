class Navigation:
    def __init__(self, ui):
        self.ui = ui
        self.loading_graph_page = None
        self.result_page = None
        self.task_type = None
        self.result = None
        
    def go_to_auth(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def go_to_page_registr(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def go_to_main(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def go_to_loading_graph(self, task_type):
        self.task_type = task_type
        self.ui.stackedWidget.setCurrentIndex(3)

    def go_to_result(self, result):
        self.result = result
        self.ui.stackedWidget.setCurrentIndex(4)

    def go_to_developer(self):
        self.ui.stackedWidget.setCurrentIndex(5)

    
