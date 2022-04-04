#ifndef __IMAGE_ENHANCEMENT_H__
#define __IMAGE_ENHANCEMENT_H__

#include <opencv2/core/core.hpp>
#include <opencv2/opencv.hpp>
#include <opencv2/ximgproc.hpp>
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"
#include <stdio.h>
#include <string>

using cv::CLAHE;

class ImageEnhancement {

public:
    ImageEnhancement(std::string method) {
        m = method;
    }

    void enhance(cv::Mat src, cv::Mat &res) {
        if (m == "simple") {
            simple_enhancement(src, res);
        } else {
            res = src;
        }
    }

private:

    // Image enhancement methods
    void simple_enhancement(cv::Mat src, cv::Mat &res) {
        cv::Mat gui_small, gui_large;
        cv::Ptr<cv::ximgproc::GuidedFilter> f_small = cv::ximgproc::createGuidedFilter(src, 2, 0.1*0.1);
        cv::Ptr<cv::ximgproc::GuidedFilter> f_large = cv::ximgproc::createGuidedFilter(src, 2*10, 0.1*0.1);
        f_small->filter(src, gui_small);
        f_large->filter(src, gui_large);

        cv::Mat residual = gui_small - gui_large;
        cv::Mat detail = gui_small + 4 * residual;
        cv::Ptr<CLAHE> clahe = cv::createCLAHE();
        clahe->setClipLimit(8);
        clahe->setTilesGridSize(cv::Size2i(8,8));
        clahe->apply(detail, res);
    }

    std::string m;
    double a;
};

#endif