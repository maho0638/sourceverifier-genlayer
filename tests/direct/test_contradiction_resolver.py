import json

def test_detects_conflict(direct_vm, direct_deploy, direct_alice):
    c = direct_deploy("contracts/contradiction_resolver.py")
    direct_vm.sender = direct_alice
    direct_vm.mock_web(r".*a\.example.*", {"status":200,"body":"Launch is October 1."})
    direct_vm.mock_web(r".*b\.example.*", {"status":200,"body":"Launch is October 15."})
    direct_vm.mock_llm(r"(?s).*material factual disagreement.*", json.dumps({"outcome":"conflict","conflict_level":95,"rationale":"The dates conflict."}))
    c.resolve("r1","launch date","https://a.example/x","https://b.example/y")
    r=c.get_result("r1")
    assert r.outcome=="conflict"
    assert r.conflict_level==95

def test_rejects_same_url(direct_vm, direct_deploy, direct_alice):
    c=direct_deploy("contracts/contradiction_resolver.py")
    direct_vm.sender=direct_alice
    with direct_vm.expect_revert("Sources must differ"):
        c.resolve("r2","x","https://a.example/x","https://a.example/x")
