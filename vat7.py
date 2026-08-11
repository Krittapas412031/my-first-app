def calculate_vat(price):
    vat = price * 0.07
    total_price = price + vat
    return vat, total_price

# ทดลองใช้งาน
if __name__ == "__main__":
    try:
        price_input = float(input("ป้อนราคาสินค้าก่อนรวม VAT (บาท): "))
        vat_amount, net_total = calculate_vat(price_input)
        
        print(f"ภาษีมูลค่าเพิ่ม (7%): {vat_amount:.2f} บาท")
        print(f"ราคาสินค้ารวม VAT ทั้งสิ้น: {net_total:.2f} บาท")
    except ValueError:
        print("กรุณากรอกตัวเลขเท่านั้น")
