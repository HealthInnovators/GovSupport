from GovSupport_core.models import GovSupportMessageEvent
from GovSupport_core.services.anonymise import analyse


def format_message(event):
    GovSupport_message = GovSupportMessageEvent(
        type="PROCESS_CHAT_MESSAGE",
        user=event["user"],
        name=event["name"],
        space_id=event["space_id"],
        thread_id=event["thread_id"],
        message_id=event["message_id"],
        message_string=event["message_string"],
        source_client="GovSupport Local",
        timestamp=event["timestamp"],
    )

    if "proceed" not in event:
        pii_identified = analyse(GovSupport_message.message_string)

        if pii_identified:
            # Optionally redact PII from the message by importing redact from services.anonymise
            # message_string = redact(message_string, pii_identified)

            print(
                "PII detected in event, run with proceed set to true to bypass warning"
            )

            return "PII Detected"

    return GovSupport_message
