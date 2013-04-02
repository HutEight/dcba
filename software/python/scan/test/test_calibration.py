import unittest
import scipy.io
import os.path
import numpy as np
from numpy.testing import assert_array_less
from scan.data_capture.image import load_from_directory
from scan.data_capture.calibration import intrinsic_calibration_with_checkerboard
from scan.common.util import rel_to_file

@unittest.skip("Slow test. (Run with --no-skip to run)")
class TestCameraCalibration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # excess epsilon to add margin
        cls.eps = np.nextafter(0, 1)
        
        # set up input data dir, parameters
        interior_corners = (8,6)
        side_length = 30 # in mm

        # use results from matlab script to test
        calib_folder = rel_to_file(os.path.join("test-data", "swept-plane", "calib"), __file__)
        calib_images = load_from_directory(calib_folder)
        cls.calib_results = scipy.io.loadmat(os.path.join(calib_folder, "Calib_Results.mat"), squeeze_me=True)

        # run the calibration
        (cls.focal_length, cls.principal_point, cls.alpha, cls.distortion) = intrinsic_calibration_with_checkerboard(
            calib_images, interior_corners, side_length)

    def test_focal_length(self):
        assert_array_less(np.abs(self.focal_length - self.calib_results['fc']), self.calib_results['fc_error'] + self.eps)

    def test_principal_point(self):
        assert_array_less(np.abs(self.principal_point - self.calib_results['cc']), self.calib_results['cc_error'] + self.eps)

    def test_alpha(self):
        assert_array_less(np.abs(self.alpha - self.calib_results['alpha_c']), self.calib_results['alpha_c_error'] + self.eps)

    def test_distortion(self):
        assert_array_less(np.abs(self.distortion - self.calib_results['kc']), self.calib_results['kc_error'] + self.eps)
