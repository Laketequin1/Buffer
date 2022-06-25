from src import lakeserver # Import personal server

main_server = lakeserver.Server(5050, direct=True)

main_server.start()

while True:
    main_server.set_data(main_server.get_client_data())
    main_server.direct_send_all(main_server.get_data())
    