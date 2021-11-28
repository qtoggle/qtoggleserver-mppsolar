## About

This is an addon for [qToggleServer](https://github.com/qtoggle/qtoggleserver).

It provides MPP Solar inverters (and similar) support for qToggleServer.

Currently, only status reading is supported. No changes to the inverter configuration can be done via this add-on.


## Install

Install using pip:

    pip install qtoggleserver-mppsolar


## Supported Models

Currently supported models include:

 * GK
 * MK
 * LV
 * MAX


## Usage

### Serial Connection

##### `qtoggleserver.conf:`
``` ini
...
peripherals = [
    ...
    {
        driver = "qtoggleserver.mppsolar.SerialMPPSolarInverter"
        name = "myinverter"             # an optional name of your choice
        serial_port = "/dev/ttyUSB0"    # use /dev/hidraw0 if using the USB connection
        serial_baud = 2400              # this is the default
        model = "GK"                    # model letters found in inverter model (e.g. "GK" for "PIP 5048GK")
        blacklist_properties = [...]    # optional list of property names to be excluded
        # optional min SoC required to force battery into discharge mode (defaults to null, i.e. disabled)
        force_battery_discharge_min_soc = 10
        # optional min grid voltage required to force battery into charge mode (defaults to null, i.e. disabled)
        force_battery_charge_grid_min_voltage = 200 
    }
    ...
]
...
```

### Bluetooth Connection

*note*: The bluetooth connection variant is limited to just a few read-only inverter properties.

##### `qtoggleserver.conf:`
``` ini
...
peripherals = [
    ...
    {
        driver = "qtoggleserver.mppsolar.BluetoothMPPSolarInverter"
        name = "myinverter"             # an optional name of your choice
        address = "00:1A:22:AA:BB:CC"   # bluetooth address of the device
        model = "GK"                    # model letters found in inverter model (e.g. "GK" for "PIP 5048GK")
    }
    ...
]
...
```
