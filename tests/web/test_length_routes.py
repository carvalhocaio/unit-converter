def test_root_redirects_to_length(client):
    response = client.get("/", follow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"] == "/length"


def test_get_length_form_renders_default_fields(client):
    response = client.get("/length")
    assert response.status_code == 200
    assert "Enter the length to convert" in response.text
    assert '<option value="kilometer">Kilometer</option>' in response.text
    assert "error" not in response.text.lower()
    assert "result-value" not in response.text


def test_post_valid_length_conversion_redirects_303_with_result(client):
    response = client.post(
        "/length",
        data={"value": "1", "from": "meter", "to": "centimeter"},
        follow_redirects=False,
    )
    assert response.status_code == 303
    location = response.headers["location"]
    assert location.startswith("/length?")
    assert "result=100" in location


def test_get_length_result_renders_summary(client):
    response = client.get(
        "/length",
        params={"value": "1", "from": "meter", "to": "centimeter", "result": "100"},
    )
    assert response.status_code == 200
    assert "1 meter = 100 centimeter" in response.text
    assert 'href="/length"' in response.text


def test_post_invalid_length_value_redirects_303_with_error(client):
    response = client.post(
        "/length",
        data={"value": "abc", "from": "meter", "to": "centimeter"},
        follow_redirects=False,
    )
    assert response.status_code == 303
    location = response.headers["location"]
    assert "error=Please+enter+a+valid+number+and+choose+valid+units" in location


def test_get_length_error_renders_message(client):
    response = client.get(
        "/length",
        params={"error": "Please enter a valid number and choose valid units"},
    )
    assert response.status_code == 200
    assert (
        '<p class="error">Please enter a valid number and choose valid units</p>'
        in response.text
    )
