"""Port check tool: tests whether a TCP port is reachable on a host."""

import socket
import sys


def check_port(host, port, timeout):
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.settimeout(timeout)
    result = sock.connect_ex((host, port))
  return result == 0


def main() -> None:
  if len(sys.argv) < 3:
    print("Usage: python main.py <host> <port> [timeout_seconds]")
    sys.exit(1)
  host = sys.argv[1]
  try:
    port = int(sys.argv[2])
  except ValueError:
    print("Error: port must be an integer")
    sys.exit(1)
  timeout = 5.0
  if len(sys.argv) > 3:
    try:
      timeout = float(sys.argv[3])
    except ValueError:
      print("Error: timeout must be a number")
      sys.exit(1)
  if not 1 <= port <= 65535:
    print("Error: port must be between 1 and 65535")
    sys.exit(1)
  if timeout <= 0:
    print("Error: timeout must be positive")
    sys.exit(1)
  try:
    open_port = check_port(host, port, timeout)
  except socket.gaierror:
    print(f"Error: cannot resolve host '{host}'")
    sys.exit(1)
  except OSError as exc:
    print(f"Error: {exc}")
    sys.exit(1)
  if open_port:
    print(f"{host}:{port} is open")
  else:
    print(f"{host}:{port} is closed or filtered")


if __name__ == "__main__":
  main()
