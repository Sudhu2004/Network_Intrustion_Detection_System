import numpy as np
from Collect_Data import PcapProcessorThreaded

class StoreData:
    def __init__(self):
        pass

    def get_flow_data(self, interface="Wi-Fi", output_file='data/another_data.pcap', timeout=20):
        # Path to the Flask script
        
    
        # Print the interface name to debug
        print(f"Using interface: {interface}")

        # Create an instance of PcapProcessorThreaded
        processor_threaded = PcapProcessorThreaded()
        
        # Process live capture
        try:
            processor_threaded.process_live_capture(interface, output_file, timeout)
        except Exception as e:
            print(f"An error occurred during live capture: {e}")

# Instantiate and call the method
dataCollection = StoreData()
dataCollection.get_flow_data()
