import json

def test_material_change(direct_vm,direct_deploy,direct_alice):
    c=direct_deploy("contracts/web_change_monitor.py"); direct_vm.sender=direct_alice
    direct_vm.mock_web(r".*status\.example.*",{"status":200,"body":"Terms now require 30 days notice."})
    direct_vm.mock_llm(r"(?s).*materially changes the facts or commitments.*",json.dumps({"changed":True,"materiality":88,"summary":"Notice period changed."}))
    c.inspect("m1","https://status.example/page","Terms require 7 days notice.")
    r=c.get_record("m1")
    assert r.changed is True and r.materiality==88

def test_cosmetic_change_not_material(direct_vm,direct_deploy,direct_alice):
    c=direct_deploy("contracts/web_change_monitor.py"); direct_vm.sender=direct_alice
    direct_vm.mock_web(r".*status\.example.*",{"status":200,"body":"Same facts, reordered wording."})
    direct_vm.mock_llm(r"(?s).*materially changes the facts or commitments.*",json.dumps({"changed":True,"materiality":20,"summary":"Cosmetic wording only."}))
    c.inspect("m2","https://status.example/page","Same facts.")
    assert c.get_record("m2").changed is False
