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
        extracted = map(extract_lecture_order_and_title, lectures)
        properly_extracted = filter(lambda info: info != None, extracted)

        # then
        self.assertEquals(len(properly_extracted), len(lectures))
    


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

    def itest_output_file_path2(self):
        # given
        input_dir  = '/home/marek/Education/finance/Economics of Money and Banking, Part One'
        output_dir = '/home/marek/Devel/varia/emb3'
        dirpath    = '/home/marek/Education/finance/Economics of Money and Banking, Part One/Lec 10: Dealers and Liquid Security Markets'
        name       = '11 - 1 - 10-1 FT-  Asymmetric Credit Growth in Europe (6-35).mp4'
        # when
        output_file = output_file_path2(input_dir, output_dir, dirpath, name)
        # then
        self.assertEquals(output_file, '/home/marek/Devel/varia/emb3/10 Dealers and Liquid Security Markets/11 - 1 - 10-1 FT-  Asymmetric Credit Growth in Europe (6-35).mp3')

    def test_relative_path(self):
        # given
        input_dir  = '/home/marek/Education/finance/Economics of Money and Banking, Part One'
        dirpath    = '/home/marek/Education/finance/Economics of Money and Banking, Part One/Lec 10: Dealers and Liquid Security Markets'
        # when
        lecture_input_subdir = os.path.relpath(dirpath, input_dir)
        # then
        self.assertEquals(lecture_input_subdir, 'Lec 10: Dealers and Liquid Security Markets')

    def test_extracting_from_file_name(self):
        # given
        name = '1 - 2 - 3-4 The Big Picture (19-20).mp4'
        # when
        technical_lecture_order, technical_part_order, lecture_order, part_order, part_title, minutes, seconds, extension = extract_from_lecture_part(name)
        # then
        self.assertEquals(technical_lecture_order, 1)
        self.assertEquals(technical_part_order, 2)
        self.assertEquals(lecture_order, 3)
        self.assertEquals(part_order, 4)
        self.assertEquals(part_title, 'The Big Picture')
        self.assertEquals(minutes, 19)
        self.assertEquals(seconds, 20)
        self.assertEquals(extension, 'mp4')

    def test_extracting_from_file_names(self):
        # given
        names = [
                '2 - 1 - 1-1 The Big Picture (19-20).mp4',
                '2 - 2 - 1-2 Prerequisites- (7-21).mp4',
                '2 - 3 - 1-3 What is a Bank, a Shadow Bank, a Central Bank- (12-10).mp4',
                '2 - 4 - 1-4 Central Themes (13-07).mp4',
                '2 - 5 - 1-5 Reading-  Allyn Young (3-10).mp4',
                '3 - 1 - 2-1 FT-  The Eurocrisis,  Liquidity vs. Solvency (10-06).mp4',
                '3 - 2 - 2-2 Hierarchy of Financial Instruments (9-39).mp4',
                '3 - 3 - 2-3 Hierarchy of Financial Institutions (6-37).mp4',
                '3 - 4 - 2-4 Dynamics of the Hierarchy (6-08).mp4',
                '3 - 5 - 2-5 Discipline and Elasticity, Currency Principle and Banking Principle (8-49).mp4',
                '3 - 6 - 2-6 Hierarchy of Market Makers (9-16).mp4',
                '3 - 7 - 2-7 Managing the Hierarchy (18-03).mp4'
        ]
        # when
        extracted = map(extract_from_lecture_part, names)
        properly_extracted = filter(lambda info: info != None, extracted)
        # then
        self.assertEquals(len(properly_extracted), len(names))

if __name__ == '__main__':
    unittest.main()
