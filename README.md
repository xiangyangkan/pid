# mix-pid

[![Travis](https://travis-ci.com/m-lundberg/simple-pid.svg?branch=master)](https://travis-ci.com/m-lundberg/simple-pid)
[![PyPI](https://img.shields.io/pypi/v/simple-pid.svg)](https://pypi.org/project/simple-pid/)
[![Read the Docs](https://img.shields.io/readthedocs/simple-pid.svg)](https://simple-pid.readthedocs.io/)
[![License](https://img.shields.io/github/license/m-lundberg/simple-pid.svg)](https://github.com/m-lundberg/simple-pid/blob/master/LICENSE.md)

A simple and easy to use PID controller in Python. If you want a PID controller without external dependencies that just works, this is for you! The PID was designed to be robust with help from [Brett Beauregards guide](http://brettbeauregard.com/blog/2011/04/improving-the-beginners-pid-introduction/).

Usage is very simple:

```python
from pid import PID
pid = PID(kp=1.0, ki=0.0, kd=0.0,
                 set_pressure=0,
                 thresholds=(-10, 10),
                 gear=1,
                 throttle_limits=((30, 60), (40, 65), (50, 70)),
                 output_limits=(None, None),
                 auto_mode=True)

# assume we have a system we want to control in controlled_system
v = controlled_system.update(0)

while True:
    # compute new ouput from the PID according to the systems current value
    control = pid(input_pressure, input_angle)
    
    # feed the PID output to the system and get its current value
    v = controlled_system.update(control)
```

Complete API documentation can be found [here](https://simple-pid.readthedocs.io/en/latest/simple_pid.html#module-simple_pid.PID).

## Installation
To install, run:
```
pip install mix-pid
```

## Usage
The `PID` class implements `__call__()`, which means that to compute a new output value, you simply call the object like this:
```python
output = pid(input_pressure, input_angle)
```

### The basics
To set the setpoint, ie. the value that the PID is trying to achieve, simply set it like this:
```python
pid.set_pressure = 0.5
```

The tunings can be changed any time when the PID is running. They can either be set individually or all at once:
```python
pid.Ki = 1.0
pid.tunings = (1.0, 0.2, 0.4)
```

In order to get output values in a certain range, and also to avoid [integral windup](https://en.wikipedia.org/wiki/Integral_windup) (since the integral term will never be allowed to grow outside of these limits), the output can be limited to a range:
```python
pid.output_limits = (0, 10)    # output value will be between 0 and 10
pid.output_limits = (0, None)  # output will always be above 0, but with no upper bound
```

### Other features
#### Auto mode
To disable the PID so that no new values are computed, set auto mode to False:
```python
pid.auto_mode = False  # no new values will be computed when pid is called
pid.auto_mode = True   # pid is enabled again
```
When disabling the PID and controlling a system manually, it might be useful to tell the PID controller where to start from when giving back control to it. This can be done by enabling auto mode like this:
```python
pid.set_auto_mode(True, last_output=0.4)
```
This will set the I-term to the value given to `last_output`, meaning that if the system that is being controlled was stable at that output value the PID will keep the system stable if started from that point, without any big bumps in the output when turning the PID back on.

#### Observing separate components
When tuning the PID, it can be useful to see how each of the components contribute to the output. They can be seen like this:
```python
p, i, d = pid.components  # the separate terms are now in p, i, d
```

## Tests
Use the following to run tests:
```
tox
```

## License
Licensed under the [MIT License](https://github.com/m-lundberg/simple-pid/blob/master/LICENSE.md).
