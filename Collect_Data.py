import pyshark
import time

class PcapProcessorThreaded:
    def __init__(self, ):
        pass

    def process_live_capture(self, interface, output_file, timeout):
        start_time = time.time()
        capture = pyshark.LiveCapture(interface=interface, output_file=output_file)
        capture.set_debug()
        capture.sniff(timeout=timeout)
        end_time = time.time()
        running_time = end_time - start_time
        print("Data Collection timeout:", running_time, "seconds")
        capture.close()

