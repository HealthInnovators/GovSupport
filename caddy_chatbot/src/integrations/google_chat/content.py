# --- Status Messages --- #

PROCESSING = "<b>Requesting GovSupport to help with this query</b>"

GENERATING_RESPONSE = "<b>Composing answer to your query</b>"

FAILURE = '<b><font color="#FF0000">GovSupport failed to respond</font></b>'

AWAITING_APPROVAL = "<b>Awaiting approval</b>"

SUPERVISOR_REVIEWING = "<b>Supervisor reviewing response</b>"

# --- Google Chat Messages ---

DOMAIN_NOT_ENROLLED = {
    "text": "GovSupport is not currently available for this domain. Please contact your administrator for more information."
}

USER_NOT_ENROLLED = {
    "text": "GovSupport is not currently registered for you. Please contact your administrator for support in onboarding to GovSupport"
}

USER_NOT_SUPERVISOR = {
    "text": "Only registered supervisors can use GovSupport Supervisor. Please contact your administrator to gain the supervisor role."
}

INTRODUCE_GovSupport_IN_DM = "Hi, I'm GovSupport! \n\n I'm an AI powered co-pilot for Citizens Advice advisers, I'm here to help give advice to support in resolving your client queries."

INTRODUCE_GovSupport_IN_SPACE = "Hi, I'm GovSupport! \n\n Thank you for adding me to {space_name}. \n\n I'm an AI powered co-pilot for Citizens Advice advisers, I'm here to help give advice to support in resolving your client queries."

SURVEY_ALREADY_COMPLETED = {
    "text": "_*This thread is now closed, please start a new call thread*_"
}

PII_DETECTED = '<b><font color="#FF0000">PII DETECTED</font><b> <i>Please ensure all queries to GovSupport are anonymised. \n\n Choose whether to proceed anyway or edit your original query<i>'

INTRODUCE_GovSupport_SUPERVISOR_IN_DM = "Hi, I'm the supervisor assistant for GovSupport! GovSupport is an AI powered co-pilot for Citizens Advice advisers. \n *To get started you will need to register the advisers into your supervision space so their messages come to you, you can do this by typing `/addUser` into the chat, other user management functionality can be seen using /help*"

INTRODUCE_GovSupport_SUPERVISOR_IN_SPACE = "Hi, thank you for adding me to {space_name}, I'm the supervisor assistant for GovSupport! GovSupport is an AI support for Citizens Advice advisers. \n\nGovSupport uses information from the below sites to form answers: \nGOV UK \nCitizens Advice \nAdviserNet \n\n*To get started you will need to register the advisers into your supervision space so their messages come to you, you can do this by typing `/addUser` into the chat, other user management functionality can be seen using `/help`*"

EXISTING_CALL_REMINDER = "<font color=\"#004F88\"><b>Active GovSupport Interaction from {call_start_time}</b></font>\n\n<i>It looks like you've already got an open chat with GovSupport that hasn't been marked as complete yet! While we're evaluating GovSupport, it's really important we obtain a completed feedback survey from every call.</i> \n\n <font color=\"#004F88\"><b>Is this request to GovSupport linked to a new call, or is your previous call still ongoing?</b></font>"

# --- Google Chat Cards --- #

PROCESSING_MESSAGE = {
    "cardsV2": [
        {
            "cardId": "StatusCard",
            "card": {
                "sections": [
                    {
                        "widgets": [
                            {
                                "decoratedText": {
                                    "icon": {"materialIcon": {"name": "pending"}},
                                    "topLabel": "Status",
                                    "text": PROCESSING,
                                },
                            }
                        ]
                    }
                ]
            },
        },
    ],
}

COMPOSING_MESSAGE = {
    "cardsV2": [
        {
            "cardId": "StatusCard",
            "card": {
                "sections": [
                    {
                        "widgets": [
                            {
                                "decoratedText": {
                                    "icon": {"materialIcon": {"name": "notes"}},
                                    "topLabel": "Status",
                                    "text": GENERATING_RESPONSE,
                                }
                            }
                        ]
                    }
                ]
            },
        },
    ],
}

COMPOSING_MESSAGE_RETRY = {
    "cardsV2": [
        {
            "cardId": "StatusCard",
            "card": {
                "sections": [
                    {
                        "widgets": [
                            {
                                "decoratedText": {
                                    "icon": {"materialIcon": {"name": "refresh"}},
                                    "topLabel": "Status",
                                    "text": GENERATING_RESPONSE,
                                    "bottomLabel": "Something went wrong, retrying...",
                                }
                            }
                        ]
                    }
                ]
            },
        },
    ],
}

REQUEST_FAILURE = {
    "cardsV2": [
        {
            "cardId": "StatusCard",
            "card": {
                "sections": [
                    {
                        "widgets": [
                            {
                                "decoratedText": {
                                    "icon": {"materialIcon": {"name": "feedback"}},
                                    "topLabel": "Status",
                                    "text": FAILURE,
                                    "bottomLabel": "Please try again shortly",
                                }
                            }
                        ]
                    }
                ]
            },
        },
    ],
}

RESPONSE_STREAMING = {
    "decoratedText": {
        "icon": {"materialIcon": {"name": "pending"}},
        "topLabel": "GovSupport response still processing...",
    }
}

SUPERVISOR_REVIEWING_RESPONSE = {
    "cardsV2": [
        {
            "cardId": "StatusCard",
            "card": {
                "sections": [
                    {
                        "widgets": [
                            {
                                "decoratedText": {
                                    "icon": {
                                        "materialIcon": {"name": "quick_reference_all"}
                                    },
                                    "topLabel": "Status",
                                    "text": SUPERVISOR_REVIEWING,
                                }
                            }
                        ]
                    }
                ]
            },
        },
    ],
}

AWAITING_SUPERVISOR_APPROVAL = {
    "cardsV2": [
        {
            "cardId": "StatusCard",
            "card": {
                "sections": [
                    {
                        "widgets": [
                            {
                                "decoratedText": {
                                    "icon": {
                                        "materialIcon": {"name": "supervisor_account"}
                                    },
                                    "topLabel": "Status",
                                    "text": AWAITING_APPROVAL,
                                }
                            }
                        ]
                    }
                ]
            },
        },
    ],
}

CALL_COMPLETE = {
    "cardsV2": [
        {
            "cardId": "callCompleteConfirmed",
            "card": {
                "sections": [
                    {
                        "widgets": [
                            {
                                "decoratedText": {
                                    "icon": {"materialIcon": {"name": "support_agent"}},
                                    "topLabel": "",
                                    "text": '<b><font color="#00ba01">Call complete</font></b>',
                                    "bottomLabel": "<b>Please complete the post call survey below</b>",
                                }
                            }
                        ]
                    }
                ]
            },
        },
    ],
}

CONTINUE_EXISTING_INTERACTION = {
    "cardsV2": [
        {
            "cardId": "continue_interaction",
            "card": {
                "sections": [
                    {
                        "widgets": [
                            {
                                "decoratedText": {
                                    "icon": {"materialIcon": {"name": "resume"}},
                                    "topLabel": "",
                                    "text": '<b><font color="#004F88">Continuing existing interaction</font></b>',
                                    "bottomLabel": "<b>Message sent to GovSupport for processing</b>",
                                }
                            }
                        ]
                    }
                ]
            },
        },
    ],
}

END_EXISTING_INTERACTION = {
    "cardsV2": [
        {
            "cardId": "end_interaction",
            "card": {
                "sections": [
                    {
                        "widgets": [
                            {
                                "decoratedText": {
                                    "icon": {"materialIcon": {"name": "call_end"}},
                                    "topLabel": "",
                                    "text": '<b><font color="#004F88">Finalising existing interaction</font></b>',
                                    "bottomLabel": "<b>Complete the survey below for GovSupport to process your new query.</b>",
                                }
                            }
                        ]
                    }
                ]
            },
        },
    ],
}

SURVEY_COMPLETE_WIDGET = {
    "widgets": [
        {
            "decoratedText": {
                "icon": {"materialIcon": {"name": "data_exploration"}},
                "topLabel": "<b>Survey complete</b>",
                "bottomLabel": "Thank you for completing your post call survey!",
            }
        }
    ]
}

INTRODUCE_GovSupport_DM_CARD = {
    "cardsV2": [
        {
            "cardId": "IntroductionCard",
            "card": {
                "sections": [
                    {
                        "widgets": [
                            {
                                "columns": {
                                    "columnItems": [
                                        {
                                            "horizontalSizeStyle": "FILL_AVAILABLE_SPACE",
                                            "horizontalAlignment": "CENTER",
                                            "verticalAlignment": "CENTER",
                                            "widgets": [
                                                {
                                                    "textParagraph": {
                                                        "text": INTRODUCE_GovSupport_IN_DM
                                                    }
                                                },
                                                {
                                                    "decoratedText": {
                                                        "icon": {
                                                            "materialIcon": {
                                                                "name": "priority_high"
                                                            }
                                                        },
                                                        "topLabel": "Getting started",
                                                        "text": "Just message for my help",
                                                    }
                                                },
                                            ],
                                        },
                                        {
                                            "widgets": [
                                                {
                                                    "image": {
                                                        "imageUrl": "https://ai.gov.uk/img/GovSupport1.webp",
                                                        "altText": "GovSupport, an owl icon",
                                                    }
                                                }
                                            ]
                                        },
                                    ]
                                }
                            },
                        ],
                    }
                ]
            },
        }
    ]
}

INTRODUCE_GovSupport_SUPERVISOR_DM_CARD = {
    "sections": [
        {
            "widgets": [
                {
                    "columns": {
                        "columnItems": [
                            {
                                "horizontalSizeStyle": "FILL_AVAILABLE_SPACE",
                                "horizontalAlignment": "CENTER",
                                "verticalAlignment": "CENTER",
                                "widgets": [
                                    {
                                        "textParagraph": {
                                            "text": "Hi, I'm GovSupport's supervisor companion! \n\n GovSupport is an AI powered co-pilot for Citizens Advice advisers using content from the below:"
                                        }
                                    },
                                    {
                                        "decoratedText": {
                                            "icon": {"materialIcon": {"name": "web"}},
                                            "text": "Citizens Advice",
                                        }
                                    },
                                    {
                                        "decoratedText": {
                                            "icon": {"materialIcon": {"name": "web"}},
                                            "text": "Advisernet",
                                        }
                                    },
                                    {
                                        "decoratedText": {
                                            "icon": {"materialIcon": {"name": "web"}},
                                            "text": "GOV.UK",
                                        }
                                    },
                                    {
                                        "textParagraph": {
                                            "text": "To get started you will need to register the advisers into your supervision space so their messages come to you."
                                        }
                                    },
                                    {
                                        "decoratedText": {
                                            "icon": {
                                                "materialIcon": {"name": "person_add"}
                                            },
                                            "topLabel": "Register an adviser",
                                            "text": "<b>/addUser</b>",
                                        }
                                    },
                                    {
                                        "decoratedText": {
                                            "icon": {"materialIcon": {"name": "help"}},
                                            "topLabel": "Other commands",
                                            "text": "<b>/help</b>",
                                        }
                                    },
                                ],
                            },
                            {
                                "widgets": [
                                    {
                                        "image": {
                                            "imageUrl": "https://ai.gov.uk/img/GovSupport1.webp",
                                            "altText": "GovSupport, an owl icon",
                                        }
                                    }
                                ]
                            },
                        ]
                    }
                }
            ]
        }
    ]
}

# --- Google Chat Dialogs --- #

SUCCESS_DIALOG = {
    "action_response": {
        "type": "DIALOG",
        "dialog_action": {"action_status": "OK"},
    }
}

ADD_USER_DIALOG = {
    "action_response": {
        "type": "DIALOG",
        "dialog_action": {
            "dialog": {
                "body": {
                    "sections": [
                        {
                            "header": "Onboard a new user to GovSupport",
                            "widgets": [
                                {
                                    "textParagraph": {
                                        "text": "To allow a new user to join GovSupport within your organisation register their email below and select their permissions"
                                    }
                                },
                                {
                                    "textInput": {
                                        "label": "Email",
                                        "type": "SINGLE_LINE",
                                        "name": "email",
                                    }
                                },
                                {
                                    "selectionInput": {
                                        "type": "RADIO_BUTTON",
                                        "label": "Role",
                                        "name": "role",
                                        "items": [
                                            {
                                                "text": "Adviser",
                                                "value": "Adviser",
                                                "selected": True,
                                            },
                                            {
                                                "text": "Supervisor",
                                                "value": "Supervisor",
                                                "selected": False,
                                            },
                                        ],
                                    }
                                },
                                {
                                    "buttonList": {
                                        "buttons": [
                                            {
                                                "text": "Add User",
                                                "onClick": {
                                                    "action": {
                                                        "function": "receiveDialog"
                                                    }
                                                },
                                            }
                                        ]
                                    },
                                    "horizontalAlignment": "END",
                                },
                            ],
                        }
                    ]
                }
            }
        },
    }
}

REMOVE_USER_DIALOG = {
    "action_response": {
        "type": "DIALOG",
        "dialog_action": {
            "dialog": {
                "body": {
                    "sections": [
                        {
                            "header": "Remove a user from GovSupport",
                            "widgets": [
                                {
                                    "textParagraph": {
                                        "text": "Input the email of the user whos access to GovSupport supervision within your organisation you would like to revoke"
                                    }
                                },
                                {
                                    "textInput": {
                                        "label": "Email",
                                        "type": "SINGLE_LINE",
                                        "name": "email",
                                    }
                                },
                                {
                                    "buttonList": {
                                        "buttons": [
                                            {
                                                "text": "Remove User",
                                                "onClick": {
                                                    "action": {
                                                        "function": "receiveDialog"
                                                    }
                                                },
                                            }
                                        ]
                                    },
                                    "horizontalAlignment": "END",
                                },
                            ],
                        }
                    ]
                }
            }
        },
    }
}

HELPER_DIALOG = {
    "action_response": {
        "type": "DIALOG",
        "dialog_action": {
            "dialog": {
                "body": {
                    "sections": [
                        {
                            "header": "Helper dialog for GovSupport Supervisor",
                            "widgets": [
                                {
                                    "textParagraph": {
                                        "text": "Adding a New User:\n\nTo add a new user under your supervision space, use the command /addUser.\nExample: /addUser\n\nRemoving User Access:\n\nIf you need to revoke access for a user, use the /removeUser command.\nExample: /removeUser\n\nListing Registered Users:\n\nTo view a list of users currently registered under your supervision, use the /listUsers command.\nThis command will display a comprehensive list, making it easy to manage and monitor user access.\nExample: /listUsers"
                                    }
                                }
                            ],
                        }
                    ]
                }
            }
        },
    }
}
