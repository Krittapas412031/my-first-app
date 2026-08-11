
    <title>โปรแกรมคำนวณราคารวม VAT 7%</title>
 
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
