# JetBot Software Setup Instructions

[JetBot](https://jetbot.org/) is an open-source robot based on the [NVIDIA Jetson Nano](https://developer.nvidia.com/embedded/jetson-nano-developer-kit). The Jetson Nano uses a removable microSD card as its main storage and boot device. In order to use the Jetson Nano, you'll need to flash a [suitable microSD card](https://amzn.to/2Us6bOv) with an image of the operating system.

## Flash OS to a microSD Card

We'll configure the Jetson Nano with the [NVIDIA JetPack SDK](https://developer.nvidia.com/embedded/jetpack), which provides a Linux operating system, the L4T Driver Package, and libraries for deep learning & accelerated computation.

1. Download and install [Etcher](https://www.balena.io/etcher), an open-source application that can flash OS images to SD cards.

2. Download the [SD Card Image for JetPack 4.5](https://developer.nvidia.com/jetson-nano-sd-card-image-45).
    > Certain SDK versions that are available in the JetPack Archive aren't compatible with JetBot (in part due to [limited docker image availability](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/l4t-pytorch)). The most recent version that's compatible with this code is [JetPack 4.5](https://developer.nvidia.com/jetpack-sdk-45-archive).

3. Insert a microSD card into your computer's SD card drive (or connect via [USB3 adapter](https://amz.run/5TnA)). Launch Etcher and use its GUI to select your drive & the downloaded JetPack 4.5 image file. Press the flash button to write the image to your microSD card– note that flashing will take a while.

## Setup Jetson Nano

A standard initial setup needs to be completed in order to get the JetPack SDK running on Jetson Nano. Follow NVIDIA's [Setup and First Boot](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit#setup) instructions to set up your device.
