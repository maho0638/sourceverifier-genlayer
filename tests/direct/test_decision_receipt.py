import json

def test_receipt_yes(direct_vm,direct_deploy,direct_alice):
    c=direct_deploy("contracts/decision_receipt.py"); direct_vm.sender=direct_alice
    direct_vm.mock_web(r".*one\.example.*",{"status":200,"body":"Yes evidence."})
    direct_vm.mock_web(r".*two\.example.*",{"status":200,"body":"Yes evidence."})
    direct_vm.mock_llm(r"(?s).*QUESTION:.*",json.dumps({"decision":"yes","confidence":90,"rationale":"Both sources support yes."}))
    c.decide("d1","Did it happen?","https://one.example/a","https://two.example/b")
    r=c.get_receipt("d1")
    assert r.decision=="yes" and r.confidence==90

def test_low_confidence_abstains(direct_vm,direct_deploy,direct_alice):
    c=direct_deploy("contracts/decision_receipt.py"); direct_vm.sender=direct_alice
    direct_vm.mock_web(r".*one\.example.*",{"status":200,"body":"Unclear."})
    direct_vm.mock_web(r".*two\.example.*",{"status":200,"body":"Unclear."})
    direct_vm.mock_llm(r"(?s).*QUESTION:.*",json.dumps({"decision":"yes","confidence":40,"rationale":"Weak evidence."}))
    c.decide("d2","Did it happen?","https://one.example/a","https://two.example/b")
    assert c.get_receipt("d2").decision=="abstain"
