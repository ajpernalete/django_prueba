from django.shortcuts import render

def cart(request):
    #Crear una session
    #request.session['cart_id'] = '123' #Dic

    #Obtener valor de una session
    valor = request.session.get('cart_id')
    print(valor)

    #Eliminar una session
    request.session['cart_id'] = None

    return render(request, 'carts/cart.html', {
        
    })
