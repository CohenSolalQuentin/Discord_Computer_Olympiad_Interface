#!/bin/bash


EXPECTED_DIR_NAME="discord_interface"

CURRENT_DIR_NAME=$(basename "$PWD")

# Verification
if [ "$CURRENT_DIR_NAME" = "$EXPECTED_DIR_NAME" ]; then


python3 -m pip install pexpect

python3 -m pip install -U discord.py

python3 -m pip install -U numpy

python3 -m pip install -U aiofiles

UPPER_DIR_DCOI=$(dirname "$PWD")

echo "export PYTHONPATH=$PYTHONPATH:"$UPPER_DIR_DCOI >> ~/.bashrc

export PYTHONPATH=$PYTHONPATH:$UPPER_DIR_DCOI
echo
echo "DCOI Installation successfull."
echo

else
    echo "Current directory is NOT '$EXPECTED_DIR_NAME'."
    echo "Current directory : '$CURRENT_DIR_NAME'"
fi

