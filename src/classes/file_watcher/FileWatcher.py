import hashlib
import os
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class FileWatcher:
    def __init__(self, directory_to_watch, callback, md5_check=True):
        self.DIRECTORY_TO_WATCH = directory_to_watch
        self.callback = callback
        self.md5_check = md5_check
        self.md5_hash_table = {}
        self.observer = Observer()

    def list_files(self):
        print(f"Listing all files in {self.DIRECTORY_TO_WATCH}:")
        for root, dirs, files in os.walk(self.DIRECTORY_TO_WATCH):
            for file in files:
                print(os.path.join(root, file))

    def run(self):
        self.list_files()
        event_handler = Handler(self.callback, self.md5_check, self.md5_hash_table)
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        print(f"\n\n**Watching for file changes on {self.DIRECTORY_TO_WATCH}**\n\n")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()


class Handler(FileSystemEventHandler):
    def __init__(self, callback, md5_check, md5_hash_table):
        self.callback = callback
        self.md5_check = md5_check
        self.md5_hash_table = md5_hash_table

    def on_created(self, event):
        if event.is_directory:
            return None

        filename = os.path.basename(event.src_path)
        print(f"File created: {filename}")
        self.process_event(event.src_path, filename)

    def on_modified(self, event):
        if event.is_directory:
            return None

        filename = os.path.basename(event.src_path)
        print(f"File modified: {filename}")
        self.process_event(event.src_path, filename)

    def on_deleted(self, event):
        if event.is_directory:
            return None

        filename = os.path.basename(event.src_path)
        print(f"File deleted: {filename}")
        if filename in self.md5_hash_table:
            del self.md5_hash_table[filename]

    def process_event(self, src_path, filename):
        try:
            with open(src_path, 'rb') as file:
                new_file_contents = file.read()

            if self.md5_check:
                md5_current = hashlib.md5(new_file_contents).hexdigest()
                if md5_current == self.md5_hash_table.get(filename):
                    return
                self.md5_hash_table[filename] = md5_current
                print(f"{filename} file Changed")
                print("MD5 table", self.md5_hash_table)

            self.callback(filename, new_file_contents.decode('utf-8'))
        except Exception as e:
            print(e)


def process_file(filename, content):
    print(f"Processing {filename} with content: {content}")


if __name__ == "__main__":
    watch_dir = "/Users/<user>/Documents/Bot"
    watcher = FileWatcher(watch_dir, process_file)
    watcher.run()
