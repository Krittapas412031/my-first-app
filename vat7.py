<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <title>โปรแกรมคำนวณราคารวม VAT 7%</title>
    <style>
        body { font-family: sans-serif; margin: 50px; background: #f4f4f9; }
        .card { background: white; padding: 20px; border-radius: 8px; max-width: 400px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        input, button { width: 100%; padding: 10px; margin-top: 10px; box-sizing: border-box; }
        button { background: #28a745; color: white; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background: #218838; }
        .result { margin-top: 15px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="card">
        <h2>คำนวณราคารวม VAT 7%</h2>
        <label>ราคาสินค้า (ยังไม่รวม VAT):</label>
        <input type="number" id="price" placeholder="ระบุจำนวนเงิน">
        <button onclick="calculateVat()">คำนวณ</button>
        <div class="result" id="output"></div>
    </div>

    <script>
        function calculateVat() {
            let price = parseFloat(document.getElementById('price').value);
            if (isNaN(price) || price <= 0) {
                document.getElementById('output').innerHTML = "กรุณากรอกตัวเลขที่ถูกต้อง";
                return;
            }
            let vat = price * 0.07;
            let total = price + vat;
            document.getElementById('output').innerHTML = 
                `VAT 7%: ${vat.toFixed(2)} บาท<br>ราคารวมสุทธิ: ${total.toFixed(2)} บาท`;
        }
    </script>
</body>
</html>
