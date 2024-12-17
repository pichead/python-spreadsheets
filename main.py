from config import ENV
import pandas as pd
import psycopg2
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from database import db

if __name__ == "__main__":


    data = db.evidenceReport.all()
    print(f"Total records: {len(data)}")
    
    result = []
    for evidenceReport, callcenter, fakeweb, account, reporter, sms in data:
        record = {
            "id": evidenceReport.id,
            "reportType": evidenceReport.reportType,
            "images": evidenceReport.images,
            "description": evidenceReport.description,
            "damageValue": float(evidenceReport.damageValue) if evidenceReport.damageValue else 0.0,
            "phoneNumber": callcenter.phoneNumber if callcenter and callcenter.phoneNumber else "N/A",
            "callTime": callcenter.callTime if callcenter and callcenter.callTime else "N/A",
            "suspiciousUrl": fakeweb.suspiciousUrl if fakeweb and fakeweb.suspiciousUrl else "N/A",
            "reporterUrl": fakeweb.reporterUrl if fakeweb and fakeweb.reporterUrl else "N/A",
            "bankName": account.bankName if account and account.bankName else "N/A",
            "accountNo": account.accountNo if account and account.accountNo else "N/A",
            "accountName": account.accountName if account and account.accountName else "N/A",
            "smsPhoneNumber": sms.smsPhoneNumber if sms and sms.smsPhoneNumber else "N/A",
            "smsUrl": sms.smsUrl if sms and sms.smsUrl else "N/A",
            "smsSenderName": sms.senderName if sms and sms.senderName else "N/A"
        }
        result.append(record)
        
    df = pd.DataFrame(result)

    # บันทึกเป็นไฟล์ Excel
    output_file = "evidence_reports.xlsx"
    df.to_excel(output_file, index=False, engine="openpyxl")

    print(f"Data has been written to {output_file}")

print("complete ...")

