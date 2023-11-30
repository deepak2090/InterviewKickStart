
# custom_pytest_html.py
from pytest_html import _markup

def pytest_configure(config):
    config._html = config._html or {}
    config._html['template'] = '/Users/deepakdas/InterviewKickStart/InterviewKickStart-1/pytest/custom_template.html'
    _markup._default_stylesheet = None

def pytest_html_report_title(report):
    report.title = "Custom Pytest Report"
    report.header = "Your Custom Header Content (if needed)"

# Add this line to indicate the custom plugin
pytest_plugins = ["custom_pytest_html"]
