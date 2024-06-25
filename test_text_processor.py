import unittest
from text_processor import TextProcessor

class TestTextProcessor(unittest.TestCase):
    def test_clean_text(self):
        tp = TextProcessor("Hello, World!")
        tp.clean_text()
        self.assertEqual(tp.cleaned_text, "hello world")

        tp = TextProcessor("123 ABC!!!")
        tp.clean_text()
        self.assertEqual(tp.cleaned_text, "abc")

        tp = TextProcessor("")
        tp.clean_text()
        self.assertEqual(tp.cleaned_text, "")

    def test_remove_stop_words(self):
        tp = TextProcessor("this is a test")
        tp.clean_text()
        tp.remove_stop_words(['this', 'is'])
        self.assertEqual(tp.cleaned_text, "a test")

        tp = TextProcessor("this is a test")
        tp.remove_stop_words(['this', 'is'])
        self.assertEqual(tp.cleaned_text, "a test")

        tp = TextProcessor("hello world")
        tp.clean_text()
        tp.remove_stop_words([])
        self.assertEqual(tp.cleaned_text, "hello world")

if __name__ == '__main__':
    unittest.main()
