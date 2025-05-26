import socket
import sys


target = input("Enter the target IP or domain name (e.g., 127.0.0.1 or google.com): ").strip()

# ✅ Step 2: Get port range from user
try:
    start_port = int(input("Enter the starting port (e.g., 20): "))
    end_port = int(input("Enter the ending port (e.g., 80): "))

    if start_port < 0 or end_port > 65535 or start_port > end_port:
        print("❌ Invalid port range. Ports must be between 0 and 65535.")
        sys.exit()

except ValueError:
    print("❌ Please enter valid integer values for ports.")
    sys.exit()

print(f"\n📡 Scanning {target} from port {start_port} to {end_port}...\n")

# ⚙️ Step 3: Scan ports
for port in range(start_port, end_port + 1):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # 1 second timeout

        result = sock.connect_ex((target, port))  # Returns 0 if connection successful

        if result == 0:
            print(f"✅ Port {port} is OPEN")
        else:
            print(f"❌ Port {port} is CLOSED")

        sock.close()

    except socket.gaierror:
        print("❌ Hostname could not be resolved.")
        break
    except socket.error:
        print("❌ Couldn't connect to server.")
        break
    except KeyboardInterrupt:
        print("\n⛔ Scan cancelled by user.")
        break

print("\n✅ Scan complete.")