from abc import ABC, abstractmethod

# Step 1: Create the Implementation Interface (Device)
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Step 2: Implement Concrete Devices
class TV(Device):
    def turn_on(self):
        return "TV is now ON"

    def turn_off(self):
        return "TV is now OFF"

class Radio(Device):
    def turn_on(self):
        return "Radio is now ON"

    def turn_off(self):
        return "Radio is now OFF"

# Step 3: Create the Abstraction (Remote Control)
class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def power_on(self):
        return self.device.turn_on()

    def power_off(self):
        return self.device.turn_off()

# Step 4: Extend Abstraction with Advanced Features
class AdvancedRemote(RemoteControl):
    def mute(self):
        return "Device is now Muted"

# Step 5: Client Code
if __name__ == "__main__":
    # Using basic remote with TV
    tv = TV()
    remote = RemoteControl(tv)
    print(remote.power_on())  # TV is now ON
    print(remote.power_off()) # TV is now OFF

    # Using advanced remote with Radio
    radio = Radio()
    adv_remote = AdvancedRemote(radio)
    print(adv_remote.power_on())  # Radio is now ON
    print(adv_remote.mute())      # Device is now Muted
    print(adv_remote.power_off()) # Radio is now OFF
