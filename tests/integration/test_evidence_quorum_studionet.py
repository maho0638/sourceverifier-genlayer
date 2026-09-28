"""Live Studionet proof for EvidenceQuorum."""

import pytest
from gltest import get_contract_factory
from gltest.assertions import tx_execution_succeeded

def _field(value, name):
    if isinstance(value, dict):
        return value.get(name)
    return getattr(value, name)

@pytest.mark.integration
def test_evidence_quorum_live_studionet():
    factory=get_contract_factory("EvidenceQuorum")
    contract=factory.deploy(consensus_max_rotations=4)
    print(f"EVIDENCE_QUORUM_CONTRACT={contract.address}",flush=True)
    tx=contract.verify(args=[
        "example-domain-quorum-v1",
        "example.com is intended for use in documentation examples.",
        "https://example.com",
        "https://www.iana.org/help/example-domains",
        "https://www.rfc-editor.org/rfc/rfc2606",
    ]).transact(wait_interval=10000,wait_retries=50)
    assert tx_execution_succeeded(tx)
    print(f"EVIDENCE_QUORUM_RECEIPT={tx}",flush=True)
    result=contract.get_result(args=["example-domain-quorum-v1"]).call()
    verdict=str(_field(result,"verdict"))
    support=int(_field(result,"support_count"))
    confidence=int(_field(result,"confidence"))
    print(f"EVIDENCE_QUORUM_VERDICT={verdict}",flush=True)
    print(f"EVIDENCE_QUORUM_SUPPORT={support}",flush=True)
    print(f"EVIDENCE_QUORUM_CONFIDENCE={confidence}",flush=True)
    assert verdict=="supported"
    assert support>=2
    assert confidence>=65
