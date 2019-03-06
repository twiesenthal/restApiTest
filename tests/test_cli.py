import logging
import mock
import rest_api_test


class TestCli():

    def test_noOptions(self):
        rest_api_test.cli.main([])

    def test_hasVerboseShort(self):
        rest_api_test.cli.main(["-v"])

    def test_hasVerboseLong(self):
        rest_api_test.cli.main(["--verbose"])

    def test_hasQuietShort(self):
        rest_api_test.cli.main(["-q"])

    def test_hasQuietLong(self):
        rest_api_test.cli.main(["--quiet"])
