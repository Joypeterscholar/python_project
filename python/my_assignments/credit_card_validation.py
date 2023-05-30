card_number = input("Hello, Kindly Enter Card details to verify: ")
length_of_card_is_invalid = len(card_number) < 13 or len(card_number) > 16
if length_of_card_is_invalid:
    print(TypeError("Invalid card number"))
card_type = ''
match card_number[0]:
    case "4":
        card_type = "Visa"
    case "5":
        card_type = "MasterCard"
    case "37":
        card_type = "American Expresss"
    case "6":
        card_type = "Discover"

sum = 0
double_digits = False

index = len(card_number) - 2
digit = 0
while index >= 0:
    digit = int(card_number[index]) * 2
    if digit > 9:
        digit %= 10 + digit/10
        card_number[index] = str(digit)
    sum += digit
    double_digits = not double_digits
    index -= 1
card_validity = ''
if sum % 10 == 0:
    card_validity = "Valid"
else:
    card_validity = "Invalid"
print(f"**Credit Card Type: {card_type}")
print(f"**Card Number: {card_number}")
print(f"Credit Card Digit Length: {len(card_number)}")
print(f"**Credit Card Validity Status: {card_validity}")

        # int sum = 0;
        # boolean doubleDigits = false;
        #
        # for (int index = cardNum.length - 2; index >= 0; index--) {
        #     int digit = Integer.parseInt(cardNum[index]) * 2;
        #     if (digit > 9){
        #         digit %= 10 + digit/10;
        #         cardNum[index] = String.valueOf(digit);
        #     }
        #     sum += digit;
        #     doubleDigits = !doubleDigits;
        # }
        # String cardValidity = "";
        # if (sum % 10 == 0) cardValidity = "Valid";
        # else cardValidity = "Invalid";
        #
        # System.out.printf("**Credit Card Type: %s%n", cardType);
        # System.out.printf("**Credit Card Number: %s%n", cardNumber);
        # System.out.printf("**Credit Card Digit Length: %d%n", cardNum.length);
        # System.out.printf("**Credit Card Validity Status: %s%n", cardValidity);


