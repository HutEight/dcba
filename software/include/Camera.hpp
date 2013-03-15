#ifndef CAMERA_H
#define CAMERA_H

#include <opencv2/opencv.hpp>
#include "OpticalEquipment.hpp"
#include "Image.hpp"

class Image;

class Camera : OpticalEquipment {
  public:
    //Property: OpenCV's VideoCapture object. TODO: May not want this as an
    //object property once we integrate our own cameras
    cv::VideoCapture& device;

    // Constructor: Only takes a VideoCapture device as argument. TODO: remove
    // this constructor so that imaging devices will always have their intrinsic
    // and external parameters in their object
    Camera(cv::VideoCapture& device) : device(device) {};
        
    /*
     * Method: captureImage
     * Given the device location information for a camera, this orders that
     * camera to take a picture, and then captures the information in that
     * picture and returns it as an <Image> object
     */

    // for other initialization possibilities, see
    // http://docs.opencv.org/modules/highgui/doc/reading_and_writing_images_and_video.html?highlight=capturefromcam#videocapture-videocapture
    static Image captureImage(const int deviceNum = 0);
    static Image captureImage(cv::VideoCapture& capture);
    static Image captureImage(const Camera& camera);
    static std::vector<Image> captureImages(int deviceNum = 0, int numImages = 1, int delayMillis = 10);
};

#endif
