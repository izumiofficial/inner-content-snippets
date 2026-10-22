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
    'depends': ['base','website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/snippets.xml',
        'views/snippet_options.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'inner_content/static/src/js/frontend.js',
        ],
        'website.assets_wysiwyg': [
            'inner_content/static/src/js/options.js',
        ],
    },

    'installable': True,
    'application': False,
    'license': 'LGPL-3'
}

