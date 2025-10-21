#!/usr/bin/env python3
import socket
import time

# Daftar domain yang akan dicek
domains = [
    "www.google.com",
    "www.cisco.com",
    "www.netacad.com",
    "www.wikipedia.org",
    "www.detik.com",
    "www.youtube.com",
    "www.reddit.com"
]

print("\n=== DNS Lookup Monitor ===\n")

for domain in domains:
    print(f"Checking: {domain}")
    start_time = time.time()
    try:
        ip = socket.gethostbyname(domain)
        end_time = time.time()
        response_time = (end_time - start_time) * 1000  # dalam ms

        print(f"Resolved IP: {ip}")
        print(f"Response Time: {response_time:.2f} ms")

        # Menilai status koneksi
        if response_time < 50:
            status = "Excellent ✅"
        elif response_time < 100:
            status = "Good 👍"
        elif response_time < 200:
            status = "Fair ⚠️"
        else:
            status = "Slow ❌"

        print(f"DNS Resolution Status: {status}\n")

    except socket.gaierror:
        print("Failed to resolve domain ❌\n")
    time.sleep(1)

print("=== DNS Lookup Completed ===\n")
