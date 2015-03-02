# -*- coding: cp1252 -*-
import unittest
import extractor as ex

class TestExtractorMethod(unittest.TestCase):
    def test_flipkart_1(self):
        assert ex.find_product_sizes("product_pages/product1.html") == ['39', '40', '42', '44']

    def test_flipkart_2(self):
        assert ex.find_product_discount("product_pages/product1.html") == "495"

    def test_shopclues_1(self):
        assert ex.find_product_fabric("product_pages/product2.html") == "cotton"

    def test_shopclues_2(self):
        assert ex.find_product_stylecode("product_pages/product2.html") == "180624"

    def test_zovi_1(self):
        assert ex.find_product_sizes("product_pages/product3.html") == ['39', '40', '42', '44', '46']

    def test_zovi_2(self):
        assert ex.find_product_gender("product_pages/product3.html") == "men"

    def test_rakuten_1(self):
         assert ex.find_product_price("product_pages/product4.html") == "$24.99"

    def test_rakuten_2(self):
        assert ex.find_product_fabric("product_pages/product4.html") == "cotton"

    def test_qoo10_1(self):
        assert ex.find_product_title("product_pages/product5.html") == "'â˜…New Slim Fit Dress SHIRTSâ˜…KOREA Mens Shirts Solid Short/long-sleeve Slim Line KOREA'"
    
    def test_qoo10_2(self):
        assert ex.find_product_discount("product_pages/product5.html") == "$35.65"

if __name__ == '__main__':
    unittest.main()

