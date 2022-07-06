import pandas as pd
file_dir = '/home/himel/Documents/Adorsho_pranisheba/Kashfia/Himel/S1006_16_12_2021_6AM_16_12_2021_3PM.xlsx'
df = pd.read_excel(file_dir)
df.dropna(inplace=True)
df[['rumination', 'eating', 'standing']] = df[['rumination', 'eating', 'standing']].astype(int)
print('Wrong annotation: ',(df['rumination'] & df['eating']).sum())