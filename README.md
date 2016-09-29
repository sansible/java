# Java

Master: [![Build Status](https://travis-ci.org/sansible/java.svg?branch=master)](https://travis-ci.org/sansible/java)  
Develop: [![Build Status](https://travis-ci.org/sansible/java.svg?branch=develop)](https://travis-ci.org/sansible/java)

* [ansible.cfg](#ansible-cfg)
* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This roles installs Oracle Java 7.




## ansible.cfg

This role is designed to work with merge "hash_behaviour". Make sure your
ansible.cfg contains these settings

```INI
[defaults]
hash_behaviour = merge
```




## Installation and Dependencies

This role has no dependencies and has been tested with Ansible 1.9.4 and 2.2.1.

To install run `ansible-galaxy install sansible.java` or add this to your
`roles.yml`

```YAML
- name: sansible.java
  version: v1.0
```

and run `ansible-galaxy install -p ./roles -r roles.yml`




## Tags

This role uses two tags: **build** and **configure**

* `build` - Installs Oracle Java.
* `configure` - Does nothing. Kept not to error when you run playbook with
  `--tags=configure`




## Example Playbook

To simply install Java:

```YAML
- name: Install GO CD Server
  hosts: sandbox

  roles:
    - name: java
```
