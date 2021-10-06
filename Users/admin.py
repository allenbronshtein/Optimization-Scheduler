import gui
class Admin:
    def __init__(self,appData):
        self.appData = appData
        gui.print_title("Hello Admin!")
    
    def run(self):
        run = True
        while run:
            gui.admin_page(self.appData)
            command = self.appData.buffer
            if command == '1': 
                self.appData.db_controller.auto_insert(self.appData)
                gui.print_body("DataBase Ready")
            if command == '2': 
                self.appData.db_controller.clear()
                gui.print_body("DataBase Cleared")
            if command == '3': run = False