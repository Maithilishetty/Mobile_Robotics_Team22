#include <opencv2/opencv.hpp>
#include <opencv2/ximgproc.hpp>
#include <fstream>
#include <string>
#include <vector>

using namespace cv;
using namespace std;
using cv::CLAHE;

int main(const int argc, const char **argv) {

    if (argc != 3) {
        std::cout << "Invalid command line args" << std::endl;
        return -1;
    }

    std::string img_in(argv[1]);
    std::string img_out(argv[2]);

    cv::Mat src = imread(img_in, IMREAD_GRAYSCALE);
    cv::Mat res;

    // ~~~~~~~~~~~~~~~~~~~ IMAGE PROCESSING HERE ~~~~~~~~~~~~~~~~~~~


    cv::Mat gui_small, gui_large;
    cv::Ptr<cv::ximgproc::GuidedFilter> f_small = cv::ximgproc::createGuidedFilter(src, 2, 0.1*0.1);
    cv::Ptr<cv::ximgproc::GuidedFilter> f_large = cv::ximgproc::createGuidedFilter(src, 2*10, 0.1*0.1);
    f_small->filter(src, gui_small);
    f_large->filter(src, gui_large);

    cv::Mat residual = gui_small - gui_large;
    cv::Mat detail = gui_small + 5 * residual;
    Ptr<CLAHE> clahe = createCLAHE();
    clahe->setClipLimit(8);
    clahe->setTilesGridSize(cv::Size2i(8,8));
    clahe->apply(detail, res);


    // ~~~~~~~~~~~~~~~~~~~ END IMAGE PROCESSING ~~~~~~~~~~~~~~~~~~~

    src.push_back(res);
    imshow("Result", src);

    imwrite(img_out, res);

    waitKey(0);

}
