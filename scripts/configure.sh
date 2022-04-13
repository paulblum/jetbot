#!/bin/bash

#configure environment variables
L4T_VERSION_STRING=$(head -n 1 /etc/nv_tegra_release)
L4T_RELEASE=$(echo $L4T_VERSION_STRING | cut -f 2 -d ' ' | grep -Po '(?<=R)[^;]+')
L4T_REVISION=$(echo $L4T_VERSION_STRING | cut -f 2 -d ',' | grep -Po '(?<=REVISION: )[^;]+')
export L4T_VERSION="$L4T_RELEASE.$L4T_REVISION"
export JETBOT_DOCKER_REMOTE=jetbot
export JETBOT_VERSION=0.4.3

#enable docker daemon at boot & set default runtime to NVIDIA
sudo systemctl enable docker
./set_nvidia_runtime.sh

#check 3GB RAM minimum
SYS_RAM_KB=$(awk '/^MemTotal:/{print $2}' /proc/meminfo)
if [ $SYS_RAM_KB -lt 3000000 ]
then
    echo -e "WARNING: Not enough RAM!\n -Required Minimum: 3000000 KB (= 3GB)\n -Installed: ${SYS_RAM_KB} KB"
fi
