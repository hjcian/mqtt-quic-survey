install MQTT client (for quick testing)

- https://mqttx.app/docs/downloading-and-installation

## troubleshooting
```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/app/pynng-mqtt/pynng/__init__.py", line 3, in <module>
    from ._nng import lib, ffi
ImportError: libmsquic.so.2: cannot open shared object file: No such file or directory
```

Solution

> https://blog.csdn.net/u014072827/article/details/123023495
>
```bash
root@eaca7a455c77:/app/python# whereis libmsquic.so.2
libmsquic.so.2: /usr/local/lib/libmsquic.so.2

root@eaca7a455c77:/app/python# cat /etc/ld.so.conf
include /etc/ld.so.conf.d/*.conf
/usr/local/lib/

# reload the library
root@eaca7a455c77:/app/python# ldconfig
```
