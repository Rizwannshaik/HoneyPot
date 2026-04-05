fake_files = {
    "/home/admin/notes.txt": "TODO: change root password",
    "/etc/passwd": "root:x:0:0:root:/root:/bin/bash",
    "/var/log/auth.log": "Failed password attempts...",
    "/home/admin/bank_details.txt": "Account: 1234567890\nIFSC: FAKE0001234",
}

def read_file(path):
    return fake_files.get(path, "cat: No such file or directory")

def list_files():
    return "\n".join(fake_files.keys())