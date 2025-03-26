from collections import OrderedDict


class LimitedSizeDict(OrderedDict):
    """
    Кеш для хранения запросов
    """

    def __init__(self, *args, **kwargs):
        self.limit = kwargs.pop('limit', None)
        super().__init__(*args, **kwargs)
        self._check_size_limit()

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self._check_size_limit()

    def _check_size_limit(self):
        if self.limit is not None:
            while len(self) > self.limit:
                self.popitem(last=False)
