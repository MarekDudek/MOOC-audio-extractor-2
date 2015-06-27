import unittest

import sys
sys.path.append('src')
from paths_processing import *

class PathsProcessing(unittest.TestCase):

    def test_lecture_directory(self):
        # given
        dirpath    = '/home/marek/Education/finance/Economics of Money and Banking, Part One/Lec 10: Dealers and Liquid Security Markets'
        output_dir = '/home/marek/Devel/varia/emb3'
        # when
        subdirectory_path = lecture_subdirectory(dirpath, output_dir)
        # then
        self.assertEquals(subdirectory_path, '/home/marek/Devel/varia/emb3/Lec 10: Dealers and Liquid Security Markets')

    def test_rebuild_input_file_path(self):
        # given
        dirpath = '/home/marek/Education/finance/Economics of Money and Banking, Part One/Lec 10: Dealers and Liquid Security Markets'
        name    = '11 - 1 - 10-1 FT-  Asymmetric Credit Growth in Europe (6-35).mp4'
        # when
        input_file = rebuild_input_file_path(dirpath, name)
        # then
        self.assertEquals(input_file, '/home/marek/Education/finance/Economics of Money and Banking, Part One/Lec 10: Dealers and Liquid Security Markets/11 - 1 - 10-1 FT-  Asymmetric Credit Growth in Europe (6-35).mp4')

if __name__ == '__main__':
    unittest.main()
