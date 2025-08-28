\[app]
title = SmartAlarm
package.name = smartalarm
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0

# Permissions (needed for alarms & wakelock)
android.permissions = WAKE_LOCK, RECEIVE_BOOT_COMPLETED

[buildozer]
log_level = 2
warn_on_root = 1
