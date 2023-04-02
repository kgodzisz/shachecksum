import os
import hashlib
import sys

# Enter the path to the file in the script.
file = sys.argv[1]

# Open the file in binary mode and calculate the SHA256 checksum.
with open(file, "rb") as f:
    file_data = f.read()
    sha256_hash = hashlib.sha256(file_data).hexdigest()

# Accept the checksum as an argument during the script invocation.
if len(sys.argv) < 2:
    print("Provide the SHA256 checksum as an argument.")
    sys.exit(1)

expected_hash = sys.argv[2]

# Compare the checksums.
if sha256_hash == expected_hash:
    print("The checksum is correct.")
else:
    print("The checksum is incorrect.")