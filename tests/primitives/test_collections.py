from unittest import TestCase

from botlang import BotlangSystem
from botlang.environment.primitives.collections import get_value_in_dict
from botlang.evaluation.values import Nil


class CollectionsTestCase(TestCase):

    def test_get_value_in_dict(self):
        the_dict = {'datos': {'mensajes': {'user': {'text': 'Jose'}}}}

        result_value = get_value_in_dict(the_dict, 'datos.mensajes.user.text')
        expected_value = 'Jose'
        self.assertEqual(expected_value, result_value)

        result_value = get_value_in_dict(the_dict, 'datos.mensajes')
        expected_value = {'user': {'text': 'Jose'}}

        self.assertEqual(expected_value, result_value)

        result_value = get_value_in_dict({'dict': {}}, 'dict')
        expected_value = {}

        self.assertEqual(expected_value, result_value)

        with self.assertRaises(KeyError):
            get_value_in_dict(the_dict, 'texto')
        with self.assertRaises(KeyError):
            get_value_in_dict({}, 'texto')
        with self.assertRaises(KeyError):
            get_value_in_dict({}, '')

    def test_get(self):
        value = BotlangSystem.run("""
            (define a_dict (make-dict))
            (put! a_dict "uno" 1)
            (get a_dict "uno")
        """)
        self.assertEqual(1, value)

        value = BotlangSystem.run("""
            (define a_dict (make-dict))
            (define another_dict (make-dict))
            (put! another_dict "uno" 1)
            (put! a_dict "another_dict" another_dict)
            (get a_dict "another_dict.uno")
        """)
        self.assertEqual(1, value)

        value = BotlangSystem.run("""
            (define a_dict (make-dict))
            (define another_dict (make-dict))
            (put! another_dict "uno" 1)
            (put! another_dict "dos" 2)
            (put! a_dict "another_dict" another_dict)
            (get-or-nil a_dict "another_dict.tres")
        """)
        self.assertEqual(Nil, value)

        value = BotlangSystem.run("""
            (define a_list (list "hola" "como" "estas"))
            (get a_list 2)
        """)
        self.assertEqual("estas", value)

        value = BotlangSystem.run("""
            (define a_list (list "hola" "como" "estas"))
            (get-or-nil a_list 3)
        """)
        self.assertEqual(Nil, value)

