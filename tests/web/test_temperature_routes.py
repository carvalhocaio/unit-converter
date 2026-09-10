def test_get_temperature_form_uses_degree_labels(client):
    response = client.get("/temperature")
    assert response.status_code == 200
    assert "Celsius (°C)" in response.text
    assert "Fahrenheit (°F)" in response.text
    assert "Kelvin (K)" in response.text
    assert "Kelvin (°K)" not in response.text


def test_get_temperature_result_renders_summary(client):
    response = client.get(
        "/temperature",
        params={"value": "100", "from": "celsius", "to": "fahrenheit", "result": "212"},
    )
    assert response.status_code == 200
    assert "100 celsius = 212 fahrenheit" in response.text


def test_post_temperature_invalid_unit_redirects_303_with_error(client):
    response = client.post(
        "/temperature",
        data={"value": "100", "from": "celsius", "to": "rankine"},
        follow_redirects=False,
    )
    assert response.status_code == 303
    assert "error=Please+enter" in response.headers["location"]
