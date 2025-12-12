import pandas as pd

# Create small toy dataset for testing
data = {
    "URL_Length": [54, 120, 33, 88, 70, 95, 60, 110, 45, 130],
    "HTTPS": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],   # 1=Uses HTTPS, 0=No HTTPS
    "Has_IP": [0, 1, 0, 1, 0, 1, 0, 0, 1, 1], # 1=URL contains IP
    "Short_URL": [0, 1, 0, 0, 1, 1, 0, 0, 1, 1], # 1=Shortened link
    "Result": [1, -1, -1, 1, -1, 1, -1, 1, -1, 1]  # 1=Phishing, -1=Legit
}

df = pd.DataFrame(data)

# Save as phishing.csv
df.to_csv("phishing.csv", index=False)

print("Sample phishing.csv created successfully!")
