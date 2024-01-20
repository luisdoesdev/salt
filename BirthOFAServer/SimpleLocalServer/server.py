from core.create_html import CreateHTML

import webbrowser
import os


create_html = CreateHTML(
    "Luis blog",
    {
        "title":"Main Article",
        "img":"https://plus.unsplash.com/premium_photo-1694628173757-75415b0c3eb5?q=80&w=3409&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
     },
)
# create_html.build_content('Luis Title')
webbrowser.open(create_html.build_url())