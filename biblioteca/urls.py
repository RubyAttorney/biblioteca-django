from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from emprestimos.views import home, detalhar_livro, fazer_emprestimo, historico_emprestimo, fazer_devolucao, cadastrar_livro, atualizar_livro, meus_livros, deletar_livro
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='home'),
    path('detalhar_livro/<int:id>', detalhar_livro,name='detalhar_livro'),
    path('fazer_emprestimo/<int:id>', fazer_emprestimo,name='fazer_emprestimo'),
    path('historico_emprestimo/',historico_emprestimo, name='historico_emprestimo'),
    path('fazer_devolucao/<int:id>',fazer_devolucao, name='fazer_devolucao'),
    path('cadastrar_livro/',cadastrar_livro, name='cadastrar_livro'),
    path('atualizar_livro/<int:id>',atualizar_livro, name='atualizar_livro'),
    path('meus_livros/',meus_livros, name='meus_livros'),
    path('deletar_livro/<int:id>',deletar_livro, name='deletar_livro'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
