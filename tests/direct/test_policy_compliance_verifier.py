import json

def test_policy_compliance(direct_vm, direct_deploy, direct_alice):
    c=direct_deploy("contracts/policy_compliance_verifier.py")
    direct_vm.sender=direct_alice
    direct_vm.mock_web(r".*artifact\.example.*", {"status":200,"body":"Report includes two sources and a signed author statement."})
    direct_vm.mock_llm(r"(?s).*Evaluate it only against POLICY.*", json.dumps({"compliant":True,"confidence":91,"findings":"All required fields are present."}))
    c.verify("p1","Must include two sources and an author statement.","https://artifact.example/report")
    r=c.get_result("p1")
    assert r.compliant is True
    assert r.confidence==91

def test_low_confidence_fails_closed(direct_vm, direct_deploy, direct_alice):
    c=direct_deploy("contracts/policy_compliance_verifier.py")
    direct_vm.sender=direct_alice
    direct_vm.mock_web(r".*artifact\.example.*", {"status":200,"body":"Ambiguous content."})
    direct_vm.mock_llm(r"(?s).*Evaluate it only against POLICY.*", json.dumps({"compliant":True,"confidence":40,"findings":"Unclear."}))
    c.verify("p2","Must be clear.","https://artifact.example/report")
    assert c.get_result("p2").compliant is False
