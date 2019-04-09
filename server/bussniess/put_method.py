from server.app import BOOKS


class PutMethod(object):

    def __init__(self):
        super(PutMethod, self).__init__()

    def remove_book(self, book_id):
        """
        :param data_id:
        :return:
        注意这里的BOOS会随着每次初始化而发生变化，所以使用这种零时变量存储是不适合这种操作，还是放一个文件省事
        """
        for book in BOOKS:
            print(book)
            if book['id'] == book_id:
                BOOKS.remove(book)
                return True
        return False
