#pytest
import pytest

exec_type = "prod"


class Cal():
    def add_num(self, x, y):
        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x + y
        return  result


class TestCal():
    @classmethod
    def setup_class(cls):
        print("start")
        cls.cal = Cal()

    @classmethod
    def teardown_class(cls):
        print("end")
        del cls.cal

    def setup_method(self, method):
        print(f"method={method.__name__}")
        # self.cal = Cal()

    def teardown_method(self, method):
        print(f"method={method.__name__}")
        # del self.cal

    # @pytest.mark.skip(reason="skip!")
    @pytest.mark.skipif(exec_type=="prod", reason="it is production mode!")
    def test_add_num(self):
        assert self.cal.add_num(1,1) == 2

    def test_add_num_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num("1",1)

