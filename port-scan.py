import socket

def scan_ports(website, start_port, end_port):
    try:
        ip = socket.gethostbyname(website)  # Resolve domain to IP
        print(f"Scanning {website} ({ip}) for open ports...")
        open_ports = []

        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)  # Set timeout for connection attempts
            result = sock.connect_ex((ip, port))  # Connect to the port
            if result == 0:  # Port is open
                open_ports.append(port)
            sock.close()

        if open_ports:
            print(f"Open ports on {website} ({ip}): {open_ports}")
        else:
            print(f"No open ports found on {website} ({ip}) in the range {start_port}-{end_port}.")
        return open_ports

    except socket.gaierror:
        print(f"Error: Unable to resolve domain name {website}.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    target_website = input("Enter the website URL (e.g., example.com): ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))
    
    scan_ports(target_website, start_port, end_port)
