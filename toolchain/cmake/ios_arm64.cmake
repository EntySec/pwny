set(CMAKE_SYSTEM_NAME iOS)
set(CMAKE_SYSTEM_PROCESSOR arm64)

set(CMAKE_C_COMPILER clang)
set(CMAKE_CXX_COMPILER clang)
set(CMAKE_AR ar)

set(CMAKE_C_COMPILER_WORKS 1)
set(CMAKE_CXX_COMPILER_WORKS 1)

add_compile_options(-x objective-c -fobjc-arc)

set(CMAKE_OSX_SYSROOT /Users/felix/Desktop/SDKs/iPhoneOS15.6.sdk)
set(CMAKE_OSX_ARCHITECTURES arm64)

add_link_options(-F ${CMAKE_OSX_SYSROOT}/System/Library/PrivateFrameworks)

set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)