"""Live Studionet proof for ChallengeableAttestation."""

import pytest
from gltest import get_contract_factory
from gltest.assertions import tx_execution_succeeded

def _field(value,name):
    if isinstance(value,dict):
        return value.get(name)
    return getattr(value,name)

@pytest.mark.integration
def test_challengeable_attestation_live_studionet():
    factory=get_contract_factory("ChallengeableAttestation")
    contract=factory.deploy(consensus_max_rotations=4)
    print(f"CHALLENGEABLE_ATTESTATION_CONTRACT={contract.address}",flush=True)
    record_id="example-domain-challenge-v1"
    create=contract.create(args=[
        record_id,
        "example.com is intended for use in documentation examples.",
        "https://example.com",
        "https://www.iana.org/help/example-domains",
    ]).transact(wait_interval=10000,wait_retries=50)
    assert tx_execution_succeeded(create)
    print(f"CHALLENGEABLE_CREATE_RECEIPT={create}",flush=True)
    challenge=contract.challenge(args=[record_id]).transact(wait_interval=10000,wait_retries=50)
    assert tx_execution_succeeded(challenge)
    print(f"CHALLENGEABLE_CHALLENGE_RECEIPT={challenge}",flush=True)
    final=contract.get_record(args=[record_id]).call()
    assert bool(_field(final,"challenged")) is True
    assert str(_field(final,"final_verdict"))=="supported"
    print(f"CHALLENGEABLE_FINAL_VERDICT={_field(final,'final_verdict')}",flush=True)
    print(f"CHALLENGEABLE_CONFIDENCE={int(_field(final,'confidence'))}",flush=True)
