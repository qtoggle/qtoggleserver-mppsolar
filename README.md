## About

This is an addon for [qToggleServer](https://github.com/qtoggle/qtoggleserver).

It provides MPP Solar inverters (and similar) support for qToggleServer.

This package is based on @jblance's [mpp-solar](https://github.com/jblance/mpp-solar) project and @ltowarek's 
[fork](https://github.com/ltowarek/mpp-solar).

Currently, only status reading is supported. No changes to the inverter configuration can be done via this add-on.


## Install

Install using pip:

    pip install qtoggleserver-mppsolar


## Usage

##### `qtoggleserver.conf:`
``` ini
...
peripherals = [
    ...
    {
        driver = "qtoggleserver.mppsolar.MPPSolarInverter"
        name = "myinverter"             # a name of your choice
        serial_port = "/dev/ttyUSB0"
        serial_baud = 2400              # this is the default
        status_properties = [           # leave unset to get all available properties
            "ac_output_active_power"
            "ac_output_voltage"
            ...
        ]
    }
    ...
]
...
```
