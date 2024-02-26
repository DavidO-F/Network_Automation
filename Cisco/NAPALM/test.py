from napalm import get_network_driver
import json
import napalm


def main():
    driver_ios = napalm.get_network_driver("ios")
    print(driver_ios)
    ios_router = driver_ios (hostname = "192.168.193.141", username = "admin", password = "admin")
    print(ios_router)
    print("Connecting to IOS Router...") 
    ios_router.open()
    # print("Checking IOS Router Connection Status:") 
    # print(ios_router.is_alive())
    # ios_router.close() 
    print("Test Completed")

if __name__ == "__main__": main()