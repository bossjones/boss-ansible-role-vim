import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize('f',
                         ['software-properties-common',
                         'python-dev',
                         'python-pip',
                         'python3-dev',
                         'python3-pip'])
def test_packages_installed(host, f):
    pkg = host.package(f)
    assert pkg.is_installed
