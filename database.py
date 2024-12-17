from config import ENV
import pandas as pd
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import declarative_base, sessionmaker,DeclarativeBase,Session
from sqlalchemy import select
from sqlalchemy.ext.automap import automap_base

DATABASE_URL = "postgresql://root:mypassword@127.0.0.1:5432/mydb"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# 3. สร้าง Automap Base สำหรับ Table ที่มีอยู่แล้ว
Base = automap_base()
Base.prepare(autoload_with=engine)


class db:
    
    tb_watchlist = Base.classes.watchlist
    tb_evidenceReport = Base.classes.evidence_report
    tb_callcenterReport = Base.classes.CallCenterReport
    tb_fakewebsiteReport = Base.classes.FakeWebsiteReport
    tb_suspiciousAccountReport = Base.classes.SuspiciousAccountReport
    tb_reporterInfo = Base.classes.ReporterInfo
    tb_fakeSmsReport = Base.classes.FakeSmsReport

    
    watchlist = session.query(tb_watchlist)
    evidenceReport = (
    session.query(
        tb_evidenceReport,
        tb_callcenterReport,
        tb_fakewebsiteReport,
        tb_suspiciousAccountReport,
        tb_reporterInfo,
        tb_fakeSmsReport
    )
    .outerjoin(tb_callcenterReport, tb_callcenterReport.reportId == tb_evidenceReport.id)
    .outerjoin(tb_fakewebsiteReport, tb_fakewebsiteReport.reportId == tb_evidenceReport.id)
    .outerjoin(tb_suspiciousAccountReport, tb_suspiciousAccountReport.reportId == tb_evidenceReport.id)
    .outerjoin(tb_reporterInfo, tb_reporterInfo.reportId == tb_evidenceReport.id)
    .outerjoin(tb_fakeSmsReport, tb_fakeSmsReport.reportId == tb_evidenceReport.id)
)
# 4. Map Table ที่มีอยู่แล้วในฐานข้อมูล
# ตรวจสอบชื่อ Table ทั้งหมด


