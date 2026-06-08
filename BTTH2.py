atm_vault_balance = 50_000_000
user_account_balance = 10_000_000


def display_balances():
    """
    Display current user account balance and ATM vault balance (for debugging).

    :return: None
    """
    print("--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND")


def deposit_money(amount):
    """
    Deposit money into user account and ATM vault.

    :param amount: amount of money to deposit (int)
    :return: True if deposit successful, False otherwise
    """
    global user_account_balance, atm_vault_balance

    if amount <= 0:
        print("Số tiền không hợp lệ")
        return False

    user_account_balance += amount
    atm_vault_balance += amount
    return True


def check_withdrawal_rules(amount):
    """
    Check all withdrawal conditions before executing transaction.

    Rules:
    - Amount must be positive
    - Amount must be multiple of 50,000
    - Account balance must be sufficient
    - ATM vault must have enough cash

    :param amount: withdrawal amount (int)
    :return: status string
    """
    fee = 1100
    total_deduction = amount + fee

    if amount <= 0:
        return "INVALID_AMOUNT"

    if amount % 50_000 != 0:
        return "NOT_MULTIPLE"

    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS"

    if amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH"

    return "OK"


def execute_withdrawal(amount):
    """
    Execute withdrawal by updating global balances.

    :param amount: amount of money to dispense (int)
    :return: None
    """
    global user_account_balance, atm_vault_balance

    fee = 1100
    total_deduction = amount + fee

    user_account_balance -= total_deduction
    atm_vault_balance -= amount

    print("Giao dịch đang xử lý...")
    print(f"Phí giao dịch: {fee:,} VND")
    print(f"Bạn đã rút thành công {amount:,} VND.")
    print(f"Số dư tài khoản còn lại: {user_account_balance:,} VND.")


def main():
    while True:
        print("\n============= SMART ATM =============")
        print("1. Xem số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Kết thúc giao dịch")
        print("=====================================")

        choice = input("Vui lòng chọn giao dịch (1-4): ")

        match choice:
            case "1":
                display_balances()

            case "2":
                print("--- NẠP TIỀN ---")
                try:
                    amount = int(input("Nhập số tiền muốn nạp: "))
                    if deposit_money(amount):
                        print(
                            f"Giao dịch thành công! "
                            f"Số dư tài khoản hiện tại: {user_account_balance:,} VND."
                        )
                except ValueError:
                    print("Số tiền không hợp lệ")

            case "3":
                print("--- RÚT TIỀN ---")
                try:
                    amount = int(input("Nhập số tiền cần rút: "))
                    status = check_withdrawal_rules(amount)

                    if status == "INVALID_AMOUNT":
                        print("Số tiền không hợp lệ")
                    elif status == "NOT_MULTIPLE":
                        print("Số tiền rút phải là bội số của 50,000")
                    elif status == "INSUFFICIENT_FUNDS":
                        print("Giao dịch thất bại: Số dư tài khoản không đủ.")
                    elif status == "ATM_OUT_OF_CASH":
                        print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ.")
                    elif status == "OK":
                        execute_withdrawal(amount)

                except ValueError:
                    print("Số tiền không hợp lệ")

            case "4":
                print("Cảm ơn quý khách đã sử dụng dịch vụ!")
                break

            case _:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


main()