import wifimgr
import blink_ip


wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  # you shall not pass :D


# Main Code goes here, wlan is a working network.WLAN(STA_IF) instance.
ip = wlan.ifconfig()[0]
print("ESP OK. IP Address: ", ip)
blink_ip.blink_ip(ip)

