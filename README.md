# Real-time Image Enhancement for Visual-Inertial SLAM in Underwater Scenarios
### EECS 568 Team 22

This repository contains the code for our final project for EECS 568: Mobile Robotics: Methods and Algorithms. Our project compared two different SLAM algorithms, ORB-SLAM3 and OKVIS. Then, we examined the effects of real-time image enhancement on both algorithms.

Here (TODO) is a link to our paper.
  
Here (TODO) is a link to our final presentation and video.

There are three separate projects within this repository: ORB-SLAM3 with Image Enhancement, OKVIS with Image Enhancement, and Single Image Enhancement. We used the <a href="https://www.lirmm.fr/aqualoc/">Aqualoc dataset</a> to test all of our projects. In particular, we made use of Harbor_01 sequence. To run the example dataset, it needs to be in the correct format, which can be downloaded [here](https://drive.google.com/file/d/15avpUuBbduXZoZ_Zv__WsQhbammBiMAz). You can also download it from source and manually convert it.

## ORB-SLAM3 with Image Enhancement

TODO insert ORB-SLAM3 build instructions here.

First, install dependencies.

- <a href="https://github.com/stevenlovegrove/Pangolin">Pangolin</a>
```
cd ~/<directory>
git clone --recursive https://github.com/stevenlovegrove/Pangolin.git
cd Pangolin
git checkout v0.6
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_FLAGS=-std=c++11 ..
make -j$nproc
sudo make install
```
- <a href="https://docs.opencv.org/4.2.0/d9/df8/tutorial_root.html">OpenCV 4.2.0</a>:

Install the dependency packages:
```
sudo apt-get install build-essential
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
```
Clone opencv and opencv_contrib:
```
cd ~/<directory>
git clone https://github.com/opencv/opencv.git
git clone https://github.com/opencv/opencv_contrib.git
cd opencv
cd ..
cd opencv_contrib
cd ..
```
Compile and install <a href="https://github.com/opencv/opencv">opencv</a> as well as <a href="https://github.com/opencv/opencv_contrib">opencv_contrib</a>:
```
cd opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX=/usr/local \
      -D INSTALL_C_EXAMPLES=ON \
      -D INSTALL_PYTHON_EXAMPLES=ON \
      -D WITH_TBB=ON \
      -D WITH_V4L=ON \
      -D WITH_QT=ON \
      -D WITH_OPENGL=ON \
      -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
      -D BUILD_EXAMPLES=ON ..
make -j$nproc
sudo make install
sudo sh -c 'echo "/usr/local/lib" >> /etc/ld.so.conf.d/opencv.conf'
sudo ldconfig
```

- <a href="https://eigen.tuxfamily.org/index.php?title=Main_Page">Eigen3</a>
```
sudo apt install libeigen3-dev
```

Here is the link to the original <a href="https://github.com/nindanaoto/ORB_SLAM3">ORB_SLAM3</a> repository we use.
To build our ORB_SLAM3_modified project:
```
cd ORB_SLAM3_modified
chmod +x build.sh
./build.sh
```
To run the project. For example, on harbor dataset:

TODO explain about the image_method parameter 

For Monocular-Inertial sensor,
```
./Examples/Monocular-Inertial/mono_inertial_harbor ./Vocabulary/ORBvoc.txt <path_to_config_file> <path_to_dataset_folder>  <path_to_timestamps> <output_filename> [image_method]
```

## OKVIS with Image Enhancement

The second project is [OKVIS](https://github.com/ethz-asl/okvis) modified to include image enhancement capabilities. To build, first install dependencies:

- CMake: ```sudo apt-get install cmake```
- Google-Glog and GFlags: ```sudo apt-get install libgoogle-glog-dev```
- BLAS and LAPACK: ```sudo apt-get install libatlas-base-dev```
- Eigen3: ```sudo apt-get install libeigen3-dev```
- SuiteSparse and CXSparse: ```sudo apt-get install libsuitesparse-dev```
- Boost: ```sudo apt-get install libboost-dev libboost-filesystem-dev```
- OpenCV 4.2.0: ```sudo apt-get install libopencv-dev```

Then, from the root directory of the repository:

- Go into the OKVIS project: ```cd okvis```
- Create the build directory: ```mkdir build```
- Generate the Makefile: ```cmake ..```
- Build the project: ```make -j```

The project can now be run from the build directory as:

```./okvis_app_synchronous <path_to_okvis_config_yaml> <path_to_dataset> <image_enhancement_technique>```

To run the example (AQUALOC Harbor) dataset, it needs to be in the correct format, which can be downloaded [here](https://drive.google.com/file/d/15avpUuBbduXZoZ_Zv__WsQhbammBiMAz). You can also download it from source and manually convert it. Then, run:

```./okvis_app_synchronous ../config/config_harbor.yaml <path_to_transformed_harbor_dataset>```

## Single Image Enhancement

Last is the image enhancement project, which is an extremely simple project that can be used to test various image enhancement algorithms on single images at a time, to see if features and contrast will be improved. First, install dependencies:

- CMake: ```sudo apt-get install cmake```
- OpenCV 4.2.0: ```sudo apt-get install libopencv-dev```

Then, from the root directory of this repository:

- Go into the Image Enhancement project: ```cd image_enhancement```
- Create the build directory: ```mkdir build && cd build```
- Generate the Makefile: ```cmake ..```
- Build the project: ```make -j```

The project can be run from the build directory as ```./image_enhancement <path_to_input_image> <path_to_output_image>```

## Evaluation

TODO add explanations for evaluation
