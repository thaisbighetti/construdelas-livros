from django.contrib import admin

from livros.models import Livro


class LivroAdmin(admin.ModelAdmin):
    ordering = ["titulo", "numero_de_paginas", "editora", "data_criacao"]
    search_fields = ["titulo", "numero_de_paginas", "editora", "data_criacao"]
    list_display = ["titulo", "numero_de_paginas", "editora", "data_criacao"]
    list_filter = ["titulo", "numero_de_paginas", "editora", "data_criacao"]


admin.site.register(Livro, LivroAdmin)
