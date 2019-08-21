# PID锅炉燃烧器控制算法

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mix-pid)
![PyPI - License](https://img.shields.io/pypi/l/mix-pid)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/mix-pid)
![PyPI](https://img.shields.io/pypi/v/mix-pid)
![PyPI](https://img.shields.io/badge/mixiot-2.0%20%7C%203.0-blue)


## 例子

```python
from pid import PID
pid = PID(kp=1.0, ki=0.0, kd=0.0,
          set_pressure=0.5,
          thresholds=(-10, 10),
          throttle_limits=((30, 60), (40, 65), (50, 70)),
          output_limits=(None, None),
          auto_mode=True)
pid(input_gear=1, input_pressure=0.4, input_angle=59)
```

完整的API文档在 [这里](https://mix-pid.readthedocs.io/en/latest/simple_pid.html#module-simple_pid.PID).

## 安装
```
pip install mix-pid
```

## 使用
每次的调用反馈返回此次推荐的油嘴档位和风门角度值
```python
output_gear, output_angle = pid(input_pressure, input_angle)
```

### 参数说明
设置目标压力
```python
pid.set_pressure = 0.5
```

设置Kp, Ki, Kd系数
```python
pid.Ki = 1.0
pid.tunings = (1.0, 0.2, 0.4)
```

设置判断决策的阈值
```python
pid.thresholds=(-10, 10)
```

设置燃烧器不同档位的风门角度限制
```python
pid.throttle_limits=((30, 60), (40, 65), (50, 70))
```

设置PID输出限制避免出现[integral windup](https://en.wikipedia.org/wiki/Integral_windup)
```python
pid.output_limits = (0, 10)    # output value will be between 0 and 10
pid.output_limits = (0, None)  # output will always be above 0, but with no upper bound
```

设置手动/自动模式
```python
pid.auto_mode=True
pid.auto_mode=False
```

## 许可证
Licensed under the [MIT License](https://github.com/xiangyangkan/pid/blob/master/LICENSE).
