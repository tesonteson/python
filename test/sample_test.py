import pytest
import os
import shutil

from sample import Cal



exec_type = "prod"


class TestCal():
    @classmethod
    def setup_class(cls):
        print("start")
        cls.cal = Cal()
        cls.test_file_name = "test.txt"
        cls.test_dir = "/tmp/test_dir"

    @classmethod
    def teardown_class(cls):
        print("end")
        del cls.cal
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)

    def setup_method(self, method):
        print(f"method={method.__name__}")
        # self.cal = Cal()

    def teardown_method(self, method):
        print(f"method={method.__name__}")
        # del self.cal

    # @pytest.mark.skip(reason="skip!")
    # @pytest.mark.skipif(exec_type=="prod", reason="it is production mode!")
    def test_add_num(self, tmpdir, csv_file):
        print(csv_file)
        print(tmpdir)
        assert self.cal.add_num(1,1) == 2

    def test_add_num_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num("1",1)

    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(tmpdir, self.test_file_name)
        assert os.path.exists(test_file_path) is True

    def test_save_no_dir(self):
        self.cal.save(self.test_dir, self.test_file_name)
        test_file_path = os.path.join(self.test_dir, self.test_file_name)
        assert os.path.exists(test_file_path) is True

