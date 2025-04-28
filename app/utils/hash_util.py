import os
import hashlib

def compute_directory_hash(directory: str) -> str:
    """Compute a hash of the directory's contents (file names, sizes, and modification times)."""
    hash_obj = hashlib.sha256()
    for root, _, files in os.walk(directory):
        for file in sorted(files):  # Sort to ensure consistent order
            file_path = os.path.join(root, file)
            try:
                # Include file name, size, and modification time in the hash
                stat = os.stat(file_path)
                hash_obj.update(file.encode())
                hash_obj.update(str(stat.st_size).encode())
                hash_obj.update(str(stat.st_mtime).encode())
            except FileNotFoundError:
                # Skip files that are deleted during the hashing process
                continue
    return hash_obj.hexdigest()

def load_stored_hash(hash_file: str) -> str:
    """Load the stored hash from a file."""
    if os.path.exists(hash_file):
        with open(hash_file, "r") as f:
            return f.read().strip()
    return ""

def save_hash(hash_file: str, directory_hash: str):
    """Save the computed hash to a file."""
    with open(hash_file, "w") as f:
        f.write(directory_hash)