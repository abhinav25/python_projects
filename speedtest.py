# pip install speedtest-cli
import speedtest

s = speedtest.Speedtest()

# Bytes for conversion
bytes_num = 1000000

# Get download Speed
dws = round(s.download()/bytes_num, 2)

# Get upload Speed
ups = round(s.upload()/bytes_num, 2)

# print internet speed
print(f'My download speed is: {dws} Mbps')
print(f'My Upload speed is: {ups} Mbps')
