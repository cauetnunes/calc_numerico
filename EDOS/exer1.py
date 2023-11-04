def dydx(x, y):
    return (y**2 - 2*x)/y

# Método de Euler
def euler_method(h, x_end):
    n = int(x_end/h)
    y = 1.0 # condição inicial
    x = 0.0
    for i in range(n):
        y += h * dydx(x, y)
        x += h
    return y

# Método de Runge-Kutta de 3ª ordem
def runge_kutta_3rd_order(h, x_end):
    n = int(x_end/h)
    y = 1.0 # condição inicial
    x = 0.0
    for i in range(n):
        k1 = h * dydx(x, y)
        k2 = h * dydx(x + 0.5*h, y + 0.5*k1)
        k3 = h * dydx(x + h, y - k1 + 2*k2)
        y += (k1 + 4*k2 + k3)/6.0
        x += h
    return y

h = 0.2
x_end = 1.0
y_euler = euler_method(h, x_end)
y_rk3 = runge_kutta_3rd_order(h, x_end)


results = {
    "Método de Euler": y_euler,
    "Runge-Kutta 3ª ordem": y_rk3,  
}

print(f"Valor aproximado usando Euler: {y_euler}")
print(f"Valor aproximado usando Runge-Kutta de 3ª ordem: {y_rk3}")


y_exato = 3**0.5

erro_euler = abs((y_exato-y_euler)/y_exato) * 100
erro_rk3 = abs((y_exato-y_rk3)/y_exato) * 100

print(f"O erro absoluto do método de Euler foi: {erro_euler:.2f}%")
print(f"O erro absoluto do metodo de runge kutta foi: {erro_rk3:.2f}%")