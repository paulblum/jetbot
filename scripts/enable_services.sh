source configure.sh # setup env vars

WORKSPACE=${1:-$HOME/jetbot} # default working directory for jupyter lab
CAMERA=${2:-opencv_gst_camera} # default opencv camera, alt is ZMQ for multi-container access

# enable jetbot display service
sudo docker run -it -d \
    --name jetbot_display \
    --network host \
    --runtime nvidia \
    --restart always \
    --privileged \
    $JETBOT_DOCKER_REMOTE/jetbot:display-$JETBOT_VERSION-$L4T_VERSION

# enable jetbot jupyter lab service
sudo docker run -it -d \
    --name jetbot_jupyter \
    --network host \
    --runtime nvidia \
    --restart always \
    --privileged \
    --env JETBOT_DEFAULT_CAMERA=$CAMERA \
    -v /dev/bus/usb:/dev/bus/usb \
    -v /tmp/argus_socket:/tmp/argus_socket \
    -v $WORKSPACE:/workspace \
    -w /workspace \
    $JETBOT_DOCKER_REMOTE/jetbot:jupyter-$JETBOT_VERSION-$L4T_VERSION
