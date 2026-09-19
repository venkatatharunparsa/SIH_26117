# NOTES — Onyx (ACL before retrieve)

**Intent (REPO_PULL_MAP Wave 2):** Connector/ACL intent only. No Onyx fork. MOCK JSON schema.

## Product docs (access types)

From https://docs.onyx.app/admins/connectors/overview (fetched 2026-09-19):

| Access type | Meaning |
|---|---|
| **Private** | Creator (+ assigned users/groups) see connector data |
| **Public** | All Onyx users see connector data (warning: private source data becomes visible to all app users) |
| **Auto Sync Permissions** | Maintain source ACL; users only see docs they can access in source |

Permission-syncing connectors are documented as an **Enterprise Edition** feature — study the *intent*, do not vendor EE code.

## Retrieval-time filter (open MIT path)

`backend/onyx/db/document_access.py` (MIT portion of repo) applies SQL filters so a document is returned only if any of:

1. Connector-credential pair `access_type == PUBLIC`
2. `Document.is_public`
3. User email ∈ `Document.external_user_emails`
4. External group IDs overlap `Document.external_user_group_ids`
5. User has access via connector-credential pair membership

`get_accessible_documents_by_ids` re-checks IDs against that filter — **authz at retrieve**, not “login then all connectors.”

## KWB mapping (G6)

```text
grant scopes → filter corpus → retrieve → cite
              ↑ fail closed: no grant match ⇒ NOT FOUND (no ACL leak)
```

We already own grants; Onyx confirms the industry pattern of **ACL join before search results surface**.

## Do not take

Full Onyx indexing pipeline, EE permission sync, Onyx UI, cloud connectors.
