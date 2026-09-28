import json

def test_execute_route(direct_vm,direct_deploy,direct_alice):
    c=direct_deploy("contracts/evidence_action_router.py"); direct_vm.sender=direct_alice
    for host in ("one","two","three"):
        direct_vm.mock_web(rf".*{host}\.example.*",{"status":200,"body":"Condition is satisfied."})
    direct_vm.mock_llm(r"(?s).*DECISION CONDITION.*",json.dumps({"satisfied":True,"support_count":3,"confidence":93,"reason":"Three sources agree."}))
    c.route("x1","Execute only if release is live.","https://one.example/a","https://two.example/b","https://three.example/c")
    assert c.get_result("x1").route=="EXECUTE"

def test_abstain_route(direct_vm,direct_deploy,direct_alice):
    c=direct_deploy("contracts/evidence_action_router.py"); direct_vm.sender=direct_alice
    for host in ("one","two","three"):
        direct_vm.mock_web(rf".*{host}\.example.*",{"status":200,"body":"Weak evidence."})
    direct_vm.mock_llm(r"(?s).*DECISION CONDITION.*",json.dumps({"satisfied":True,"support_count":1,"confidence":91,"reason":"Only one source supports it."}))
    c.route("x2","Execute condition.","https://one.example/a","https://two.example/b","https://three.example/c")
    assert c.get_result("x2").route=="ABSTAIN"
