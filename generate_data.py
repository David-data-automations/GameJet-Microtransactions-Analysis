import pandas as pd
import numpy as np
from datetime import date, timedelta
import os

# --- 1. SETUP ---
if not os.path.exists('datasets'):
    os.makedirs('datasets')

N_USERS = 22576 # Based on Task 1a
start_date = date(2023, 1, 1)
N_DAYS = 90
udids = [f'U{i:05d}' for i in range(1, N_USERS + 1)]

# --- 2. GENERATE USERS TABLE ---
install_dates = [start_date + timedelta(days=np.random.randint(0, N_DAYS)) for _ in range(N_USERS)]
languages = np.random.choice(['en', 'es', 'fr', 'de'], N_USERS, p=[0.70, 0.15, 0.10, 0.05])
countries = np.random.choice(['US', 'CA', 'MX', 'BR', 'DE', 'FR'], N_USERS, p=[0.50, 0.10, 0.10, 0.10, 0.10, 0.10])

df_users = pd.DataFrame({
    'udid': udids,
    'install_date': install_dates,
    'lang': languages,
    'country': countries
})
df_users.to_csv('datasets/users.csv', index=False)

# --- 3. GENERATE SESSIONS TABLE ---
# Users who opened the app: Total users (22576) - Non-users (32) = 22544
active_udids = udids[:22544]
N_SESSIONS = int(N_USERS * 32.1) # Total sessions based on the average
session_udids = np.random.choice(active_udids, N_SESSIONS, p=np.power(np.arange(len(active_udids)) + 1, -1.5)) # Skewed sessions (Pareto)
session_udids = np.random.choice(active_udids, N_SESSIONS) # Simpler, less resource intensive skew

df_sessions = []
for udid in active_udids:
    install_date = df_users.loc[df_users['udid'] == udid, 'install_date'].iloc[0]
    num_sessions = np.random.lognormal(mean=1.5, sigma=1.0) # Skewed distribution
    num_sessions = int(np.clip(num_sessions, 1, 1939)) # Limit to max sessions observed
    
    start_times = [datetime.combine(install_date, datetime.min.time()) + timedelta(minutes=np.random.randint(0, N_DAYS*24*60)) for _ in range(num_sessions)]
    start_times.sort()
    
    # Simulate session number for each user
    session_data = pd.DataFrame({
        'udid': udid,
        'ts': start_times,
        'session_num': np.arange(1, num_sessions + 1)
    })
    df_sessions.append(session_data)

df_sessions = pd.concat(df_sessions, ignore_index=True)
df_sessions['date'] = df_sessions['ts'].dt.date
df_sessions.to_csv('datasets/sessions.csv', index=False)

# --- 4. GENERATE IAPS TABLE (In-App Purchases) ---
# Goal: ~20% paying users. Ensure Whales/Dolphins exist.
PAYING_USERS = int(N_USERS * 0.20)
paying_udids = np.random.choice(udids, PAYING_USERS, replace=False)

iaps_list = []
for udid in paying_udids:
    install_date = df_users.loc[df_users['udid'] == udid, 'install_date'].iloc[0]
    
    # Determine the persona to simulate spending behavior
    # Ensure a few whales (top 1% of payers) and dolphins (next 10%)
    if np.random.rand() < 0.05: # 5% chance of being a whale
        spend_tier = 'whale'
    elif np.random.rand() < 0.20: # 15% chance of being a dolphin
        spend_tier = 'dolphin'
    else:
        spend_tier = 'minnow'
        
    if spend_tier == 'whale':
        num_purchases = np.random.randint(15, 50)
        revenue_cents = np.random.randint(10000, 50000, num_purchases)
    elif spend_tier == 'dolphin':
        num_purchases = np.random.randint(5, 15)
        revenue_cents = np.random.randint(2000, 10000, num_purchases)
    else: # minnow
        num_purchases = np.random.randint(1, 5)
        revenue_cents = np.random.randint(1, 2000, num_purchases)

    # Ensure Day 0 purchases are common (as per analysis)
    purchase_dates = [install_date + timedelta(days=np.random.randint(0, 30)) for _ in range(num_purchases)]
    
    iaps_data = pd.DataFrame({
        'udid': udid,
        'ts': [datetime.combine(d, datetime.min.time()) + timedelta(seconds=np.random.randint(0, 86400)) for d in purchase_dates],
        'date': purchase_dates,
        'prod_type': np.random.choice(['gems', 'passes', 'value_pack'], num_purchases),
        'prod_qty': np.random.randint(1, 5, num_purchases),
        'rev': revenue_cents
    })
    iaps_list.append(iaps_data)

df_iaps = pd.concat(iaps_list, ignore_index=True)
df_iaps.to_csv('datasets/iaps.csv', index=False)

print("Generated three inter-related dummy data files (users.csv, sessions.csv, iaps.csv) successfully in the 'datasets/' folder.")
