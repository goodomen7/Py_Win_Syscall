import ssl



context = ssl.create_default_context()

test_time = "May  9 00:00:00 2023 GMT"
result = ssl.cert_time_to_seconds(test_time)

host = "www.python.org"
port = 443
cert = ssl.get_server_certificate((host, port))

certs = ssl.enum_certificates("ROOT")
crls = ssl.enum_crls("ROOT")