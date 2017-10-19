# java

Master: [![Build Status](https://travis-ci.org/sansible/java.svg?branch=master)](https://travis-ci.org/sansible/java)  
Develop: [![Build Status](https://travis-ci.org/sansible/java.svg?branch=develop)](https://travis-ci.org/sansible/java)

* [ansible.cfg](#ansible-cfg)
* [Installation and Dependencies](#installation-and-dependencies)
* [Tags](#tags)
* [Examples](#examples)

This roles installs OpenJDK Java or Oracle Java, any version can be installed
but 7 is used by default.




## ansible.cfg

This role is designed to work with merge "hash_behaviour". Make sure your
ansible.cfg contains these settings

```INI
[defaults]
hash_behaviour = merge
```




## Installation and Dependencies

This role has no dependencies and has been tested with Ansible 2.0+.

To install run `ansible-galaxy install sansible.java` or add this to your
`roles.yml`

```YAML
- name: sansible.java
  version: v1.1
```

and run `ansible-galaxy install -p ./roles -r roles.yml`




## Tags

This role uses one tag: **build**

* `build` - Installs Oracle Java.




## Example Playbook

To install OpenJDK Java 7:

```YAML
- name: Install Java
  hosts: sandbox

  roles:
    - name: java
```

To install Oracle Java 7:

```YAML
- name: Install Java
  hosts: sandbox

  roles:
    - name: java
      java:
        vendor: oracle
```

To install OpenJDK Java 8:

```YAML
- name: Install Java
  hosts: sandbox

  roles:
    - name: java
      java:
        version: 8
```
