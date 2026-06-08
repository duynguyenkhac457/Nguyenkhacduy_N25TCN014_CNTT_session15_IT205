yavailable_seats = 50
flight_revenue = 0.0

BASE_PRICE = 2000.0
MAX_CAPACITY = 50


def calculate_ticket_cost(quantity, ticket_class):
    """
    Calculate total ticket cost including service fee.

    :param quantity: number of tickets (int)
    :param ticket_class: 1 for Economy, 2 for Business (int)
    :return: final_total_cost (float)
    """
    if ticket_class == 1:
        unit_price = BASE_PRICE
        class_name = "Economy"
    elif ticket_class == 2:
        unit_price = BASE_PRICE * 1.5
        class_name = "Business"
    else:
        return None, None

    subtotal = unit_price * quantity
    service_fee = subtotal * 0.05
    final_total = subtotal + service_fee

    print("-> Xác nhận đặt chỗ:")
    print(f"Số lượng: {quantity} | Hạng: {class_name}")
    print(f"Tạm tính: ${subtotal}")
    print(f"Phí dịch vụ (5%): ${service_fee}")
    print(f"Tổng thanh toán: ${final_total}")

    return final_total, class_name


def process_booking(quantity, total_cost):
    """
    Process booking by updating seat availability and revenue.

    :param quantity: number of tickets (int)
    :param total_cost: total booking cost (float)
    :return: True if booking successful, False otherwise
    """
    global available_seats, flight_revenue

    if quantity > available_seats:
        print(f"Rất tiếc, chuyến bay chỉ còn {available_seats} chỗ trống.")
        return False

    available_seats -= quantity
    flight_revenue += total_cost
    print(f"Đặt vé thành công! Ghế trống còn lại: {available_seats}")
    return True


def cancel_tickets(quantity):
    """
    Cancel tickets and refund money based on refund policy.

    :param quantity: number of tickets to cancel (int)
    :return: refund_amount (float) or None if invalid
    """
    global available_seats, flight_revenue

    if quantity <= 0:
        print("Dữ liệu không hợp lệ.")
        return None

    if available_seats + quantity > MAX_CAPACITY:
        print("Lỗi: Số lượng vé hủy vượt quá số vé đã bán ra.")
        return None

    refund_per_ticket = BASE_PRICE * 0.8
    refund_amount = refund_per_ticket * quantity

    available_seats += quantity
    flight_revenue -= refund_amount

    return refund_amount


def print_flight_status():
    """
    Print current flight status report.

    Report format includes:
    - Maximum capacity
    - Booked seats
    - Available seats
    - Total revenue
    """
    booked_seats = MAX_CAPACITY - available_seats

    print("--- TÌNH TRẠNG CHUYẾN BAY VN2026 ---")
    print(f"Sức chứa tối đa: {MAX_CAPACITY}")
    print(f"Ghế đã đặt: {booked_seats}")
    print(f"Ghế trống: {available_seats}")
    print(f"Tổng doanh thu hiện tại: ${flight_revenue}")


def main():
    while True:
        print("\n============= SKYBOOKING SYSTEM =============")
        print("Chuyến bay: VN2026 | Khởi hành: Hà Nội")
        print("1. Đặt vé máy bay")
        print("2. Hủy vé & Hoàn tiền")
        print("3. Xem tình trạng chuyến bay")
        print("4. Đóng hệ thống")
        print("=============================================")

        choice = input("Chọn chức năng (1-4): ")

        match choice:
            case "1":
                print("--- ĐẶT VÉ MÁY BAY ---")
                try:
                    quantity = int(input("Nhập số lượng vé: "))
                    ticket_class = int(input("Chọn hạng vé (1: Economy, 2: Business): "))

                    if quantity <= 0:
                        print("Số lượng vé không hợp lệ.")
                        continue

                    total_cost, _ = calculate_ticket_cost(quantity, ticket_class)
                    if total_cost is None:
                        print("Hạng vé không hợp lệ.")
                        continue

                    process_booking(quantity, total_cost)

                except ValueError:
                    print("Dữ liệu nhập không hợp lệ.")

            case "2":
                print("--- HỦY VÉ & HOÀN TIỀN ---")
                try:
                    quantity = int(input("Nhập số lượng vé muốn hủy: "))
                    refund = cancel_tickets(quantity)
                    if refund is not None:
                        print(
                            f"Hủy vé thành công. "
                            f"Hệ thống đã hoàn lại: ${refund} (80% giá cơ bản)."
                        )
                        print(f"Ghế trống hiện tại: {available_seats}")
                except ValueError:
                    print("Dữ liệu nhập không hợp lệ.")

            case "3":
                print_flight_status()

            case "4":
                print("Hệ thống đã đóng. Cảm ơn quý khách!")
                break

            case _:
                print("Chức năng không hợp lệ. Vui lòng chọn lại.")


main()