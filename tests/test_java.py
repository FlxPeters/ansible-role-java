from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_java_is_available(Command):
    which_java = Command("which java")
    assert which_java.rc == 0
