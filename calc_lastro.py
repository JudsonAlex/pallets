def calcular_combinacao_caixas(pallet_largura, pallet_comprimento, caixa_largura, caixa_comprimento):
    # Opção 1: Caixas na orientação original
    caixas_largura_original = pallet_largura // caixa_largura
    caixas_comprimento_original = pallet_comprimento // caixa_comprimento
    total_original = caixas_largura_original * caixas_comprimento_original
    espaco_largura_restante_1 = pallet_largura - (caixas_largura_original * caixa_largura)
    espaco_comprimento_restante_1 = pallet_comprimento - (caixas_comprimento_original * caixa_comprimento)

    # Opção 2: Caixas na orientação rotacionada
    caixas_largura_rotacionada = pallet_largura // caixa_comprimento
    caixas_comprimento_rotacionada = pallet_comprimento // caixa_largura
    total_rotacionada = caixas_largura_rotacionada * caixas_comprimento_rotacionada
    espaco_largura_restante_2 = pallet_largura - (caixas_largura_rotacionada * caixa_comprimento)
    espaco_comprimento_restante_2 = pallet_comprimento - (caixas_comprimento_rotacionada * caixa_largura)

    # Combinação 1: Original + Rotacionada no espaço restante
    caixas_rotacionadas_no_espaco_restante_1 = (espaco_largura_restante_1 // caixa_comprimento) * (pallet_comprimento // caixa_largura)
    caixas_rotacionadas_no_espaco_restante_1 += (espaco_comprimento_restante_1 // caixa_largura) * (pallet_largura // caixa_comprimento)
    total_combinado_1 = total_original + caixas_rotacionadas_no_espaco_restante_1

    # Combinação 2: Rotacionada + Original no espaço restante
    caixas_originais_no_espaco_restante_2 = (espaco_largura_restante_2 // caixa_largura) * (pallet_comprimento // caixa_comprimento)
    caixas_originais_no_espaco_restante_2 += (espaco_comprimento_restante_2 // caixa_comprimento) * (pallet_largura // caixa_largura)
    total_combinado_2 = total_rotacionada + caixas_originais_no_espaco_restante_2

    # Verifica qual combinação maximiza o número de caixas
    if total_combinado_1 > total_combinado_2:
        return (total_original, caixas_rotacionadas_no_espaco_restante_1, total_combinado_1)
    else:
        return (caixas_originais_no_espaco_restante_2, total_rotacionada, total_combinado_2)

# Exemplo de uso:
pallet_largura = 120  # largura do pallet em cm
pallet_comprimento = 100  # comprimento do pallet em cm
caixa_largura = 30  # largura da caixa em cm
caixa_comprimento = 40  # comprimento da caixa em cm

caixas_original, caixas_rotacionadas, total_maximo = calcular_combinacao_caixas(pallet_largura, pallet_comprimento, caixa_largura, caixa_comprimento)

print(f"Caixas na orientação original: {caixas_original}")
print(f"Caixas na orientação rotacionada: {caixas_rotacionadas}")
print(f"Total máximo de caixas no pallet: {total_maximo}")