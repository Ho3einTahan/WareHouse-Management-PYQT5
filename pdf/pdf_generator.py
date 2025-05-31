import pdfkit
import os
from di.injection import product_service

products=product_service.list_products()

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
    <h1>📄 گزارش کالا</h1>
    <table>
        <thead>
            <tr>
                <th>کد</th>
                <th>نام کالا</th>
                <th>تعداد</th>
                <th>قیمت خرید (تومان)</th>
                <th>قیمت فروش (تومان)</th>
                <th>توضیحات</th>
            </tr>
        </thead>
        <tbody>
"""

for product in products:
    html += f"""
        <tr>
            <td>{product.productCode}</td>
            <td>{product.productName}</td>
            <td>{product.inventory}</td>
            <td>{product.buyPrice}</td>
            <td>{product.sellPrice}</td>
            <td>{product.description}</td>
        </tr>
    """

html += f"""
        </tbody>
    </table>
</body>
</html>
"""

# You need to install wkhtmltopdf from https://wkhtmltopdf.org/downloads.html
config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

def generatePdf():
    pdfkit.from_string(html,"report.pdf",configuration=config)
    os.startfile("report.pdf")