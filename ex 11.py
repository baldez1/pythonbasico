larg = float(input('Qual é a largura da parede: '))
alt = float(input('Qual é a altura da parede: '))
área = larg * alt
print('Sua parede tem dimensão de {}x{} e sua área é de {}m². '.format(larg, alt, área))
tinta = área / 2
print('Para pintar sua parede você precisará de {}l de tinta.'.format(tinta))