#!/bin/bash

# Exit on any error
set -e

pip install mpremote

echo "Deleting the lib/XRPLib/ files in the XRP"
read -p "Press Enter to continue..."
mpremote rm -r :/lib/XRPLib

xrp_cp() {
  local url="$1"
  local dest="$2"
  tmpfile=$(mktemp)
  curl -s "$url" -o "$tmpfile"
  python3 -m mpremote fs cp "$tmpfile" :"$dest"
  rm "$tmpfile"
}

echo "Upload starting!"

base_url="https://raw.githubusercontent.com/cornell-cup/astrobee"
xrp_cp "$base_url/ece_astrobee_testing_file.py" ece_astrobee_testing_file.py
xrp_cp "$base_url/maneuvers_async_new.py" maneuvers_async_new.py

xrp_cp "$base_url/lib/XRPLib/__init__.py" lib/XRPLib/__init__.py
xrp_cp "$base_url/lib/XRPLib/board.py" lib/XRPLib/board.py
xrp_cp "$base_url/lib/XRPLib/defaults.py" lib/XRPLib/defaults.py
xrp_cp "$base_url/lib/XRPLib/imu.py" lib/XRPLib/imu.py
xrp_cp "$base_url/lib/XRPLib/imu_defs.py" lib/XRPLib/imu_defs.py
xrp_cp "$base_url/lib/XRPLib/pid.py" lib/XRPLib/pid.py
xrp_cp "$base_url/lib/XRPLib/resetbot.py" lib/XRPLib/resetbot.py
xrp_cp "$base_url/lib/XRPLib/servo.py" lib/XRPLib/servo.py
xrp_cp "$base_url/lib/XRPLib/version.py" lib/XRPLib/version.py
xrp_cp "$base_url/lib/XRPLib/x_controller_async.py" lib/XRPLib/x_controller_async.py
xrp_cp "$base_url/lib/XRPLib/y_controller_async.py" lib/XRPLib/y_controller_async.py
xrp_cp "$base_url/lib/XRPLib/z_controller_async.py" lib/XRPLib/z_controller_async.py

echo "Upload complete!"
