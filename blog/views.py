from django.shortcuts import render, redirect
from .models import Post, Categoria, Comment
from .forms import FormularioCrearPost, FormularioEditarPost, FormularioComentario
from django.contrib import messages

# Create your views here.

# Vista para mostrar los post
def blog(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts': posts})


# Vista para mostrar el formulario para crear un post y procesarlo
def create_post(request):
    formularioCrearPost = FormularioCrearPost()

    if request.method == 'POST':
        formulario_crearPost = FormularioCrearPost(data=request.POST,
                                                   files=request.FILES)

        if formulario_crearPost.is_valid():
            titulo = formulario_crearPost.cleaned_data['titulo']
            contenido = formulario_crearPost.cleaned_data['contenido']
            imagen = formulario_crearPost.cleaned_data['imagen']
            categorias = formulario_crearPost.cleaned_data['categorias']

            # Crear el post y guardar en la base de datos
            post = Post(
                titulo=titulo,
                contenido=contenido,
                imagen=imagen,
                autor=request.user
            )
            post.save()  # Guardar el post para poder asignarle categorías

            # Asignar las categorías al post
            post.categorias.set(categorias)
            post.save()
            
            messages.success(request, 'Post creado exitosamente')

            return redirect(f'/blog/post?post_id={post.id}')

    return render(request, 'post/createPost.html',
                  {'formularioCrearPost': formularioCrearPost})


# Vista para mostrar los detalles de un post
def read_post(request):
    
    formularioComentario = FormularioComentario() 
    post_id = request.GET.get('post_id')
    post = Post.objects.get(pk=post_id)
    comentarios = Comment.objects.filter(post=post)
    
    if request.method == 'POST':
        formularioComentario = FormularioComentario(data=request.POST)
    
        if formularioComentario.is_valid():
            comentario = Comment(
                texto = formularioComentario.cleaned_data["texto"],
                autor = request.user,
                post = post
        )
        
        comentario.save()
        
        return redirect(f'/blog/post?post_id={post.id}')
        
    return render(request, 'post/readPost.html',{'post':post, 'formularioComentario': formularioComentario, 'comentarios': comentarios})

# Vista para borrar un post
def delete_post(request):
    post_id = request.GET.get('post_id')
    post = Post.objects.get(pk=post_id)
    post.delete()
    messages.success(request, 'Post eliminado exitosamente')
    return redirect('Blog')

# Vista para editar un post
def edit_post(request):
    post_id = request.GET.get('post_id')
    post = Post.objects.get(pk=post_id)
    
    if request.method == 'POST':
        formularioEditarPost = FormularioEditarPost(request.POST, request.FILES, post = post)
        if formularioEditarPost.is_valid():
            post.titulo = formularioEditarPost.cleaned_data["titulo"]
            post.contanido = formularioEditarPost.cleaned_data["contenido"]
            if formularioEditarPost.cleaned_data["imagen"]:
                post.imagen = formularioEditarPost.cleaned_data["imagen"]
            post.categorias.set(formularioEditarPost.cleaned_data["categorias"])
            post.save()
            return redirect(f'/blog/post?post_id={post.id}')
    else:
        formularioEditarPost = FormularioEditarPost(post=post)
        
    return render(request, 'post/editPost.html',{'post':post, 'formularioEditarPost':formularioEditarPost})

# Vista para crear un comentario asociado a un post
def CreateComment(request):
    formularioComentario = FormularioComentario(data=request.POST)
    
    if formularioComentario.is_valid():
        comentario = Comment(
            texto = formularioComentario.cleaned_data["texto"],
            autor = request.user
            
        )
        
        comentario.save()
        messages.success(request, 'Comentario creado exitosamente')
        return redirect('Blog')

def DeleteComment(request):
    comment_id = request.GET.get('comment_id')
    comment = Comment.objects.get(pk=comment_id)
    post_id = comment.post_id
    comment.delete()
    messages.success(request, 'Comentario eliminado exitosamente')
    return redirect(f'/blog/post?post_id={post_id}')