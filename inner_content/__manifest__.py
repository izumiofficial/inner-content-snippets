{
    'name': "Website Inner Content",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "Shahrul Izlan",
    'website': "https://www.computs.com.my",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/snippets.xml',
    ],
    'assets': {
        'website.website_builder_assets': [
            'inner_content/static/src/js/inner_content_plugin.js',
        ],
        'web.assets_frontend': [
            'inner_content/static/src/scss/inner_content_slides.scss',
        ],
    }
    'installable': True,
    'application': False,
    'license': 'GPL-3.0'
}

