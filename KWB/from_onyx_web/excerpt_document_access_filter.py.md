# Trimmed excerpt — Onyx document access filter (MIT path)

Source: https://raw.githubusercontent.com/onyx-dot-app/onyx/main/backend/onyx/db/document_access.py  
Upstream LICENSE: MIT Expat outside `ee/` (https://raw.githubusercontent.com/onyx-dot-app/onyx/main/LICENSE)  
Copyright (c) 2023-present DanswerAI, Inc.  
Fetched: 2026-09-19 — **trimmed for study**; imports / helpers omitted; do not run as package.

```python
def apply_document_access_filter(
    stmt: Select,
    user_email: str | None,
    external_group_ids: list[str],
    user_id: UUID | None = None,
    prior_emails: list[str] | None = None,
) -> Select:
    """Filter documents by source ACL or associated connector access."""
    # joins Document → DocumentByConnectorCredentialPair → ConnectorCredentialPair
    # ...
    access_filters: list[ColumnElement[bool]] = [
        ConnectorCredentialPair.access_type == AccessType.PUBLIC,
        Document.is_public.is_(True),
    ]
    if user_email:
        access_filters.append(any_(Document.external_user_emails) == user_email)
    if prior_emails:
        access_filters.append(
            Document.external_user_emails.overlap(
                cast(postgresql.array(prior_emails), postgresql.ARRAY(String))
            )
        )
    if external_group_ids:
        access_filters.append(
            Document.external_user_group_ids.overlap(
                cast(postgresql.array(external_group_ids), postgresql.ARRAY(String))
            )
        )
    if user_id:
        access_filters.append(build_user_cc_pair_access_filter(user_id))

    return stmt.where(or_(*access_filters))


def get_accessible_documents_by_ids(
    db_session: Session,
    document_ids: list[str],
    user_email: str | None,
    external_group_ids: list[str],
    user_id: UUID | None = None,
) -> list[Document]:
    """Return requested documents allowed by the retrieval-time access policy."""
    if not document_ids:
        return []
    stmt = select(Document).where(Document.id.in_(document_ids))
    stmt = apply_document_access_filter(
        stmt, user_email, external_group_ids, user_id=user_id
    )
    stmt = stmt.distinct()
    return list(db_session.execute(stmt).scalars().all())
```

**KWB takeaway:** re-filter by principal at retrieve time; never return unauthorized hit metadata.
