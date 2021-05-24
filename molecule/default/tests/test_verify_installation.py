# -*- coding: utf-8 -*-
import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_package_installed(host):
    assert host.file('/usr/local/bin/docker-compose').exists
    assert host.file('/usr/local/bin/docker-compose').is_symlink
    assert host.file('/usr/local/bin/docker-compose').mode == 0o777
    assert host.run('docker-compose --version').succeeded


def test_bash_completion(host):
    assert host.package('bash-completion').is_installed
    assert host.file('/etc/bash_completion.d/docker-compose').exists
