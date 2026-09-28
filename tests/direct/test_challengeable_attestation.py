import json

def test_one_fresh_challenge(direct_vm, direct_deploy, direct_alice):
    c=direct_deploy("contracts/challengeable_attestation.py")
    direct_vm.sender=direct_alice
    direct_vm.mock_web(r".*one\.example.*", {"status":200,"body":"Evidence supports the claim."})
    direct_vm.mock_web(r".*two\.example.*", {"status":200,"body":"Evidence supports the claim."})
    direct_vm.mock_llm(r"(?s).*Use only these sources.*", json.dumps({"verdict":"supported","confidence":92}))
    c.create("c1","A claim.","https://one.example/a","https://two.example/b")
    c.challenge("c1")
    r=c.get_record("c1")
    assert r.challenged is True
    assert r.final_verdict=="supported"
    with direct_vm.expect_revert("Challenge already used"):
        c.challenge("c1")

def test_finalize_blocks_challenge(direct_vm, direct_deploy, direct_alice):
    c=direct_deploy("contracts/challengeable_attestation.py")
    direct_vm.sender=direct_alice
    direct_vm.mock_web(r".*one\.example.*", {"status":200,"body":"Evidence."})
    direct_vm.mock_web(r".*two\.example.*", {"status":200,"body":"Evidence."})
    direct_vm.mock_llm(r"(?s).*Use only these sources.*", json.dumps({"verdict":"insufficient","confidence":70}))
    c.create("c2","A claim.","https://one.example/a","https://two.example/b")
    c.finalize("c2")
    with direct_vm.expect_revert("Record already finalized"):
        c.challenge("c2")
