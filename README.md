# Java

This roles installs Oracle Java.




## ansible.cfg

This role is designed to work with merge "hash_behaviour". Make sure your
ansible.cfg contains these settings

```INI
[defaults]
hash_behaviour = merge
```




## Example Playbook

To simply install GO CD server:

```YAML
- name: Install GO CD Server
  hosts: sandbox

  roles:
    - java
```
