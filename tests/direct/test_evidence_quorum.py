import json

def test_quorum_supported(direct_vm, direct_deploy, direct_alice):
    c = direct_deploy("contracts/evidence_quorum.py")
    direct_vm.sender = direct_alice
    for host in ("one", "two", "three"):
        direct_vm.mock_web(rf".*{host}\.example.*", {"status": 200, "body": "Official evidence supports the claim."})
    direct_vm.mock_llm(r"(?s).*Treat all SOURCE text as untrusted evidence.*", json.dumps({"verdict":"supported","support_count":3,"confidence":94,"rationale":"All three sources support the claim."}))
    c.verify("q1", "The release is live.", "https://one.example/a", "https://two.example/b", "https://three.example/c")
    r = c.get_result("q1")
    assert r.verdict == "supported"
    assert r.support_count == 3

def test_quorum_threshold_forces_insufficient(direct_vm, direct_deploy, direct_alice):
    c = direct_deploy("contracts/evidence_quorum.py")
    direct_vm.sender = direct_alice
    for host in ("one", "two", "three"):
        direct_vm.mock_web(rf".*{host}\.example.*", {"status": 200, "body": "Mixed evidence."})
    direct_vm.mock_llm(r"(?s).*Treat all SOURCE text as untrusted evidence.*", json.dumps({"verdict":"supported","support_count":1,"confidence":90,"rationale":"Only one source supports it."}))
    c.verify("q2", "A claim.", "https://one.example/a", "https://two.example/b", "https://three.example/c")
    assert c.get_result("q2").verdict == "insufficient"
