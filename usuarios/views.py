from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import PerfilForm, DataForm
from django.views.decorators.csrf import ensure_csrf_cookie
from .models import Perfil, Data
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, 'As senhas não coincidem')
            return redirect('register')
        if len(password1) < 5:
            messages.error(request, 'A senha deve ter pelo menos 5 dígitos')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe')
            return redirect('register')

        User.objects.create_user(username=username, password=password1)
        user = authenticate(request, username=username, password=password1)
        auth_login(request, user)
        messages.success(request, f'Usuário registrado com sucesso!\nBem vindo(a) {username}')
        return redirect('inicio')
        
    return render(request, 'cadastrouser.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, f'Bem-vindo, {username}')
            return redirect('inicio')
        else:
            messages.error(request, 'Credenciais inválidas.')
            return redirect('login')
        
    return render(request, 'login.html')

@login_required
def cadastro_perfil(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        genero = request.POST['genero']
        endereco = request.POST['endereco']
        
        if '.' not in email or "@" not in email:
            messages.error(request, 'Email Inválido')
            return redirect('attperfil')
            
        perfil, criado = Perfil.objects.update_or_create(
            usuario=request.user,
            defaults={
                'nome': nome,
                'email': email,
                'genero': genero,
                'endereco': endereco,
            }
        )
        
        msg = 'Perfil registrado com sucesso!' if criado else 'Perfil atualizado com sucesso!'
        messages.success(request, msg)
        return redirect('inicio')
    return render(request, 'atualizar_perfil.html', {'perfil': Perfil.objects.filter(usuario=request.user).first()})

@login_required
def cadastro_data(request):
    if request.method == 'POST':
        renda_familiar =  request.POST['renda_familiar']
        num_membros = request.POST['num_membros']
        despesas_mensais = request.POST['despesas_mensais']
        situacao_emprego = request.POST['situacao_emprego']
        tipo_moradia = request.POST['tipo_moradia']
        nivel_escolaridade = request.POST['nivel_escolaridade']
        
        if float(renda_familiar) < 0:
            messages.error(request, 'A renda familiar não pode ser negativa.')
            return redirect('attdata')

        if int(num_membros) <= 0:
            messages.error(request, 'O número de membros deve ser maior que zero.')
            return redirect('attdata')

        if float(despesas_mensais) < 0:
            messages.error(request, 'As despesas mensais não podem ser negativas.')
            return redirect('attdata')
        
        data, criado = Data.objects.update_or_create(
            usuario=request.user,
            defaults={
                'renda_familiar': renda_familiar,
                'num_membros': num_membros,
                'despesas_mensais': despesas_mensais,
                'situacao_emprego': situacao_emprego,
                'tipo_moradia': tipo_moradia,
                'nivel_escolaridade': nivel_escolaridade
            }
        )
        
        msg = 'Data registrada com sucesso!' if criado else 'Data atualizada com sucesso!'
        messages.success(request, msg)
        return redirect('inicio')
    return render(request, 'atualizar_dados.html', {'data': Data.objects.filter(usuario=request.user).first()})

@login_required
def inicio(request):
    return render(request, 'inicio.html', {'user': request.user})
    

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def gerar_pdf(request):
    try:
        perfil = Perfil.objects.get(usuario=request.user)
        data = Data.objects.get(usuario=request.user)
    except (Perfil.DoesNotExist, Data.DoesNotExist):
        return HttpResponse('Perfil ou Dados não encontrados.')

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="dados_cadastrais.pdf"'

    pdf = canvas.Canvas(response, pagesize=letter)
    

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(100, 800, "Dados Cadastrais - Programa Social")
    pdf.setFont("Helvetica", 12)
    
    
    

    y_position = 750
    pdf.drawString(100, y_position, "Perfil:")
    y_position -= 20
    pdf.drawString(120, y_position, f"Nome: {perfil.nome}")
    y_position -= 15
    pdf.drawString(120, y_position, f"Email: {perfil.email}")
    y_position -= 15
    pdf.drawString(120, y_position, f"Gênero: {perfil.get_genero_display()}")
    y_position -= 15
    pdf.drawString(120, y_position, f"Endereço: {perfil.endereco}")


    y_position -= 30
    pdf.drawString(100, y_position, "Informações Socioeconômicas:")
    y_position -= 20
    pdf.drawString(120, y_position, f"Renda Familiar: R$ {data.renda_familiar}")
    y_position -= 15
    pdf.drawString(120, y_position, f"Número de Membros: {data.num_membros}")
    y_position -= 15
    pdf.drawString(120, y_position, f"Despesas Mensais: R$ {data.despesas_mensais}")
    y_position -= 15
    pdf.drawString(120, y_position, f"Situação de Emprego: {data.get_situacao_emprego_display()}")
    y_position -= 15
    pdf.drawString(120, y_position, f"Tipo de Moradia: {data.get_tipo_moradia_display()}")
    y_position -= 15
    pdf.drawString(120, y_position, f"Nível de Escolaridade: {data.get_nivel_escolaridade_display()}")


    pdf.showPage()
    pdf.save()

    return response