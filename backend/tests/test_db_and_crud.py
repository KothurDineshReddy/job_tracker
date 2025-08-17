import pytest
from app.infra.db import init_db, upsert_application, list_applications
from app.domain.schemas import ApplicationIn

def test_db_init_and_upsert_then_list():
    # create tables
    init_db()

    # insert
    first = ApplicationIn(id="t1", status="Applied", source="upload", company="Acme", title="SWE")
    out1 = upsert_application(first)
    assert out1.id == "t1"
    assert out1.status == "Applied"

    # update same id
    updated = ApplicationIn(id="t1", status="Interview", source="upload")
    out2 = upsert_application(updated)
    assert out2.status == "Interview"

    # list + filter
    all_rows = list_applications()
    assert any(r.id == "t1" for r in all_rows)

    only_iv = list_applications(status="Interview")
    assert len(only_iv) >= 1 and all(r.status == "Interview" for r in only_iv)

    acme = list_applications(q="Acme")
    assert any(r.company == "Acme" for r in acme)