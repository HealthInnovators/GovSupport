import boto3
import botocore
import json

# --- RUN `sam local start-lambda` TO START THE LOCAL LAMBDA ENDPOINT ---
lambda_client = boto3.client(
    "lambda",
    region_name="eu-west-2",
    endpoint_url="http://127.0.0.1:3001",
    use_ssl=False,
    verify=False,
    config=botocore.client.Config(signature_version=botocore.UNSIGNED),
)


# --- RUN `pytest` TO RUN THE TESTS ---
def test_supervise_enrolment_domain_true():
    with open("tests/events/GovSupportLocalMessageEvent.json") as event:
        CONVERSATIONS_EVENT = json.load(event)

    response = lambda_client.invoke(
        FunctionName="SuperviseFunction",
        InvocationType="RequestResponse",
        Payload=json.dumps(CONVERSATIONS_EVENT),
    )

    response = json.load(response["Payload"])

    assert response == "Supervision Event Received"


def test_supervise_enrolment_domain_false():
    with open("tests/events/GovSupportLocalMessageEvent_UnknownDomain.json") as event:
        CONVERSATIONS_EVENT = json.load(event)

    response = lambda_client.invoke(
        FunctionName="SuperviseFunction",
        InvocationType="RequestResponse",
        Payload=json.dumps(CONVERSATIONS_EVENT),
    )

    response = json.load(response["Payload"])
    response = json.loads(response)

    assert response == {
        "text": "Your domain is not enrolled in GovSupport. Please contact your administrator."
    }


def test_supervise_enrolment_user_true():
    with open("tests/events/GovSupportLocalMessageEvent.json") as event:
        CONVERSATIONS_EVENT = json.load(event)

    response = lambda_client.invoke(
        FunctionName="SuperviseFunction",
        InvocationType="RequestResponse",
        Payload=json.dumps(CONVERSATIONS_EVENT),
    )

    response = json.load(response["Payload"])

    assert response == "Supervision Event Received"


def test_supervise_enrolment_user_false():
    with open("tests/events/GovSupportLocalMessageEvent_UnknownUser.json") as event:
        CONVERSATIONS_EVENT = json.load(event)

    response = lambda_client.invoke(
        FunctionName="SuperviseFunction",
        InvocationType="RequestResponse",
        Payload=json.dumps(CONVERSATIONS_EVENT),
    )

    response = json.load(response["Payload"])
    response = json.loads(response)

    assert response == {
        "text": "User is not registered, please contact your administrator for support in onboarding to GovSupport"
    }


def test_supervise_invoke():
    with open("tests/events/GovSupportLocalMessageEvent.json") as event:
        CONVERSATIONS_EVENT = json.load(event)

    response = lambda_client.invoke(
        FunctionName="SuperviseFunction",
        InvocationType="RequestResponse",
        Payload=json.dumps(CONVERSATIONS_EVENT),
    )

    response = json.load(response["Payload"])

    assert response == "Supervision Event Received"
