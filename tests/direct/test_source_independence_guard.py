import json

def test_detects_syndication(direct_vm, direct_deploy, direct_alice):
    c=direct_deploy("contracts/source_independence_guard.py")
    direct_vm.sender=direct_alice
    direct_vm.mock_web(r".*one\.example.*", {"status":200,"body":"Originally published by Wire X. Same article."})
    direct_vm.mock_web(r".*two\.example.*", {"status":200,"body":"Originally published by Wire X. Same article."})
    direct_vm.mock_llm(r"(?s).*genuinely independent evidence sources.*", json.dumps({"independent":False,"confidence":96,"relationship":"syndicated","rationale":"Both republish the same wire copy."}))
    c.check("i1","https://one.example/a","https://two.example/b")
    r=c.get_result("i1")
    assert r.independent is False
    assert r.relationship=="syndicated"

def test_requires_distinct_sources(direct_vm, direct_deploy, direct_alice):
    c=direct_deploy("contracts/source_independence_guard.py")
    direct_vm.sender=direct_alice
    with direct_vm.expect_revert("Sources must differ"):
        c.check("i2","https://one.example/a","https://one.example/a")
