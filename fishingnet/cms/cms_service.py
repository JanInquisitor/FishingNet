fake_db = {
    '/company/history': {
        'page_title': 'Company history',
        'page_details': 'Details about company history...'
    },
    '/company/employees': {
        'page_title': 'Our team',
        'page_details': 'Details about company employees...'
    }
}


class cms_service:
    def __init__(self):
        pass

    def get_page(url: str) -> dict:
        if not url:
            return {}
        url = url.strip().lower()
        url = '/' + url.lstrip('/')
        page = fake_db.get(url, {})
        return page

