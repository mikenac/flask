import unittest
from jwt_authenticator.authentication_handler import AuthenticationHandler


class TestHelloApp(unittest.TestCase):
    """ Test fixture for application unit tests"""

    def test_generate_and_validate_token(self):
        """ Generate and decode a token"""

        audience = 'http://www.service.teletracking.com/'
        roles = {'role': ['admin', 'user'], 'audience': audience}
        secret = 'drMemxWrLen6fCXQA5jO6gXkK/UoZVzPGRDiff7ByPU='
        token = AuthenticationHandler.generate_auth_token(roles, secret)
        decoded_token = AuthenticationHandler.validate_and_decode_token(
            token=token, key=secret,
            audience=audience
        )
        self.assertTrue(decoded_token['role'][0] == 'admin')
        self.assertTrue(decoded_token['role'][1] == 'user')

    def test_decode_IQ_token(self):
        """Decode a token created by IQ"""

        token = """eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYW1laWQiOiJhZGZzfHNodzAwMXNhaW50ZWxzZXdoZXJlfGpwX2FkbWluQHVybjphdXRoMDpzYWludGVsc2V3aGVyZSIsImVtYWlsIjoiSmFpbWluLlBhdGVsODMrNTE2NDU2QGdtYWlsLmNvbSIsInVuaXF1ZV9uYW1lIjoiSVFHRU5IT1NQXFxiXy1kcHl4eDBFeVVjR0pIaG1aOCIsImh0dHBzOi8vdGVsZXRyYWNraW5nLmNsb3VkYXBwLm5ldC9pZGVudGl0eS9jbGFpbXMvYWR1c2VyZ3VpZCI6IjMveFFhZ0VrSWttcllBU0VQZHVZRmc9PSIsImh0dHBzOi8vdGVsZXRyYWNraW5nLmNsb3VkYXBwLm5ldC9pZGVudGl0eS9jbGFpbXMvZmlyc3RuYW1lIjoiQWRtaW4iLCJodHRwczovL3RlbGV0cmFja2luZy5jbG91ZGFwcC5uZXQvaWRlbnRpdHkvY2xhaW1zL2xhc3RuYW1lIjoiVGVzdCIsImh0dHBzOi8vdGVsZXRyYWNraW5nLmNsb3VkYXBwLm5ldC9pZGVudGl0eS9jbGFpbXMvb3VuYW1lIjoiU2FpbnRFbHNld2hlcmUiLCJyb2xlIjpbIkRvbWFpbiBVc2VycyIsIkFkbWluaXN0cmF0b3IiLCJJUUdlbkhvc3BTZWMiLCJTYWludEVsc2V3aGVyZSJdLCJ1cG4iOiJKYWltaW4uUGF0ZWw4Mys1MTY0NTZAZ21haWwuY29tIiwiaHR0cDovL3NjaGVtYXMuYXV0aDAuY29tL2lkZW50aXRpZXMvZGVmYXVsdC9wcm92aWRlciI6ImFkZnMiLCJodHRwOi8vc2NoZW1hcy5hdXRoMC5jb20vaWRlbnRpdGllcy9kZWZhdWx0L2Nvbm5lY3Rpb24iOiJzaHcwMDFzYWludGVsc2V3aGVyZSIsImh0dHA6Ly9zY2hlbWFzLmF1dGgwLmNvbS9pZGVudGl0aWVzL2RlZmF1bHQvaXNTb2NpYWwiOiJmYWxzZSIsImh0dHA6Ly9zY2hlbWFzLmF1dGgwLmNvbS9naXZlbl9uYW1lIjoiSVFHRU5IT1NQXFxiXy1kcHl4eDBFeVVjR0pIaG1aOCIsImh0dHA6Ly9zY2hlbWFzLmF1dGgwLmNvbS9waWN0dXJlIjoiaHR0cHM6Ly9zLmdyYXZhdGFyLmNvbS9hdmF0YXIvMzUxYTRiMjU4NWViM2UyYjA1NWI4ZTAyOGY4NzdmNDc_cz00ODBcdTAwMjZyPXBnXHUwMDI2ZD1odHRwcyUzQSUyRiUyRmNkbi5hdXRoMC5jb20lMkZhdmF0YXJzJTJGaXEucG5nIiwiaHR0cDovL3NjaGVtYXMuYXV0aDAuY29tL25pY2tuYW1lIjoiSmFpbWluLlBhdGVsODMrNTE2NDU2IiwiaHR0cDovL3NjaGVtYXMuYXV0aDAuY29tL2VtYWlsX3ZlcmlmaWVkIjoidHJ1ZSIsImh0dHA6Ly9zY2hlbWFzLmF1dGgwLmNvbS9jbGllbnRJRCI6Imtrakgxd3AzdE53RmpEN0M1djI3a0oyWHFWUHE1akhtIiwiaHR0cDovL3NjaGVtYXMuYXV0aDAuY29tL3VwZGF0ZWRfYXQiOiJNb24gSmFuIDE0IDIwMTkgMTU6NTY6MTIgR01UKzAwMDAgKFVUQykiLCJodHRwOi8vc2NoZW1hcy5hdXRoMC5jb20vY3JlYXRlZF9hdCI6IkZyaSBKYW4gMTEgMjAxOSAyMDoxNToyMiBHTVQrMDAwMCAoVVRDKSIsImF1dGhtZXRob2QiOiJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvYXV0aGVudGljYXRpb25tZXRob2QvcGFzc3dvcmQiLCJhdXRoX3RpbWUiOiIyMDE5LTAxLTE0VDIzOjU2OjEyLjg1M1oiLCJodHRwczovL3RlbGV0cmFja2luZy5jbG91ZGFwcC5uZXQvaWRlbnRpdHkvY2xhaW1zL3RlbmFudGlkIjoiMjExNmU5NDMtNTA5NC00MWY3LTgzMTgtODNhYWMyYWMxMTQ3IiwiaHR0cHM6Ly90ZWxldHJhY2tpbmcuY2xvdWRhcHAubmV0L2lkZW50aXR5L2NsYWltcy9jb250ZXh0cGVyc29uaWQiOiIwYTAxMjBhMS04NTU3LTQ4MzEtYTQyNi1hOGJkMDBmNjFkYzkiLCJodHRwczovL3RlbGV0cmFja2luZy5jbG91ZGFwcC5uZXQvaWRlbnRpdHkvY2xhaW1zL3VzZXJuYW1lZm9ybWFsIjoiVGVzdCwgQWRtaW4iLCJodHRwczovL3RlbGV0cmFja2luZy5jbG91ZGFwcC5uZXQvaWRlbnRpdHkvY2xhaW1zL3VzZXJuYW1laW5mb3JtYWwiOiJBZG1pbiBUZXN0IiwiaHR0cHM6Ly90ZWxldHJhY2tpbmcuY2xvdWRhcHAubmV0L2lkZW50aXR5L2NsYWltcy91c2VySWQiOiI0ZmU5OTdmZC00ZGNkLTQxNWItYjJjYi1hOGJkMDBmNjFkYzkiLCJodHRwczovL3RlbGV0cmFja2luZy5jbG91ZGFwcC5uZXQvaWRlbnRpdHkvY2xhaW1zL2ZlYXR1cmV0eXBlaWQiOlsiNCIsIjIiLCIxIiwiMyIsIjUiLCI2Il0sImlzcyI6InRlbGV0cmFja2luZy5jb20iLCJhdWQiOiJodHRwOi8vd3d3LnNlcnZpY2UudGVsZXRyYWNraW5nLmNvbS8iLCJleHAiOjE1NTAwNzM0MzksIm5iZiI6MTU0NzQ4MTQzOX0.UCL-Wc3OSVDI58U5ShOYqLa-DwNc_WQ3BlY5P3CfnVI"""
        audience = 'http://www.service.teletracking.com/'

        secret = 'drMemxWrLen6fCXQA5jO6gXkK/UoZVzPGRDiff7ByPU='
        decoded_token = AuthenticationHandler.validate_and_decode_token(
            token=token, key=secret,
            audience=audience
        )
        self.assertTrue(decoded_token['role'][0] == 'Domain Users', "Group 1 not match")
        self.assertTrue(decoded_token['role'][1] == 'Administrator', "Group 2 not match")

    def test_runtime_method(self):

        import requests

        audience = 'http://www.service.teletracking.com/'
        roles = {'role': ['use'], 'audience': audience}
        secret = 'drMemxWrLen6fCXQA5jO6gXkK/UoZVzPGRDiff7ByPU='
        token = AuthenticationHandler.generate_auth_token(roles, secret)
        print(token)

        headers = {"Authorization": token}
        r = requests.get("http://localhost:5000/app/v1.0/fred", headers=headers)
        print(r.text)
        print(r.status_code)


