
1. how to add pagination to page (example: gallery):
    1) add script to gallery.html
       ```
       {% block scripts %} 
           <script>
                initPagination(list route, container(f.e. '.content-container')) 
           </script>
       {% endblock %}
       ```
    2) make file gallery_content.html with only {% block %} content (just copy it)
    3) add to bottom of gallery.html's content block 
       a code from pagination.html
    4) ```
       if page_number:
            return render(request, 'gallery_content.html', template_variables)
       ```
