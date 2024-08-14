import pyshark
import time

# Record the current time before running the code

# #to get stored pcap files
# capture = pyshark.FileCapture('data\yet_another_file.cap')

# print(capture[0])

#to get live data
file = 'data/yet_another_new_data.pcap'
start_time = time.time()

capture = pyshark.LiveCapture(interface="eth0", output_file=file)
capture.set_debug()

capture.sniff(timeout=10)

# for packet in capture:
#     print("Packet Info: \n")
#     print(packet)

end_time = time.time()
running_time = end_time - start_time
print("Running time:", running_time, "seconds")
capture.close()