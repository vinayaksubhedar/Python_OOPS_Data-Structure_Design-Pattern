"""
Adapter Patten was used to convert Jason generated through AI tool to XML which was input for our old system.
"""

class FahrenheitThermometer:
    def get_temperature(self):
        """Returns temperature in Fahrenheit"""
        return 200  # Example value
    
class TemperatureAdapter:
    def __init__(self, thermometer):
        self.thermometer = thermometer  # Accepts the legacy thermometer
    
    def get_temperature(self):
        """Converts Fahrenheit to Celsius"""
        fahrenheit = self.thermometer.get_temperature()
        print(fahrenheit)
        celsius = (fahrenheit - 32) * 5.0 / 9.0
        return round(celsius, 2)


# Legacy thermometer
if __name__ == "__main__":
    old_thermometer = FahrenheitThermometer()
    # Adapter makes it compatible with Celsius-based system
    adapter = TemperatureAdapter(old_thermometer)
    print(f"Temperature in Celsius: {adapter.get_temperature()}°C")

