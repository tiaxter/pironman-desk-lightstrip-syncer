import tinytuya, os, re, time
from dotenv import load_dotenv

load_dotenv()

def setup_device():
    device = tinytuya.BulbDevice(
        os.getenv("DEVICE_ID"),
        "Auto",
        os.getenv("LOCAL_KEY"),
    )
    # setup configuration for connect to rgb led strip
    device.set_version(3.3)
    device.set_socketPersistent(True)  
    device.set_dpsUsed({"20": None})
    # return device
    return device

# Main function here
if __name__ == "__main__":
    device = setup_device()

    last_state = False

    while True:
        try:
            is_on = device.state()['is_on']

            # If state is different from the latest then
            if is_on != last_state:
                os.system(f"pironman -rw {'on' if is_on else 'off'}")

            last_state = is_on
            # 100 milliseconds of sleep
            time.sleep(0.100)
        except:
            device = setup_device()
