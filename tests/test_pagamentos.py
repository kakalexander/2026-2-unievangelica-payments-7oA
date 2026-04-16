import pytest
from app.pagamentos import (
    calcular_desconto,
    aplicar_juros_atraso,
    validar_metodo_pagamento,
    processar_reembolso
)

def test_calcular_desconto():
    # Arrange
    valor = 100
    percentual = 10
    
    # Act
    resultado = calcular_desconto(valor, percentual)
    
    # Assert
    assert resultado == 90

def test_aplicar_juros_atraso():
    # Arrange
    valor_pago = 100
    dias_atraso = 5
    dias_ok = 0
    
    # Act
    resultado_com_atraso = aplicar_juros_atraso(valor_pago, dias_atraso)
    resultado_sem_atraso = aplicar_juros_atraso(valor_pago, dias_ok)
    
    # Assert
    assert resultado_com_atraso == 105.0
    assert resultado_sem_atraso == 100.0

def test_validar_metodo_pagamento():
    # Arrange
    metodos_aceitos = ["pix", "cartao_credito", "cartao_debito", "boleto"]
    metodos_rejeitados = ["cheque", "dinheiro", "transferencia", "crypto"]
    
    # Act
    resultados_aceitos = [validar_metodo_pagamento(m) for m in metodos_aceitos]
    resultados_rejeitados = [validar_metodo_pagamento(m) for m in metodos_rejeitados]
    
    # Assert
    assert all(resultados_aceitos)
    assert not any(resultados_rejeitados)

def test_processar_reembolso():
    # Arrange
    valor_pago = 200.0
    valor_reembolso_parcial = 100.0
    valor_reembolso_exato = 200.0
    valor_reembolso_estouro = 201.0
    
    # Act
    resultado_parcial = processar_reembolso(valor_pago, valor_reembolso_parcial)
    resultado_exato = processar_reembolso(valor_pago, valor_reembolso_exato)
    resultado_estouro = processar_reembolso(valor_pago, valor_reembolso_estouro)
    
    # Assert
    assert resultado_parcial == 100.0
    assert resultado_exato == 0.0      # // Caso de Valor Limite
    assert resultado_estouro == -1     # // Caso de Valor Limite
