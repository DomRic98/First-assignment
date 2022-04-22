import os
import unittest
from download_sequential import download
import pytest

class TestDownload(unittest.TestCase):
    def setUp(self):
        self.files_list = ["VBF_HToTauTau.root", "GluGluToHToTauTau.root"]
        self.files_dim = [24184554, 20460281]  # bytes

    def test_download_dim(self):
        """
        Check on the size of the downloaded files compared to the expected one.

        :return: If it passed ok, if it failed: "The dimensions aren't the same".
        """
        print("TEST 2 - Called...")
        dim_result = []
        for file in self.files_list:
            dim_result.append(os.stat(file).st_size)
        self.assertEqual(dim_result, self.files_dim, "The dimensions aren't the same")


if __name__ == '__main__':
    test_order = ["test_download_files", "test_download_dim"]
    loader = unittest.TestLoader()
    loader.sortTestMethodsUsing = lambda x, y: test_order.index(x) - test_order.index(y)
    unittest.main(testLoader=loader, verbosity=2)
