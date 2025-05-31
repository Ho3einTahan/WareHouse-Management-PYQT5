import pdfkit
import os

orders = [
    {"name": "ماست کاله", "code": "PRD001", "desc": "ماست پرچرب 1 کیلوگرمی", "quantity": 3, "price": 90000},
    {"name": "دوغ آبعلی", "code": "PRD002", "desc": "دوغ گازدار 1.5 لیتری", "quantity": 2, "price": 60000},
    {"name": "پنیر صباح", "code": "PRD003", "desc": "پنیر سفید 400 گرمی", "quantity": 5, "price": 75000},
]

total_price = sum(item["quantity"] * item["price"] for item in orders)

html = f"""
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="UTF-8">
    <style>

        body {{
            direction: rtl;
            padding: 40px;
            line-height: 2;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        th, td {{
            border: 1px solid #000;
            padding: 8px;
            text-align: center;
        }}
        th {{
            background-color: #eee;
        }}
        h1 {{
            color: #444;
        }}
    </style>
</head>
<body>
    <h1>📄 گزارش سفارش کالا</h1>
    <table>
        <thead>
            <tr>
                <th>نام کالا</th>
                <th>کد</th>
                <th>توضیحات</th>
                <th>تعداد</th>
                <th>قیمت واحد (تومان)</th>
                <th>قیمت کل (تومان)</th>
            </tr>
        </thead>
        <tbody>
"""

for item in orders:
    total = item["quantity"] * item["price"]
    html += f"""
        <tr>
            <td>{item['name']}</td>
            <td>{item['code']}</td>
            <td>{item['desc']}</td>
            <td>{item['quantity']}</td>
            <td>{item['price']:,}</td>
            <td>{total:,}</td>
        </tr>
    """

html += f"""
        </tbody>
    </table>
    <h3>مبلغ کل سفارش‌ها: {total_price:,} تومان</h3>
</body>
</html>
"""

# You need to install wkhtmltopdf from https://wkhtmltopdf.org/downloads.html
config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

def generatePdf():
    pdfkit.from_string(html,"report.pdf",configuration=config)
    os.startfile("report.pdf")