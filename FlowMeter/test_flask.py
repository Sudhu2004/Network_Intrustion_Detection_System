from flask import Flask, request, jsonify
import os
import subprocess

app = Flask(__name__)

@app.route('/process_pcap', methods=['POST'])
def process_pcap():
    # Check if file is present in the request
    if 'pcap_file' not in request.files:
        return jsonify({'error': 'No file part'})

    pcap_file = request.files['pcap_file']

    # Check if file is uploaded
    if pcap_file.filename == '':
        return jsonify({'error': 'No selected file'})

    # Save the file to a temporary directory
    tmp_dir = '/tmp'
    pcap_path = os.path.join(tmp_dir, pcap_file.filename)
    pcap_file.save(pcap_path)

    # Check if output directory is provided
    if 'output_dir' not in request.form:
        return jsonify({'error': 'Output directory not provided'})

    output_dir = request.form['output_dir']

    # Run the cicflowmeter command to process the pcap file
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'another_output.csv')

    # Command to run cicflowmeter
    command = f"cicflowmeter -f {pcap_path} -c {output_file}"

    # Run the command
    result = subprocess.run(command, shell=True)
    print(result)
    # Check if output file is created
    if os.path.exists(output_file):
        return jsonify({'output_dir': output_dir})
    else:
        return jsonify({'error': 'Error creating output file'})

if __name__ == '__main__':
    app.run(debug=True)
