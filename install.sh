#!/usr/bin/env bash
# This Code Write by Mr.nope
# Calendar 1.3

if [[ "$(id -u)" -ne 0 ]]; then
  echo ""
  echo "Please, Run This Programm as Root!"
  echo ""
  exit 1
fi
main() {
  printf '\033]2;Calendar/Installing\a'
  clear
  echo "Installing..."
  chmod +x run.py
  sleep 2
  apt install python
  apt install python3
  apt install python3-pip
  pip3 install --upgrade pip
  echo ""
  echo "<Finish>"
  echo "
Usage:
      python3 run.py
      "
  exit 1
}
main