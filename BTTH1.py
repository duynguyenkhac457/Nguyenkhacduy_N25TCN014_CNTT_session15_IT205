inventory_stock = 100
total_revenue = 0.0


def add_stock(amount):
    """
    Add more products to inventory stock.

    :param amount: number of products to add (int)
    :return: None
    """
    global inventory_stock
    inventory_stock += amount


def process_sale(quantity):
    """
    Check if inventory has enough products for selling.

    :param quantity: number of products customer wants to buy (int)
    :return: True if enough stock, False otherwise
    """
    global inventory_stock

    if quantity > inventory_stock:
        print(
            f"Lỗi: Không đủ hàng trong kho. "
            f"Tồn kho hiện tại chỉ còn {inventory_stock}."
        )
        return False
    return True


def calculate_final_price(quantity, price):
    """
    Calculate final price after discount and VAT.

    Discount rule:
    - 10% discount if subtotal >= 1000
    VAT:
    - 8% VAT after discount

    :param quantity: quantity of products (int)
    :param price: unit price (float)
    :return: final_total (float)
    """
    subtotal = quantity * price
    discount = 0.0

    if subtotal >= 1000:
        discount = subtotal * 0.10

    after_discount = subtotal - discount
    vat = after_discount * 0.08
    final_total = after_discount + vat

    print("-> Hóa đơn chi tiết:")
    print(f"Số lượng: {quantity} | Đơn giá: ${price}")
    print(f"Tạm tính: ${subtotal}")
    print(f"Giảm giá (10%): ${discount}")
    print(f"Thuế VAT (8%): ${vat}")
    print(f"Tổng thanh toán: ${final_total}")

    return final_total


def print_report():
    """
    Print business report including inventory and total revenue.

    :return: None
    """
    print("--- BÁO CÁO KINH DOANH ---")
    print(f"Tồn kho hiện tại: {inventory_stock} sản phẩm")
    print(f"Tổng doanh thu: ${total_revenue}")


def main():
    global inventory_stock, total_revenue

    while True:
        print("\n========== TECHSTORE MANAGEMENT SYSTEM ==========")
        print("1. Nhập thêm hàng vào kho")
        print("2. Bán hàng (Tính toán hóa đơn)")
        print("3. Xem báo cáo tổng quan")
        print("4. Thoát chương trình")
        print("=================================================")

        choice = input("Chọn chức năng (1-4): ")

        match choice:
            case "1":
                print("--- NHẬP HÀNG ---")
                try:
                    amount = int(input("Nhập số lượng sản phẩm muốn thêm: "))
                    if amount <= 0:
                        print("Dữ liệu nhập vào phải lớn hơn 0.")
                        continue

                    add_stock(amount)
                    print(f"Đã nhập thành công {amount} sản phẩm.")
                    print(f"Tồn kho hiện tại: {inventory_stock}")

                except ValueError:
                    print("Lỗi: Vui lòng nhập số hợp lệ.")

            case "2":
                print("--- BÁN HÀNG ---")
                try:
                    quantity = int(input("Nhập số lượng mua: "))
                    price = float(input("Nhập đơn giá ($): "))

                    if quantity <= 0 or price <= 0:
                        print("Dữ liệu nhập vào phải lớn hơn 0.")
                        continue

                    if not process_sale(quantity):
                        continue

                    final_total = calculate_final_price(quantity, price)

                    inventory_stock -= quantity
                    total_revenue += final_total

                    print("Đã bán thành công!")

                except ValueError:
                    print("Lỗi: Vui lòng nhập đúng kiểu dữ liệu.")

            case "3":
                print_report()

            case "4":
                print("Đã thoát chương trình.")
                break

            case _:
                print("Chức năng không hợp lệ. Vui lòng chọn lại.")


main()