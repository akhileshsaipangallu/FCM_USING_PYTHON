from pyfcm import FCMNotification


# your FCM_SERVER_KEY
FCM_SERVER_KEY = '<Your FCM_SERVER_KEY>'
push_service = FCMNotification(api_key=FCM_SERVER_KEY)

# registration_id of your device
registration_id = '<device registration_id>'

# registration_ids for bulk message
registration_ids = [
    '<device registration_id 1>',
    '<device registration_id 2>',
    '.....'
]

message_title = "Notification tittle"
message_body = "Notification body"

data_message = {
    "Nick": "Mario",
    "body": "great match!",
    "Room": "PortugalVSDenmark"
}

# Notify Single Device
result_one = push_service.notify_single_device(
    registration_id=registration_id,
    message_title=message_title,
    message_body=message_body,
    data_message=data_message,
)

# Notify  Multiple Devices
result_two = push_service.notify_multiple_devices(
    registration_ids=registration_ids,
    message_title=message_title,
    message_body=message_body,
    data_message=data_message,
)

# Print responses
print result_one
print result_two
