#!/bin/bash
current_dir=$(dirname "$(readlink -f "$0")")

git clone https://github.com/wanghaEMQ/pynng-mqtt.git
cd pynng-mqtt
git submodule update --init --recursive

# Install msquic to system
cd nng/extern/msquic
mkdir -p build
cd build
cmake ..
make -j8
# install if build successfully
make install

# Go back to the root path of pynng-mqtt and install.
cd $current_dir/pynng-mqtt
pip3 install --user asyncio
pip3 install -e .
