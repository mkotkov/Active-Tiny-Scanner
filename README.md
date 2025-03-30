
# Active-Tiny-Scanner

This is a simple port scanner that allows you to check whether a port is open on a given host for TCP or UDP connections.

## Description

This tool allows you to scan ports on a target host using TCP or UDP protocols to check if the port is open.

## Installation

To run **TinyScanner**, make sure you have Python installed (version 3.x and above).

1. Clone the repository or download the source code:
    ```bash
    git clone https://01.kood.tech/git/mkotkov/active.git
    cd active
    ```

2. Make sure you have Python installed along with the necessary dependencies:
    ```bash
    python --version
    ```

## Usage

Run the program with various options to scan ports on a host.

### General Syntax

```bash
tinyscanner.py [OPTIONS] [HOST] [PORT]
```

### Options:

- `-p RANGE` — range of ports to scan (e.g., `80`, `80-90`).
- `-u` — scan using UDP.
- `-t` — scan using TCP.
- `--help` — show help message and exit.

### Example Usage:

1. Scan port 80 on the local host using UDP:

    ```bash
    python tinyscanner.py -u 127.0.0.1 -p 80
    ```

2. Scan ports 80-83 on a remote host using TCP:

    ```bash
    python tinyscanner.py -t 10.53.224.5 -p 80-83
    ```

3. Get help about the program:

    ```bash
    python tinyscanner.py --help
    ```

    **Output:**
    ```bash
    Usage: tinyscanner [OPTIONS] [HOST] [PORT]
    Options:
      -p RANGE     Range of ports to scan
      -u           UDP scan
      -t           TCP scan
      --help       Show this message and exit.
    ```

## How it works

- **Scanner** uses sockets to establish connections to the specified host and port. For TCP, it checks if the connection can be established, and for UDP, it sends packets and checks for a response.
- The program is written in Python and can be used to scan both local and remote hosts.

## Important Note

- TCP and UDP ports may operate independently of each other, so the presence of an open TCP port does not mean the corresponding UDP port is open, and vice versa.
- Make sure your firewall and antivirus software are not blocking traffic during the scan.


## License

MIT License

Copyright (c) [2024] [Maksym Kotkov]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
