import unittest

from main import get_doc_owner_name, get_all_doc_owners_names, get_doc_shelf, add_new_doc, add_new_shelf, delete_doc, \
    move_doc_to_shelf, directories


class TestSecretary(unittest.TestCase):

    def test_user_doc_number(self):
        self.assertEqual(get_doc_owner_name('2207 876234'), 'Василий Гупкин')
        self.assertEqual(get_doc_owner_name('2207'), None)

    def test_get_all_doc_owners_names(self):
        self.assertEqual(get_all_doc_owners_names(), {'Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов'})

    def test_get_doc_shelf(self):
        self.assertEqual(get_doc_shelf('2207 876234'), '1')
        self.assertEqual(get_doc_shelf('2207'), None)

    def test_add_new_doc(self):
        self.assertEqual(add_new_doc('1234 567891', 'doc_type', 'Name Surname', '3'), '3')

    def test_add_new_shelf(self):
        self.assertEqual(add_new_shelf('4'), ('4', True))
        self.assertEqual(add_new_shelf('1'), ('1', False))

    def test_delete_doc(self):
        self.assertEqual(delete_doc('10006'), ('10006', True))
        self.assertEqual(delete_doc('2207'), None)

    def test_move_doc_to_shelf(self):
        move_doc_to_shelf('11-2', '3')
        self.assertIn('11-2', directories['3'])
        self.assertNotIn('11-2', directories['1'])


if __name__ == '__main__':
    unittest.main()
