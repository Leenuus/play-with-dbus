#!/usr/bin/env python
# NOTE: pitfall
# make sure you install dependency
# pip install pycairo PyGObject
# this package don't setup dependency for you
from dasbus.connection import SessionMessageBus

bus = SessionMessageBus()

proxy = bus.get_proxy("org.freedesktop.Notifications", "/org/freedesktop/Notifications")

specs = proxy.Introspect()
print(specs)

id = proxy.Notify(
    "",
    0,
    "face-smile",
    "Hello World!",
    "This notification can be ignored.",
    [],
    {},
    1000,
)

print("The notification {} was sent.".format(id))
