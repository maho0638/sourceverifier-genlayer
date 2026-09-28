"""Live Studionet proof for CitationAttestor."""

import pytest
from gltest import get_contract_factory
from gltest.assertions import tx_execution_succeeded

def _field(value,name):
    if isinstance(value,dict):
        return value.get(name)
    return getattr(value,name)

@pytest.mark.integration
def test_citation_attestor_live_studionet():
    factory=get_contract_factory("CitationAttestor")
    contract=factory.deploy(consensus_max_rotations=4)
    print(f"CITATION_ATTESTOR_CONTRACT={contract.address}",flush=True)
    tx=contract.attest(args=[
        "iana-example-attestation-v1",
        "example.com is intended for use in documentation examples.",
        "https://www.iana.org/help/example-domains",
    ]).transact(wait_interval=10000,wait_retries=50)
    assert tx_execution_succeeded(tx)
    print(f"CITATION_ATTESTOR_RECEIPT={tx}",flush=True)
    result=contract.get_attestation(args=["iana-example-attestation-v1"]).call()
    verdict=str(_field(result,"verdict"))
    confidence=int(_field(result,"confidence"))
    excerpt=str(_field(result,"excerpt"))
    print(f"CITATION_ATTESTOR_VERDICT={verdict}",flush=True)
    print(f"CITATION_ATTESTOR_CONFIDENCE={confidence}",flush=True)
    print(f"CITATION_ATTESTOR_EXCERPT={excerpt}",flush=True)
    assert verdict=="supports"
    assert confidence>=65
    assert excerpt
