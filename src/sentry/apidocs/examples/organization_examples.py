from drf_spectacular.utils import OpenApiExample

ORG_ROLE_LIST = [
    {
        "id": "billing",
        "name": "Billing",
        "desc": "Can manage subscription and billing details.",
        "scopes": ["org:billing"],
        "allowed": True,
        "isAllowed": True,
        "isRetired": False,
        "is_global": False,
        "isGlobal": False,
        "isTeamRolesAllowed": False,
        "minimumTeamRole": "contributor",
    },
    {
        "id": "member",
        "name": "Member",
        "desc": "Members can view and act on events, as well as view most other data within the organization.",
        "scopes": [
            "team:read",
            "project:releases",
            "org:read",
            "event:read",
            "alerts:write",
            "member:read",
            "alerts:read",
            "event:admin",
            "project:read",
            "event:write",
        ],
        "allowed": True,
        "isAllowed": True,
        "isRetired": False,
        "is_global": False,
        "isGlobal": False,
        "isTeamRolesAllowed": True,
        "minimumTeamRole": "contributor",
    },
    {
        "id": "admin",
        "name": "Admin",
        "desc": "Admin privileges on any teams of which they're a member. They can create new teams and projects, as well as remove teams and projects on which they already hold membership (or all teams, if open membership is enabled). Additionally, they can manage memberships of teams that they are members of. They cannot invite members to the organization.",
        "scopes": [
            "team:admin",
            "org:integrations",
            "project:admin",
            "team:read",
            "project:releases",
            "org:read",
            "team:write",
            "event:read",
            "alerts:write",
            "member:read",
            "alerts:read",
            "event:admin",
            "project:read",
            "event:write",
            "project:write",
        ],
        "allowed": True,
        "isAllowed": True,
        "isRetired": True,
        "is_global": False,
        "isGlobal": False,
        "isTeamRolesAllowed": True,
        "minimumTeamRole": "admin",
    },
    {
        "id": "manager",
        "name": "Manager",
        "desc": "Gains admin access on all teams as well as the ability to add and remove members.",
        "scopes": [
            "team:admin",
            "org:integrations",
            "project:releases",
            "team:write",
            "member:read",
            "org:write",
            "project:write",
            "project:admin",
            "team:read",
            "org:read",
            "event:read",
            "member:write",
            "alerts:write",
            "alerts:read",
            "event:admin",
            "project:read",
            "event:write",
            "member:admin",
        ],
        "allowed": True,
        "isAllowed": True,
        "isRetired": False,
        "is_global": True,
        "isGlobal": True,
        "isTeamRolesAllowed": True,
        "minimumTeamRole": "admin",
    },
    {
        "id": "owner",
        "name": "Owner",
        "desc": "Unrestricted access to the organization, its data, and its settings. Can add, modify, and delete projects and members, as well as make billing and plan changes.",
        "scopes": [
            "team:admin",
            "org:integrations",
            "project:releases",
            "org:admin",
            "team:write",
            "member:read",
            "org:write",
            "project:write",
            "project:admin",
            "team:read",
            "org:read",
            "event:read",
            "member:write",
            "alerts:write",
            "org:billing",
            "alerts:read",
            "event:admin",
            "project:read",
            "event:write",
            "member:admin",
        ],
        "allowed": True,
        "isAllowed": True,
        "isRetired": False,
        "is_global": True,
        "isGlobal": True,
        "isTeamRolesAllowed": True,
        "minimumTeamRole": "admin",
    },
]

TEAM_ROLE_LIST = [
    {
        "id": "contributor",
        "name": "Contributor",
        "desc": "Contributors can view and act on events, as well as view most other data within the team's projects.",
        "scopes": [
            "project:read",
            "project:releases",
            "member:read",
            "team:read",
            "event:read",
            "alerts:read",
            "event:write",
            "org:read",
        ],
        "allowed": False,
        "isAllowed": False,
        "isRetired": False,
        "isTeamRolesAllowed": True,
        "isMinimumRoleFor": None,
    },
    {
        "id": "admin",
        "name": "Team Admin",
        "desc": "Admin privileges on the team. They can create and remove projects, and can manage the team's memberships.",
        "scopes": [
            "project:read",
            "project:releases",
            "member:read",
            "event:admin",
            "team:write",
            "project:admin",
            "team:read",
            "org:integrations",
            "alerts:write",
            "team:admin",
            "project:write",
            "event:read",
            "alerts:read",
            "event:write",
            "org:read",
        ],
        "allowed": False,
        "isAllowed": False,
        "isRetired": False,
        "isTeamRolesAllowed": True,
        "isMinimumRoleFor": "admin",
    },
]


class OrganizationExamples:
    RETRIEVE_ORGANIZATION = [
        OpenApiExample(
            "Retrieve an organization",
            value={
                "avatar": {"avatarType": "letter_avatar", "avatarUuid": None},
                "dateCreated": "2018-11-06T21:19:55.101Z",
                "hasAuthProvider": False,
                "id": "2",
                "isEarlyAdopter": False,
                "links": {
                    "organizationUrl": "https://the-interstellar-jurisdiction.sentry.io",
                    "regionUrl": "https://us.sentry.io",
                },
                "name": "The Interstellar Jurisdiction",
                "require2FA": False,
                "slug": "the-interstellar-jurisdiction",
                "status": {"id": "active", "name": "active"},
            },
            status_codes=["200"],
            response_only=True,
        )
    ]

    UPDATE_ORGANIZATION = [
        OpenApiExample(
            "Update an organization",
            value={
                "id": "2",
                "slug": "the-interstellar-jurisdiction",
                "status": {"id": "active", "name": "active"},
                "name": "The Interstellar Jurisdiction",
                "dateCreated": "2018-11-06T21:19:55.101Z",
                "isEarlyAdopter": False,
                "require2FA": False,
                "requiresSso": False,
                "avatar": {"avatarType": "letter_avatar", "avatarUuid": None, "avatarUrl": None},
                "links": {
                    "organizationUrl": "https://the-interstellar-jurisdiction.sentry.io",
                    "regionUrl": "https://us.sentry.io",
                },
                "hasAuthProvider": False,
                "access": [
                    "org:integrations",
                    "member:admin",
                    "alerts:write",
                    "team:write",
                    "team:admin",
                    "project:write",
                    "org:read",
                    "member:write",
                    "project:read",
                    "member:read",
                    "event:admin",
                    "event:write",
                    "org:write",
                    "org:admin",
                    "project:releases",
                    "org:billing",
                    "project:admin",
                    "team:read",
                    "event:read",
                    "alerts:read",
                ],
                "onboardingTasks": [
                    {
                        "task": "create_project",
                        "status": "complete",
                        "user": {
                            "id": "1",
                            "name": "Stella R",
                            "username": "stella@the-interstellar-jurisdiction.io",
                            "email": "stella@the-interstellar-jurisdiction.io",
                            "avatarUrl": "https://gravatar.com/avatar/wufeousrfdiohfwea8sfhawesdhiu",
                            "isActive": True,
                            "hasPasswordAuth": True,
                            "isManaged": False,
                            "dateJoined": "2019-06-05T17:43:29.556793Z",
                            "lastLogin": "2019-06-25T13:53:44.524478Z",
                            "has2fa": False,
                            "lastActive": "2024-06-25T14:43:41.678886Z",
                            "isSuperuser": True,
                            "isStaff": False,
                            "experiments": {},
                            "emails": [
                                {
                                    "id": "1",
                                    "email": "stella@the-interstellar-jurisdiction.io",
                                    "is_verified": False,
                                }
                            ],
                            "avatar": {
                                "avatarType": "letter_avatar",
                                "avatarUuid": None,
                                "avatarUrl": None,
                            },
                        },
                        "completionSeen": None,
                        "dateCompleted": "2019-06-17T18:56:25.856360Z",
                        "data": {},
                    }
                ],
                "experiments": {},
                "isDefault": False,
                "defaultRole": "member",
                "orgRoleList": ORG_ROLE_LIST,
                "teamRoleList": TEAM_ROLE_LIST,
                "openMembership": True,
                "allowSharedIssues": True,
                "enhancedPrivacy": False,
                "dataScrubber": False,
                "dataScrubberDefaults": False,
                "sensitiveFields": [],
                "safeFields": [],
                "storeCrashReports": 0,
                "attachmentsRole": "member",
                "debugFilesRole": "admin",
                "eventsMemberAdmin": True,
                "alertsMemberWrite": True,
                "scrubIPAddresses": False,
                "scrapeJavaScript": True,
                "allowJoinRequests": True,
                "relayPiiConfig": None,
                "codecovAccess": False,
                "aiSuggestedSolution": True,
                "githubPRBot": True,
                "githubOpenPRBot": True,
                "githubNudgeInvite": True,
                "aggregatedDataConsent": False,
                "issueAlertsThreadFlag": True,
                "metricAlertsThreadFlag": True,
                "trustedRelays": [],
                "role": "owner",
                "orgRole": "owner",
                "pendingAccessRequests": 0,
                "isDynamicallySampled": False,
                "teams": [
                    {
                        "id": "1",
                        "slug": "my-team",
                        "name": "my-team",
                        "dateCreated": "2019-06-17T18:56:19.729172Z",
                        "isMember": True,
                        "teamRole": "admin",
                        "flags": {"idp:provisioned": False},
                        "access": [
                            "project:read",
                            "project:releases",
                            "member:read",
                            "event:admin",
                            "team:write",
                            "project:admin",
                            "team:read",
                            "org:integrations",
                            "alerts:write",
                            "team:admin",
                            "project:write",
                            "event:read",
                            "alerts:read",
                            "event:write",
                            "org:read",
                        ],
                        "hasAccess": True,
                        "isPending": False,
                        "memberCount": 1,
                        "avatar": {"avatarType": "letter_avatar", "avatarUuid": None},
                    }
                ],
                "projects": [
                    {
                        "team": {"id": "1", "slug": "my-team", "name": "my-team"},
                        "teams": [{"id": "1", "slug": "my-team", "name": "my-team"}],
                        "id": "1",
                        "name": "node",
                        "slug": "node",
                        "isBookmarked": False,
                        "isMember": True,
                        "access": [
                            "project:read",
                            "project:releases",
                            "member:read",
                            "event:admin",
                            "team:write",
                            "project:admin",
                            "team:read",
                            "org:integrations",
                            "alerts:write",
                            "team:admin",
                            "project:write",
                            "event:read",
                            "alerts:read",
                            "event:write",
                            "org:read",
                        ],
                        "hasAccess": True,
                        "dateCreated": "2019-06-17T18:56:25.777769Z",
                        "environments": [],
                        "eventProcessing": {"symbolicationDegraded": False},
                        "features": ["releases"],
                        "firstEvent": None,
                        "firstTransactionEvent": False,
                        "hasSessions": False,
                        "hasProfiles": False,
                        "hasReplays": False,
                        "hasFeedbacks": False,
                        "hasNewFeedbacks": False,
                        "hasCustomMetrics": False,
                        "hasMonitors": False,
                        "hasMinifiedStackTrace": False,
                        "hasInsightsHttp": True,
                        "hasInsightsDb": False,
                        "hasInsightsAssets": True,
                        "hasInsightsAppStart": False,
                        "hasInsightsScreenLoad": False,
                        "hasInsightsVitals": False,
                        "hasInsightsCaches": False,
                        "hasInsightsQueues": False,
                        "hasInsightsLlmMonitoring": False,
                        "platform": "node",
                        "platforms": [],
                        "latestRelease": None,
                        "hasUserReports": False,
                        "latestDeploys": None,
                    }
                ],
            },
            status_codes=["200"],
            response_only=True,
        )
    ]

    LIST_ORGANIZATIONS = [
        OpenApiExample(
            "List your organizations",
            value=[
                {
                    "avatar": {"avatarType": "letter_avatar", "avatarUuid": None},
                    "dateCreated": "2018-11-06T21:19:55.101Z",
                    "features": [
                        "session-replay-video",
                        "onboarding",
                        "advanced-search",
                        "monitor-seat-billing",
                        "issue-platform",
                    ],
                    "hasAuthProvider": False,
                    "id": "2",
                    "isEarlyAdopter": False,
                    "links": {
                        "organizationUrl": "https://the-interstellar-jurisdiction.sentry.io",
                        "regionUrl": "https://us.sentry.io",
                    },
                    "name": "The Interstellar Jurisdiction",
                    "require2FA": False,
                    "slug": "the-interstellar-jurisdiction",
                    "status": {"id": "active", "name": "active"},
                }
            ],
            status_codes=["200"],
            response_only=True,
        )
    ]

    LIST_PROJECTS = [
        OpenApiExample(
            "List an organization's projects",
            value=[
                {
                    "slug": "prime-mover",
                    "name": "Prime Mover",
                    "dateCreated": "2018-11-06T21:19:58.536Z",
                    "firstEvent": None,
                    "access": [],
                    "hasAccess": True,
                    "id": "3",
                    "isBookmarked": False,
                    "isMember": True,
                    "platform": "",
                    "platforms": [],
                    "team": {
                        "id": "2",
                        "name": "Powerful Abolitionist",
                        "slug": "powerful-abolitionist",
                    },
                    "teams": [
                        {
                            "id": "2",
                            "name": "Powerful Abolitionist",
                            "slug": "powerful-abolitionist",
                        }
                    ],
                    "environments": ["local"],
                    "eventProcessing": {"symbolicationDegraded": False},
                    "features": ["releases"],
                    "firstTransactionEvent": True,
                    "hasSessions": True,
                    "hasProfiles": True,
                    "hasReplays": True,
                    "hasMinifiedStackTrace": False,
                    "hasMonitors": True,
                    "hasFeedbacks": False,
                    "hasNewFeedbacks": False,
                    "hasCustomMetrics": False,
                    "hasUserReports": False,
                    "hasInsightsHttp": True,
                    "hasInsightsDb": False,
                    "hasInsightsAssets": True,
                    "hasInsightsAppStart": False,
                    "hasInsightsScreenLoad": False,
                    "hasInsightsVitals": False,
                    "hasInsightsCaches": False,
                    "hasInsightsQueues": False,
                    "hasInsightsLlmMonitoring": False,
                    "latestRelease": None,
                }
            ],
            status_codes=["200"],
            response_only=True,
        )
    ]

    RETRIEVE_EVENT_COUNTS_V2 = [
        OpenApiExample(
            "Retrieve event counts v2",
            value={
                "start": "2022-02-14T19:00:00Z",
                "end": "2022-02-28T18:03:00Z",
                "intervals": ["2022-02-28T00:00:00Z"],
                "groups": [
                    {
                        "by": {"outcome": "invalid"},
                        "totals": {"sum(quantity)": 165665},
                        "series": {"sum(quantity)": [165665]},
                    }
                ],
            },
            status_codes=["200"],
            response_only=True,
        ),
    ]

    RETRIEVE_SUMMARY_EVENT_COUNT = [
        OpenApiExample(
            "Get event counts for projects in an organization",
            value={
                "start": "2023-09-19T13:00:00Z",
                "end": "2023-09-19T12:28:00Z",
                "projects": [
                    {
                        "id": "1",
                        "slug": "android-project",
                        "stats": [
                            {
                                "category": "error",
                                "outcomes": {
                                    "accepted": 1930571,
                                    "filtered": 1934881,
                                    "rate_limited": 2506132,
                                    "invalid": 0,
                                    "abuse": 1938113,
                                    "client_discard": 1942414,
                                    "cardinality_limited": 0,
                                },
                                "totals": {"dropped": 2506132, "sum(quantity)": 10252111},
                            },
                            {
                                "category": "transaction",
                                "outcomes": {
                                    "accepted": 1909849,
                                    "filtered": 1947142,
                                    "rate_limited": 2458946,
                                    "invalid": 0,
                                    "abuse": 1927179,
                                    "client_discard": 1931595,
                                    "cardinality_limited": 0,
                                },
                                "totals": {"dropped": 2458946, "sum(quantity)": 10174711},
                            },
                        ],
                    },
                ],
            },
            status_codes=["200"],
            response_only=True,
        )
    ]

    UPDATE_ORG_MEMBER = [
        OpenApiExample(
            "Update organization member",
            value={
                "id": "57377908164",
                "email": "sirpenguin@antarcticarocks.com",
                "name": "Sir Penguin",
                "user": {
                    "id": "280094367316",
                    "name": "Sir Penguin",
                    "username": "sirpenguin@antarcticarocks.com",
                    "email": "sirpenguin@antarcticarocks.com",
                    "avatarUrl": "https://secure.gravatar.com/avatar/16aeb26c5fdba335c7078e9e9ddb5149?s=32&d=mm",
                    "isActive": True,
                    "hasPasswordAuth": True,
                    "isManaged": False,
                    "dateJoined": "2021-07-06T21:13:58.375239Z",
                    "lastLogin": "2021-08-02T18:25:00.051182Z",
                    "has2fa": False,
                    "lastActive": "2021-08-02T21:32:18.836829Z",
                    "isSuperuser": False,
                    "isStaff": False,
                    "experiments": {},
                    "emails": [
                        {
                            "id": "2153450836",
                            "email": "sirpenguin@antarcticarocks.com",
                            "is_verified": True,
                        }
                    ],
                    "avatar": {"avatarType": "letter_avatar", "avatarUuid": None},
                    "authenticators": [],
                    "canReset2fa": True,
                },
                "role": "member",
                "orgRole": "member",
                "roleName": "Member",
                "pending": False,
                "expired": False,
                "flags": {
                    "idp:provisioned": False,
                    "idp:role-restricted": False,
                    "sso:linked": False,
                    "sso:invalid": False,
                    "member-limit:restricted": False,
                    "partnership:restricted": False,
                },
                "dateCreated": "2021-07-06T21:13:01.120263Z",
                "inviteStatus": "approved",
                "inviterName": "maininviter@antarcticarocks.com",
                "teams": ["cool-team", "ancient-gabelers"],
                "teamRoles": [
                    {"teamSlug": "ancient-gabelers", "role": "admin"},
                    {"teamSlug": "powerful-abolitionist", "role": "contributor"},
                ],
                "invite_link": None,
                "isOnlyOwner": False,
                "orgRoleList": ORG_ROLE_LIST,
                "teamRoleList": TEAM_ROLE_LIST,
            },
            status_codes=["200"],
            response_only=True,
        )
    ]

    LIST_RELAYS = [
        OpenApiExample(
            "List an organization's trusted relays",
            value=[
                {
                    "relayId": "0123abcd-4567-efgh-ij89-012aaa456bbb",
                    "version": "23.11.2",
                    "firstSeen": "2023-12-10T00:00:00.000000Z",
                    "lastSeen": "2023-12-20T22:22:22.222222Z",
                    "publicKey": "asdfa54g9987ga9dfha0f8adfhkj324-dafd78321-I",
                }
            ],
            status_codes=["200"],
            response_only=True,
        ),
    ]

    RELEASE_DETAILS = [
        OpenApiExample(
            "Retrieve release details",
            value={
                "id": 1122684517,
                "version": "control@abc123",
                "status": "open",
                "shortVersion": "control@abc123",
                "versionInfo": {
                    "package": "control",
                    "version": {"raw": "abc123"},
                    "description": "abc123",
                    "buildHash": "abc123",
                },
                "ref": None,
                "url": None,
                "dateReleased": None,
                "dateCreated": "2024-05-21T11:26:16.190281Z",
                "data": {},
                "newGroups": 0,
                "owner": None,
                "commitCount": 2,
                "lastCommit": {
                    "id": "xyz123",
                    "message": "feat(raspberries): Made raspberries even more delicious",
                    "dateCreated": "2024-05-21T11:04:55Z",
                    "pullRequest": {
                        "id": "70214",
                        "title": "feat(raspberries): Made raspberries even more delicious",
                        "message": "Made raspberries even more delicious",
                        "dateCreated": "2024-05-03T07:32:28.205043Z",
                        "repository": {
                            "id": "1",
                            "name": "raj/raspberries",
                            "url": "https://raspberries.raspberries/raj/raspberries",
                            "provider": {"id": "integrations:github", "name": "GitHub"},
                            "status": "active",
                            "dateCreated": "2016-10-10T21:36:42.414678Z",
                            "integrationId": "2933",
                            "externalSlug": "raj/raspberries",
                            "externalId": "873328",
                        },
                        "author": {
                            "id": "2837091",
                            "name": "Raj's Raspberries",
                            "username": "rajraspberry",
                            "avatarUrl": "https://gravatar.com/avatar/bf99685de539465db9208ab3a888843ba0e5e85b1f156084484c7c6c31312be5?s=32&d=mm",
                            "isActive": True,
                            "hasPasswordAuth": False,
                            "isManaged": False,
                            "dateJoined": "2023-08-07T12:32:09.091427Z",
                            "lastLogin": "2024-05-21T05:46:23.824074Z",
                            "has2fa": True,
                            "lastActive": "2024-05-21T13:59:10.614891Z",
                            "isSuperuser": True,
                            "isStaff": True,
                            "experiments": {},
                            "emails": [
                                {
                                    "id": "2972219",
                                    "email": "raj@raspberries",
                                    "is_verified": True,
                                }
                            ],
                            "avatar": {
                                "avatarType": "upload",
                                "avatarUuid": "xyz123",
                                "avatarUrl": "https://sentry.io/avatar/xyz123/",
                            },
                        },
                        "externalUrl": "https://github.com/raj/raspberries/pull/70214",
                    },
                    "suspectCommitType": "",
                    "repository": {
                        "id": "1",
                        "name": "raj/raspberries",
                        "url": "https://github.com/raj/raspberries",
                        "provider": {"id": "integrations:github", "name": "GitHub"},
                        "status": "active",
                        "dateCreated": "2016-10-10T21:36:42.414678Z",
                        "integrationId": "2933",
                        "externalSlug": "raj/raspberries",
                        "externalId": "873328",
                    },
                    "author": {
                        "id": "2837091",
                        "name": "Raj's Raspberries",
                        "username": "rajraspberry",
                        "avatarUrl": "https://gravatar.com/avatar/bf99685de539465db9208ab3a888843ba0e5e85b1f156084484c7c6c31312be5?s=32&d=mm",
                        "isActive": True,
                        "hasPasswordAuth": False,
                        "isManaged": False,
                        "dateJoined": "2023-08-07T12:32:09.091427Z",
                        "lastLogin": "2024-05-21T05:46:23.824074Z",
                        "has2fa": True,
                        "lastActive": "2024-05-21T13:59:10.614891Z",
                        "isSuperuser": True,
                        "isStaff": True,
                        "experiments": {},
                        "emails": [
                            {"id": "2972219", "email": "raj@raspberries", "is_verified": True}
                        ],
                        "avatar": {
                            "avatarType": "upload",
                            "avatarUuid": "xyz123",
                            "avatarUrl": "https://sentry.io/avatar/xyz123/",
                        },
                    },
                    "releases": [
                        {
                            "version": "control@abc123",
                            "shortVersion": "control@abc123",
                            "ref": None,
                            "url": None,
                            "dateReleased": None,
                            "dateCreated": "2024-05-21T11:26:16.190281Z",
                        },
                        {
                            "version": "backend@abc123",
                            "shortVersion": "backend@abc123",
                            "ref": None,
                            "url": None,
                            "dateReleased": None,
                            "dateCreated": "2024-05-21T11:56:36.790866Z",
                        },
                        {
                            "version": "control@def789",
                            "shortVersion": "control@def789",
                            "ref": None,
                            "url": None,
                            "dateReleased": None,
                            "dateCreated": "2024-05-21T12:44:25.923663Z",
                        },
                        {
                            "version": "frontend@ghi012",
                            "shortVersion": "frontend@ghi012",
                            "ref": None,
                            "url": None,
                            "dateReleased": None,
                            "dateCreated": "2024-05-21T12:46:42.338358Z",
                        },
                    ],
                },
                "deployCount": 1,
                "lastDeploy": {
                    "id": 53070941,
                    "environment": "canary-test-control",
                    "dateStarted": None,
                    "dateFinished": "2024-05-21T11:26:17.597793Z",
                    "name": "control@abc123 to canary-test-",
                    "url": None,
                },
                "authors": [
                    {
                        "id": 2837091,
                        "name": "Raj's Raspberries",
                        "username": "rajraspberry",
                        "email": "raj@raspberries",
                        "avatarUrl": "https://gravatar.com/avatar/bf99685de539465db9208ab3a888843ba0e5e85b1f156084484c7c6c31312be5?s=32&d=mm",
                        "isActive": True,
                        "hasPasswordAuth": False,
                        "isManaged": False,
                        "dateJoined": "2023-08-07T12:32:09.091427Z",
                        "lastLogin": "2024-05-21T05:46:23.824074Z",
                        "has2fa": True,
                        "lastActive": "2024-05-21T13:59:10.614891Z",
                        "isSuperuser": True,
                        "isStaff": True,
                        "experiments": {},
                        "emails": [
                            {"id": "2972219", "email": "raj@raspberries", "is_verified": True}
                        ],
                        "avatar": {
                            "avatarType": "upload",
                            "avatarUuid": "xyz123",
                            "avatarUrl": "https://sentry.io/avatar/xyz123/",
                        },
                    }
                ],
                "projects": [
                    {
                        "id": 1,
                        "slug": "sentry",
                        "name": "Backend",
                        "newGroups": 0,
                        "platform": "python",
                        "platforms": ["native", "other", "python"],
                        "hasHealthData": False,
                        "healthData": {
                            "durationP50": None,
                            "durationP90": None,
                            "crashFreeUsers": None,
                            "crashFreeSessions": None,
                            "sessionsCrashed": 0,
                            "sessionsErrored": 0,
                            "totalUsers": None,
                            "totalUsers24h": None,
                            "totalProjectUsers24h": None,
                            "totalSessions": None,
                            "totalSessions24h": None,
                            "totalProjectSessions24h": None,
                            "adoption": None,
                            "sessionsAdoption": None,
                            "stats": {
                                "24h": [
                                    [1715126400, 0],
                                    [1715212800, 0],
                                    [1715299200, 0],
                                    [1715385600, 0],
                                    [1715472000, 0],
                                    [1715558400, 0],
                                    [1715644800, 0],
                                    [1715731200, 0],
                                    [1715817600, 0],
                                    [1715904000, 0],
                                    [1715990400, 0],
                                    [1716076800, 0],
                                    [1716163200, 0],
                                    [1716249600, 0],
                                ]
                            },
                            "hasHealthData": False,
                        },
                    }
                ],
                "firstEvent": None,
                "lastEvent": None,
                "currentProjectMeta": {},
                "userAgent": "Python-urllib/3.11",
                "adoptionStages": {
                    "sentry": {"stage": "low_adoption", "adopted": None, "unadopted": None}
                },
            },
            status_codes=["200"],
            response_only=True,
        )
    ]

    GET_HISTORICAL_ANOMALIES = [
        OpenApiExample(
            "Identify anomalies in historical data",
            value=[
                {
                    "anomaly": {
                        "anomaly_score": -0.38810767243044786,
                        "anomaly_type": "none",
                    },
                    "timestamp": 169,
                    "value": 0.048480431,
                },
                {
                    "anomaly": {
                        "anomaly_score": -0.3890542800124323,
                        "anomaly_type": "none",
                    },
                    "timestamp": 170,
                    "value": 0.047910238,
                },
            ],
        )
    ]
