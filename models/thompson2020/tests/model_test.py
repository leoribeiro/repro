import unittest
from parameterized import parameterized

from repro.models.thompson2020 import Prism
from repro.testing import assert_dicts_approx_equal, get_testing_device_parameters


class TestThompson202Models(unittest.TestCase):
    @parameterized.expand(get_testing_device_parameters())
    def test_prism_references_example(self, device: int):
        # Tests the examples from the Github repo
        model = Prism(device=device)
        inputs = [
            {"candidate": "Hi world.", "references": ["Hello world."]},
            {"candidate": "This is a Test.", "references": ["This is a test."]},
        ]
        expected_macro = {"prism": -1.0184666}
        expected_micro = [{"prism": -1.4878583}, {"prism": -0.5490748}]
        actual_macro, actual_micro = model.predict_batch(inputs)

        assert_dicts_approx_equal(expected_macro, actual_macro)
        assert len(expected_micro) == len(actual_micro)
        for expected, actual in zip(expected_micro, actual_micro):
            assert_dicts_approx_equal(expected, actual, abs=1e-4)

    @parameterized.expand(get_testing_device_parameters())
    def test_prism_sources_example(self, device: int):
        # Tests the examples from the Github repo
        model = Prism(device=device)
        inputs = [
            {"candidate": "Hi world.", "sources": ["Bonjour le monde."]},
            {"candidate": "This is a Test.", "sources": ["C'est un test."]},
        ]
        expected_macro = {"prism": -1.8306842}
        expected_micro = [{"prism": -2.462842}, {"prism": -1.1985264}]
        actual_macro, actual_micro = model.predict_batch(inputs)

        assert_dicts_approx_equal(expected_macro, actual_macro)
        assert len(expected_micro) == len(actual_micro)
        for expected, actual in zip(expected_micro, actual_micro):
            assert_dicts_approx_equal(expected, actual, abs=1e-4)

    def test_invalid_input(self):
        model = Prism()
        inputs = [{"candidate": "Hi world."}, {"candidate": "This is a Test."}]
        with self.assertRaises(Exception):
            model.predict_batch(inputs)

        inputs = [
            {"candidate": "Hi world.", "references": ["Hello world."]},
            {"candidate": "This is a Test.", "sources": ["C'est un test."]},
        ]
        with self.assertRaises(Exception):
            model.predict_batch(inputs)

        inputs = [
            {"candidate": "Hi world.", "references": ["Hello world."]},
            {
                "candidate": "This is a Test.",
            },
        ]
        with self.assertRaises(Exception):
            model.predict_batch(inputs)

        inputs = [
            {
                "candidate": "Hi world.",
            },
            {"candidate": "This is a Test.", "sources": ["C'est un test."]},
        ]
        with self.assertRaises(Exception):
            model.predict_batch(inputs)

    @parameterized.expand(get_testing_device_parameters())
    def test_prism_translation_regression(self, device: int):
        # Tests using Prism as a translation system using
        # the examples from https://github.com/thompsonb/prism/tree/master/translation
        model = Prism(device=device)
        inputs = [
            {"source": "Hi world."},
            {"source": "This is a Test."},
            {"source": "Some of my Best Friends are Linguists."},
        ]

        actual_outputs = model.translate_batch("fr", inputs)
        assert actual_outputs == [
            "Le Monde.",
            "C'est un test.",
            "Certains de mes meilleurs amis sont linguistes.",
        ]
