import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hostname_file(host):
    hostname_file = host.file("/etc/hostname")
    assert hostname_file.contains("instance")


def test_host_file(host):
    localhost = host.addr("instance")
    assert '127.0.0.1' in localhost.ip_addresses


def test_users(host):
    assert host.user("test_sudo_user").exists
    assert 'sudo' in host.user("test_sudo_user").groups
    assert host.user("test_standard_user").exists
    assert 'sudo' not in host.user("test_standard_user").groups
    assert 'bar' in host.user("test_standard_user").groups


def test_locale(host):
    assert 'LANG=en_US.UTF-8' in host.run("localectl status").stdout


def test_locale_list(host):
    locale_list = host.run("localectl list-locales").stdout
    assert 'fr_FR' in locale_list
    assert 'ar_IN' in locale_list
    assert 'ga_IE' in locale_list
    assert 'fr_LU' in locale_list


def test_ntp(host):
    assert ('System clock synchronized: yes' in host.run("timedatectl status").stdout
            or 'NTP enabled: yes' in host.run("timedatectl status").stdout)


def test_sudo_nopasswd(host):
    assert 'uid=0' in host.run("sudo -i -u test_sudo_user sudo -i id").stdout
