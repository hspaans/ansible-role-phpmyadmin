"""Role testing files using testinfra."""

import pytest


@pytest.mark.parametrize("pkg", ["phpmyadmin"])
def test_pkg_installed(host, pkg):
    package = host.package(pkg)

    assert package.is_installed
