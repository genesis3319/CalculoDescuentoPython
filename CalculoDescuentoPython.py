def calcular_descuento(monto_total, porcentaje_descuento=15):
    """
    Calcula el monto del descuento y el monto final a pagar.

    :param monto_total: Monto total de la compra.
    :param porcentaje_descuento: Porcentaje de descuento a aplicar (por defecto 15%).
    :return: Monto del descuento y monto final a pagar.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    monto_final = monto_total - descuento
    return descuento, monto_final

def main():
    # Esta es la primera llamada a la función con monto total
    monto1 = 250.00
    descuento1, monto_final1 = calcular_descuento(monto1)
    print(f"Compra de ${monto1:.2f}:")
    print(f"Descuento: ${descuento1:.2f}")
    print(f"Monto final a pagar: ${monto_final1:.2f}\n")

    # Esta es la segunda llamada a la función con monto total y porcentaje de descuento
    monto2 = 300.00
    porcentaje_descuento2 = 18
    descuento2, monto_final2 = calcular_descuento(monto2, porcentaje_descuento2)
    print(f"Compra de ${monto2:.2f} con un descuento del {porcentaje_descuento2}%:")
    print(f"Descuento: ${descuento2:.2f}")
    print(f"Monto final a pagar: ${monto_final2:.2f}")

if __name__ == "__main__":
    main()