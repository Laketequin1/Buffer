from src import lakeserver # Import personal server\

main_server = lakeserver.Server(5050)

main_server.start()

input("Press enter to close...")

