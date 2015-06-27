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

    def test_lecture_directory2(self):
        # given
        dirpath    = '/home/marek/Education/finance/Economics of Money and Banking, Part One/Lec 10: Dealers and Liquid Security Markets'
        output_dir = '/home/marek/Devel/varia/emb3'
        # when
        subdirectory_path = lecture_subdirectory2(dirpath, output_dir)
        # then
        self.assertEquals(subdirectory_path, '/home/marek/Devel/varia/emb3/10 Dealers and Liquid Security Markets')

    def test_finding_lecture_input_subdirectory(self):
        # given
        dirpath    = '/home/marek/Education/finance/Economics of Money and Banking, Part One/Lec 10: Dealers and Liquid Security Markets'
        # when
        lecture_input_subdir = lecture_input_subdirectory(dirpath)
        # then
        self.assertEquals(lecture_input_subdir, 'Lec 10: Dealers and Liquid Security Markets')
    
    def test_lecture_friendly_name_two_digits(self):
        # given
        lecture_input_subdir = 'Lec 10: Dealers and Liquid Security Markets'
        # when
        name = lecture_sortable_name(lecture_input_subdir)
        # then
        self.assertEquals(name, '10 Dealers and Liquid Security Markets')

    def test_lecture_friendly_name_one_digits(self):
        # given
        lecture_input_subdir = 'Lec 3: Money and the State: Domestic'
        # when
        name = lecture_sortable_name(lecture_input_subdir)
        # then
        self.assertEquals(name, '03 Money and the State: Domestic')

    def test_lecture_title(self):
        # given
        lectures = [
            'Lec 1: The Four Prices of Money',
            'Lec 2:    The Natural Hierarchy of Money',
            'Lec 3: Money and the State: Domestic   ',
            'Lec 4   : The Money View, Micro and Macro',
            'Lec    5: The Central Bank as a Clearinghouse',
            '   Lec 6: Federal Funds, Final Settlement',
            'Lec 7: Repos, Postponing Settlement',
            'Lec 8: Eurodollars, Parallel Settlement',
            'Lec 9: The World that Bagehot Knew',
            'Lec 10: Dealers and Liquid Security Markets',
            'Lec 11: Banks and the Market for Liquidity',
            'Lec 12: Lender-Dealer of Last Resort'
        ]

        # when
        orders_and_titles = map(extract_lecture_order_and_title, lectures)

        # then
        self.assertEquals(len(orders_and_titles), len(lectures))
    

    def test_rebuild_input_file_path(self):
        # given
        dirpath = '/home/marek/Education/finance/Economics of Money and Banking, Part One/Lec 10: Dealers and Liquid Security Markets'
        name    = '11 - 1 - 10-1 FT-  Asymmetric Credit Growth in Europe (6-35).mp4'
        # when
        input_file = rebuild_input_file_path(dirpath, name)
        # then
        self.assertEquals(input_file, '/home/marek/Education/finance/Economics of Money and Banking, Part One/Lec 10: Dealers and Liquid Security Markets/11 - 1 - 10-1 FT-  Asymmetric Credit Growth in Europe (6-35).mp4')

    def test_output_file_path(self):
        # given
        input_dir  = '/home/marek/Education/finance/Economics of Money and Banking, Part One'
        output_dir = '/home/marek/Devel/varia/emb3'
        dirpath    = '/home/marek/Education/finance/Economics of Money and Banking, Part One/Lec 10: Dealers and Liquid Security Markets'
        name       = '11 - 1 - 10-1 FT-  Asymmetric Credit Growth in Europe (6-35).mp4'
        # when
        output_file = output_file_path(input_dir, output_dir, dirpath, name)
        # then
        self.assertEquals(output_file, '/home/marek/Devel/varia/emb3/Lec 10: Dealers and Liquid Security Markets/11 - 1 - 10-1 FT-  Asymmetric Credit Growth in Europe (6-35).mp3')


if __name__ == '__main__':
    unittest.main()
