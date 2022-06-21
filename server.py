from src import lakeserver # Import personal server

def update_data(self):
    self.set_data(self.get_client_data())

main_server = lakeserver.Server(5050, pre_send_func=update_data)

main_server.start()

while True:
    pass
    