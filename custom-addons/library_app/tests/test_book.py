from odoo.tests.common import TransactionCase


class TestBook(TransactionCase):
    print('test book read .......')
    def setUp(self, *args, **kwargs):
        print('test book runing .......')
        result = super().setUp(*args, **kwargs)
        user_admin = self.env.ref('base.user_admin')
        self.env = self.env(user=user_admin)
        self.Book = self.env['library.book']
        self.book_ode = self.Book.create({
            'name': 'Odoo Development Essentials',
            'isbn': '879-1-78439-279-6'})
        return result

    def test_create(self):
        "Test Books are active by default"
        print('test book check .......')
        self.assertEqual(self.book_ode.active, True)

    def test_check_isbn(self):
        "Check valid ISBN"
        print('test book check isbn.......')
        self.assertTrue(self.book_ode._check_isbn)