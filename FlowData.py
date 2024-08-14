import requests
import subprocess
import time

class PcapProcessor:
    def __init__(self, flask_script_path):
        self.flask_script_path = flask_script_path

    def process_pcap_file(self, file_path, output_dir, flask_url):
        with open(file_path, 'rb') as file:
            files = {'pcap_file': file}
            data = {'output_dir': output_dir}

            response = requests.post(flask_url, files=files, data=data)

            if response.status_code == 200:
                data = response.json()
                if 'output_dir' in data:
                    return data['output_dir']
                elif 'error' in data:
                    return f"Error: {data['error']}"
                else:
                    return "Unknown error occurred"
            else:
                return "Error: Failed to process pcap file"

    def initialize_flask(self):
        try:
            flask_command = ["wsl", "python3", self.flask_script_path]
            subprocess.run(flask_command, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error running Flask application: {e}")

    def process_pcap_after_flask_initializes(self, pcap_file_path, output_directory, flask_url, wait_time=5):
        time.sleep(wait_time)

        result = self.process_pcap_file(pcap_file_path, output_directory, flask_url)
        print(result)