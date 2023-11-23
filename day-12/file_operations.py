import psutil
import configparser


def get_current_connections():
    # Get the number of current connections
    connections = psutil.net_connections()
    return len(connections)


def update_sever_config(new_max_connections):
    config = configparser.ConfigParser()
    config.read('server.conf')  # Replace with the actual path to your server.conf file
    print(config['Network_Settings']['MAX_CONNECTIONS'])
    config.set('Network_Settings', 'MAX_CONNECTIONS', str(new_max_connections))

    with open('server.conf', 'w') as configfile:
        config.write(configfile)


def main():
    connections_threshold = 100
    current_connections = get_current_connections()
    print(f"Max Connections: {current_connections}")
    if current_connections >= connections_threshold:
        new_max_connections = current_connections + 200
        update_sever_config(new_max_connections)
        print(f"Updated MAX_CONNECTIONS to : {new_max_connections}")


if __name__ == "__main__":
    main()
