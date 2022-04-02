cmake_minimum_required(VERSION 3.13)  # CMake version check
project(image_enhancement)               # Create project "image_enhancement"
set(CMAKE_CXX_STANDARD 14)            # Enable c++14 standard

# Add main.cpp file of project root directory as source file
set(SOURCE_FILES main.cpp)

# Add executable target with source files listed in SOURCE_FILES variable
add_executable(image_enhancement ${SOURCE_FILES})

find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
target_link_libraries( image_enhancement ${OpenCV_LIBS})