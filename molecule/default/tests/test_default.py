import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_java_versions(host):
    java8openjdk = host.package("openjdk-8-jdk")
    assert java8openjdk.is_installed


def test_java_default(host):
    java_dest = "/usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java"
    java_alternatives = host.file("/etc/alternatives/java")
    assert java_alternatives.linked_to == java_dest
