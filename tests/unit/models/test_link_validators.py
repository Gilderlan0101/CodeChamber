import pytest

from application.src.models.link_validators import validate_links


@pytest.mark.parametrize(
    "github, linkedin, site",
    [
        (
            ("https://github.com/username", True),
            ("https://linkedin.com/in/username", True),
            ("https://example.com", True),
        ),
        (
            ("https://github.com/username/xxx", False),
            ("https://linkedin.com/in/username", False),
            ("https://example.com", False),
        ),
        (
            ("https://github.com/username", True),
            ("https://linkedi.com/in/username", False),
            ("htps://example.com", False),
        ),
        (
            ("htps://github.com/username", False),
            ("https://linkedin.com/in/username", True),
            ("ttps://example.com", False),
        ),
        (
            ("htps://github.com/username", False),
            ("htps://linkedin.com/in/username", False),
            ("https://example.com", True),
        ),
        (
            ("https://linkedin.com/in/username", False),
            ("https://example.com", False),
            ("https://github.com/username", True),
        ),
    ],
)
def test_validate_links(github, linkedin, site):
    github, github_valid = github
    linkedin, linkedin_valid = linkedin
    site, site_regex = site
    result = validate_links(github, linkedin, site)

    assert result == {
        "github_valid": github_valid,
        "linkedin_valid": linkedin_valid,
        "site_regex": site_regex,
    }
