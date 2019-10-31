import os
import shutil
import sys
import threading

import time

from unipacker.core import UnpackerEngine, SimpleClient
from unipacker.unpackers import get_unpacker
from unipacker.utils import RepeatedTimer

class IOHandler(object):

    def __init__(self, samples, dest_dir, partition_by_packer):
        os.makedirs(dest_dir, exist_ok=True)
        for sample in samples:
            print(f"Next up: {sample}")

            try:
                self.handle_sample(sample, dest_dir, partition_by_packer)
            except Exception as e:
                print('Exception: {0}\n'.format(str(e)))

    def handle_sample(self, sample, dest_dir, partition_by_packer):
        unpacker, _ = get_unpacker(sample)

        engine = None
        hearbeat = None

        try:
            event = threading.Event()
            client = SimpleClient(event)
            heartbeat = RepeatedTimer(120, print, "- still running -", file=sys.stderr)

            print('Initializing engine: {0}'.format(time.time()))
            engine = UnpackerEngine(sample)
            engine.register_client(client)
            heartbeat.start()
            print('Starting engine: {0}'.format(time.time()))
            # Start thread & timeout (seconds)
            threading.Thread(target=engine.emu, args=(10,)).start()

            event.wait()

        finally:
            print('Finished: {0}'.format(time.time()))
            if heartbeat is not None:
                heartbeat.stop()
            if engine is not None:
                engine.stop()

        if partition_by_packer:
            dest_dir = os.path.join(dest_dir, sample.unpacker.name)
            os.makedirs(dest_dir, exist_ok=True)
        dest_file = os.path.join(dest_dir, f"unpacked_{os.path.basename(sample.path)}")
        print(f"\nEmulation of {os.path.basename(sample.path)} finished.\n"
              f"--- Saving to {dest_file} ---\n")
        shutil.move("unpacked.exe", dest_file)
