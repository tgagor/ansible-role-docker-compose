Ansible role for docker-compose
===============================

This role will install docker-compose on compatible platforms.

[![Molecule Test](https://github.com/tgagor/ansible-role-docker-compose/actions/workflows/test-and-release.yml/badge.svg)](https://github.com/tgagor/ansible-role-docker-compose/actions/workflows/test-and-release.yml)
[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-tgagor-docker-compose.svg)](https://galaxy.ansible.com/tgagor/docker-compose)

## Supported systems

* Ubuntu
  * 18.04
  * 20.04
  * 20.10
  * 21.04
* Debian
  * 9 (stretch)
  * 10 (buster)
  * 11 (bullseye)
* CentOS
  * 7
  * 8
* Fedora
  * 33
  * 34

## Requirements

If `docker_compose_enable_bash_completion` is set to `true`, role will install `bash-completion` package.

## Role variables

Role doesn't require any custom variables.

## Dependencies

There are no dependencies on other roles.

## Example playbook

Just add to you playbook, to install it on `localhost`:

```yaml
- hosts: localhost
  connection: local
  gather_facts: true
  become: yes
  tasks:
    - name: Install docker_compose
      include_role:
        name: tgagor.docker_compose
```

## License
-------

See [LICENSE](LICENSE)
