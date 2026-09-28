import json

def test_attests_excerpt(direct_vm, direct_deploy, direct_alice):
    c=direct_deploy("contracts/citation_attestor.py")
    direct_vm.sender=direct_alice
    direct_vm.mock_web(r".*docs\.example.*", {"status":200,"body":"Version 3 launched on September 20."})
    direct_vm.mock_llm(r"(?s).*verbatim evidence.*", json.dumps({"verdict":"supports","excerpt":"Version 3 launched on September 20.","confidence":98}))
    c.attest("a1","Version 3 launched on September 20.","https://docs.example/release")
    r=c.get_attestation("a1")
    assert r.verdict=="supports"
    assert "September 20" in r.excerpt

def test_requires_https(direct_vm, direct_deploy, direct_alice):
    c=direct_deploy("contracts/citation_attestor.py")
    direct_vm.sender=direct_alice
    with direct_vm.expect_revert("Source must use HTTPS"):
        c.attest("a2","x","http://docs.example")
