import pandas as pd 


class ModelInference:
    def __init__(self):
        self.mean_values = [28001680.746361718, 2589911.620407374, 105062.08643302266, 95453.04858439442, 4052.5439399847287, 555.0930456487124, 16996.44408209579, 242.05800321349844, 249.2459712171017, 6.121278527738439, 27744764.05700856, 13864065.616925292, 0.5569573107089185, 305.664881892096, 5299.6712559350835, 1476.6430779136224, 60.55543966675341, 551.940841400682, 555.0930456487124, 16994.89204897337, 10.214078761027453, 9.556261485802718]
        self.std_values = [42766802.197003104, 51569479.4391863, 346339.2341140198, 319860.71082673426, 30919.27480160786, 6163.663069565681, 2241175.2369952328, 15642.771061536021, 19689.57222078891, 715.1550680383307, 42770936.49124741, 33352930.905204732, 0.5707335566717643, 398.04593861997984, 11869.737393666344, 7315.272620919325, 157.64379415396905, 797.4495636051091, 6163.663069565681, 2240952.8014762662, 984.2046326239517, 747.197814201113]
        self.column_mapping = {
            'src_ip': ' Destination Port',
            'dst_ip': ' Destination Port',  # Adjust this according to your mapping
            'src_port': ' Source Port',  # Adjust this according to your mapping
            'dst_port': ' Destination Port',
            'protocol': ' Protocol',  # Adjust this according to your mapping
            'timestamp': ' Timestamp',  # Adjust this according to your mapping
            'flow_duration': ' Flow Duration',
            'flow_byts_s': 'Flow Bytes/s',
            'flow_pkts_s': ' Flow Packets/s',
            'fwd_pkts_s': 'Fwd Packets/s',
            'bwd_pkts_s': ' Bwd Packets/s',
            'tot_fwd_pkts': ' Total Fwd Packets',
            'tot_bwd_pkts': ' Total Backward Packets',
            'totlen_fwd_pkts': 'Total Length of Fwd Packets',
            'totlen_bwd_pkts': ' Total Length of Bwd Packets',
            'fwd_pkt_len_max': ' Fwd Packet Length Max',
            'fwd_pkt_len_min': ' Fwd Packet Length Min',
            'fwd_pkt_len_mean': ' Fwd Packet Length Mean',
            'fwd_pkt_len_std': ' Fwd Packet Length Std',
            'bwd_pkt_len_max': 'Bwd Packet Length Max',
            'bwd_pkt_len_min': ' Bwd Packet Length Min',
            'bwd_pkt_len_mean': ' Bwd Packet Length Mean',
            'bwd_pkt_len_std': ' Bwd Packet Length Std',
            'pkt_len_max': ' Max Packet Length',
            'pkt_len_min': ' Min Packet Length',
            'pkt_len_mean': ' Packet Length Mean',
            'pkt_len_std': ' Packet Length Std',
            'pkt_len_var': ' Packet Length Variance',
            'fwd_header_len': ' Fwd Header Length',
            'bwd_header_len': ' Bwd Header Length',
            'fwd_seg_size_min': ' min_seg_size_forward',
            'fwd_act_data_pkts': ' act_data_pkt_fwd',
            'flow_iat_mean': ' Flow IAT Mean',
            'flow_iat_max': ' Flow IAT Max',
            'flow_iat_min': ' Flow IAT Min',
            'flow_iat_std': ' Flow IAT Std',
            'fwd_iat_tot': 'Fwd IAT Total',
            'fwd_iat_max': ' Fwd IAT Max',
            'fwd_iat_min': ' Fwd IAT Min',
            'fwd_iat_mean': ' Fwd IAT Mean',
            'fwd_iat_std': ' Fwd IAT Std',
            'bwd_iat_tot': 'Bwd IAT Total',
            'bwd_iat_max': ' Bwd IAT Max',
            'bwd_iat_min': ' Bwd IAT Min',
            'bwd_iat_mean': ' Bwd IAT Mean',
            'bwd_iat_std': ' Bwd IAT Std',
            'fwd_psh_flags': ' Fwd PSH Flags',
            'bwd_psh_flags': ' Bwd PSH Flags',
            'fwd_urg_flags': ' Fwd URG Flags',
            'bwd_urg_flags': ' Bwd URG Flags',
            'fin_flag_cnt': ' FIN Flag Count',
            'syn_flag_cnt': ' SYN Flag Count',
            'rst_flag_cnt': ' RST Flag Count',
            'psh_flag_cnt': ' PSH Flag Count',
            'ack_flag_cnt': ' ACK Flag Count',
            'urg_flag_cnt': ' URG Flag Count',
            'ece_flag_cnt': ' ECE Flag Count',
            'down_up_ratio': ' Down/Up Ratio',
            'pkt_size_avg': ' Average Packet Size',
            'init_fwd_win_byts': 'Init_Win_bytes_forward',
            'init_bwd_win_byts': ' Init_Win_bytes_backward',
            'active_max': ' Active Max',
            'active_min': ' Active Min',
            'active_mean': ' Active Mean',
            'active_std': ' Active Std',
            'idle_max': ' Idle Max',
            'idle_min': ' Idle Min',
            'idle_mean': ' Idle Mean',
            'idle_std': ' Idle Std',
            'fwd_byts_b_avg': 'Fwd Avg Bytes/Bulk',
            'fwd_pkts_b_avg': ' Fwd Avg Packets/Bulk',
            'bwd_byts_b_avg': ' Bwd Avg Bytes/Bulk',
            'bwd_pkts_b_avg': ' Bwd Avg Packets/Bulk',
            'fwd_blk_rate_avg': ' Fwd Avg Bulk Rate',
            'bwd_blk_rate_avg': 'Bwd Avg Bulk Rate',
            'fwd_seg_size_avg': ' Avg Fwd Segment Size',
            'bwd_seg_size_avg': ' Avg Bwd Segment Size',
            'cwe_flag_count': ' CWE Flag Count',
            'subflow_fwd_pkts': 'Subflow Fwd Packets',
            'subflow_bwd_pkts': ' Subflow Bwd Packets',
            'subflow_fwd_byts': ' Subflow Fwd Bytes',
            'subflow_bwd_byts': ' Subflow Bwd Bytes'
        }
        
    def preprocess_input(self, input_file):
        df = pd.read_csv(input_file)
        df.rename(columns=self.column_mapping, inplace=True)
        req_col=[' Flow Duration','Flow Bytes/s',' Flow Packets/s','Fwd Packets/s', ' Bwd Packets/s','Total Length of Fwd Packets',
                 ' Total Length of Bwd Packets', ' Fwd Header Length',' Bwd Header Length',' act_data_pkt_fwd','Fwd IAT Total','Bwd IAT Total',' Down/Up Ratio',
                 ' Average Packet Size','Init_Win_bytes_forward',' Init_Win_bytes_backward','Fwd Avg Bytes/Bulk',' Bwd Avg Bytes/Bulk',
                 ' Fwd Avg Packets/Bulk',' Bwd Avg Packets/Bulk',' Fwd Avg Bulk Rate','Bwd Avg Bulk Rate', ' Avg Fwd Segment Size',
                 ' Avg Bwd Segment Size', ' Subflow Fwd Bytes', ' Subflow Bwd Bytes',' Subflow Bwd Packets','Subflow Fwd Packets',]
        df = df[req_col]
        df = df.astype(float)
        rem = df.columns[16:22]
        df = df.drop(columns=rem,axis=1)
        return df.values.tolist()