import unittest

import sys
sys.path.append('src')
from paths_processing import *

class PathsProcessing(unittest.TestCase):

    def test_lecture_directory(self):
        # given
        dirpath = '/home/marek/Education/finance/Economics of Money and Banking, Part One/Lec 10: Dealers and Liquid Security Markets'
        output_dir = '/home/marek/Devel/varia/emb3'
        # when
        subdirectory_path = lecture_subdirectory(dirpath, output_dir)
        # then
        self.assertEquals(subdirectory_path, '/home/marek/Devel/varia/emb3/Lec 10: Dealers and Liquid Security Markets')

if __name__ == '__main__':
    unittest.main()
