def is_happy_ticket(ticket_number):
    half_length = len(ticket_number) // 2
    first_half_sum = sum(map(int, ticket_number[:half_length]))
    second_half_sum = sum(map(int, ticket_number[half_length:]))

    return first_half_sum == second_half_sum

# Примеры использования:
ticket_number = input("Введите шестизначный номер: ")
print(is_happy_ticket(ticket_number))