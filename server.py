from src import lakeserver # Import personal server\

main_server = lakeserver.Server(5050)

main_server.start()

while True:
    main_server.set_data(main_server.get_client_data())
    print(main_server.get_data(), main_server.get_client_data())