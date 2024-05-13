# DBUS

## What is DBUS

DBus is a cross-desktop standard widely used in Linux Desktop Community. It provides a way for linux desktop applications to communicate with each other. So programmers don't have to implement their own __IPC__ mechanism from scratch.

If you are using something like _KDE_ or _Gnome_, chances are you are already enjoying some features it provides. Say your battery information in the task bar, it is provided by dbus. Or if you are using screensaver, and your screen goes dim when you are enjoying Youtube, disturbing, right? This can be fixed in the screensaver setting, but in fact, you can write a simple script telling screensaver's dbus interface not to do so.

Generally, you can imagine that dbus is a server sitting there, listening to messages and requests from applications, routing them to the right destinations, and responsing to the requests. In fact, this mental model works on most of modern linux distros, though dbus was designed to be able to work without a daemon according to wikipedia.

## Python Bindings

- A quite old one is `pydbus`, it works though


## References

- [A good introduction to dbus, thank __Koen Vervloesem__](https://www.linuxjournal.com/article/10455)
- [Freedesktop introduction to dbus](https://www.freedesktop.org/wiki/IntroductionToDBus/)
- [freedeskop, what is dbus?](https://www.freedesktop.org/wiki/Software/dbus/)
- [Python dbus tutorial](https://dbus.freedesktop.org/doc/dbus-python/tutorial.html)
- [dbus bindings list](https://www.freedesktop.org/wiki/Software/DBusBindings/)
- [What is a bus in computer architecture](https://en.wikipedia.org/wiki/Bus_(computing))
