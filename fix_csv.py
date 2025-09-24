import pandas as pd

file_path = 'XAUUSDc_M1_202506111341_202509220003.csv'
df = pd.read_csv(file_path, sep='\t')

out_path = 'XAUUSDx_M1.csv'
df.to_csv(out_path, index=False)
out_path