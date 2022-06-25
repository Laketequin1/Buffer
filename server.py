from src import lakeserver # Import personal server
import time


main_server = lakeserver.Server(5050, direct=True, header=2048)

main_server.start()

while True:
    main_server.direct_send_all(main_server.get_client_data())
    time.sleep(0.01)