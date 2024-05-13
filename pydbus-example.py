#!/usr/bin/env python

import dbus
from icecream import ic

def main():

    sebus = dbus.SessionBus()
    sybus = dbus.SystemBus()

    notification_bus_name = "org.freedesktop.Notifications"
    notification_obj_path = "/org/freedesktop/Notifications"

    n_proxy = sebus.get_object(notification_bus_name, notification_obj_path)

    res = n_proxy.Introspect()
    ic(res)
    iface = dbus.Interface(n_proxy, "org.freedesktop.Notifications")
    notify = iface.Notify
    ic(notify)
    notify(
        "",
        0,
        "face-smile",
        "Hello World!",
        "This notification can be ignored.",
        [],
        {},
        1000,
    )


if __name__ == "__main__":
    main()
