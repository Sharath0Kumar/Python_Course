def http_status_code(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown Status Code"
        

print(http_status_code(200))  # Output: OK
print(http_status_code(404))  # Output: Not Found
print(http_status_code(500))  # Output: Internal Server Error
print(http_status_code(123))  # Output: Unknown Status Code